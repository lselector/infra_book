#!/usr/bin/env python3
"""Download source documents into the wiki Raw/ tree.

Reads the source list in raw_sources.json (category,
filename, title, URL), fetches each URL, converts HTML
to clean Markdown, and writes the result into
Context-Wiki-Infra/Raw/<category>/<filename>.

Each saved file gets a short provenance header with the
source URL and retrieval date. Files already present are
skipped unless --force is given, so the script is safe
to re-run after fixing a few broken URLs.

Usage:
    python raw_download.py              # fetch missing
    python raw_download.py --force      # re-fetch all
    python raw_download.py --only caddy # filter by text
    python raw_download.py --registry   # rebuild sources.md

Created: 2026-07-27
Last updated: 2026-07-27
"""

import concurrent.futures as cf
import datetime as dt
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

import html2text
import requests
from bs4 import BeautifulSoup

HERE = Path(__file__).parent
SOURCES = HERE / "raw_sources.json"
RAW = HERE / "Context-Wiki-Infra" / "Raw"
REGISTRY = RAW / "sources.md"
TAIL_MARK = "## Local reference implementations"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,"
              "text/markdown,text/plain;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

MAIN_SELECTORS = [
    "main", "article", "[role=main]", "#main-content",
    "#main_content", "#content", ".content",
    ".devsite-article-body", ".markdown-body",
    "#docs-content", ".docs-content", "#mw-content-text",
]

DROP_TAGS = [
    "script", "style", "noscript", "nav", "header",
    "footer", "aside", "form", "svg", "iframe",
    "template", "button",
]

DROP_SELECTORS = [
    ".sidebar", ".toc", "#toc", ".breadcrumb",
    ".breadcrumbs", ".navbar", ".site-header",
    ".site-footer", ".cookie", ".banner", ".feedback",
    ".devsite-book-nav", ".devsite-footer",
    ".page-nav", ".pagination", ".edit-this-page",
]

CATEGORY_TITLES = {
    "01_foundations":
        "01_foundations — thinking about infrastructure",
    "02_architectures":
        "02_architectures — static sites to multi-tenant "
        "SaaS (incl. mobile / PWA)",
    "03_deployments":
        "03_deployments — Cloudflare, VPS/Linux setup, "
        "Caddy/Nginx, PaaS, serverless, containers",
    "04_network_storage_db":
        "04_network_storage_db — networking, storage, "
        "databases (SQLite, self-hosted PostgreSQL)",
    "05_ops_cicd_security":
        "05_ops_cicd_security — CI/CD, monitoring, "
        "security, authentication, cost",
    "06_product_patterns":
        "06_product_patterns — infra by product type "
        "(incl. landing pages / email capture)",
    "07_playbooks":
        "07_playbooks — recipes and checklists",
    "08_scaling_maturity":
        "08_scaling_maturity — environments, IaC, scaling",
    "09_appendices":
        "09_appendices — starter stacks, diagrams, "
        "further reading, case study",
    "12_ai_in_saas":
        "12_ai_in_saas — adding an AI assistant to a SaaS "
        "(LLM APIs, streaming, limits, abuse protection)",
}


# --------------------------------------------------------------
def load_sources():
    """Load the source list from raw_sources.json."""
    with open(SOURCES, encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------
def fix_encoding(rsp, ctype):
    """Stop requests defaulting text/* to ISO-8859-1."""
    # Without an explicit charset, requests assumes
    # ISO-8859-1 and UTF-8 punctuation turns into
    # mojibake. Sniff the bytes instead.
    if "charset" in ctype.lower():
        return
    rsp.encoding = rsp.apparent_encoding or "utf-8"


# --------------------------------------------------------------
def fetch(url, tries=3):
    """GET a URL, returning (text, content_type)."""
    last = None
    for attempt in range(tries):
        try:
            rsp = requests.get(
                url, headers=HEADERS, timeout=40
            )
            rsp.raise_for_status()
            ctype = rsp.headers.get("content-type", "")
            fix_encoding(rsp, ctype)
            return rsp.text, ctype.lower()
        except Exception as err:      # noqa: BLE001
            last = err
    raise RuntimeError(str(last))


# --------------------------------------------------------------
def strip_noise(soup):
    """Remove scripts, chrome, and navigation elements."""
    for tag in soup(DROP_TAGS):
        tag.decompose()
    for sel in DROP_SELECTORS:
        for tag in soup.select(sel):
            tag.decompose()
    return soup


# --------------------------------------------------------------
def pick_main(soup):
    """Return the best content container in the page."""
    for sel in MAIN_SELECTORS:
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 400:
            return node
    return soup.body or soup


# --------------------------------------------------------------
def make_converter():
    """Build a configured html2text converter."""
    conv = html2text.HTML2Text()
    conv.body_width = 0
    conv.ignore_images = True
    conv.ignore_emphasis = False
    conv.protect_links = False
    conv.single_line_break = False
    conv.mark_code = False
    return conv


# --------------------------------------------------------------
def absolutize(soup, base_url):
    """Rewrite relative href/src values to absolute URLs."""
    for tag in soup.find_all(href=True):
        tag["href"] = urljoin(base_url, tag["href"])
    for tag in soup.find_all(src=True):
        tag["src"] = urljoin(base_url, tag["src"])
    return soup


# --------------------------------------------------------------
def html_to_md(html, base_url, strip=True):
    """Convert an HTML page to reasonably clean Markdown."""
    # Pick the main container first, then strip chrome
    # inside it: badly nested pages would otherwise lose
    # the whole body to a stray unclosed <nav>.
    soup = BeautifulSoup(html, "html.parser")
    absolutize(soup, base_url)
    node = pick_main(soup)
    if strip:
        strip_noise(node)
    out = tidy(make_converter().handle(str(node)))
    if len(out) < 500 and strip:
        return html_to_md(html, base_url, strip=False)
    return out


# --------------------------------------------------------------
def tidy(text):
    """Collapse runs of blank lines and trailing spaces."""
    out, blanks = [], 0
    for line in text.splitlines():
        line = line.rstrip()
        blanks = blanks + 1 if not line else 0
        if blanks > 2:
            continue
        out.append(line)
    return "\n".join(out).strip() + "\n"


# --------------------------------------------------------------
def header(item, today):
    """Build the provenance header for a Raw file."""
    return (
        f"<!--\n"
        f"title: {item['title']}\n"
        f"source: {item['url']}\n"
        f"retrieved: {today}\n"
        f"category: {item['cat']}\n"
        f"note: immutable source capture - do not edit\n"
        f"-->\n\n"
        f"# {item['title']}\n\n"
        f"Source: <{item['url']}>\n\n"
        f"---\n\n"
    )


# --------------------------------------------------------------
def is_markdown(url, ctype):
    """True when the response is already plain text/md."""
    if url.endswith((".md", ".txt")):
        return True
    return ("markdown" in ctype
            or ctype.startswith("text/plain"))


# --------------------------------------------------------------
def download_one(item, force=False):
    """Fetch and save a single source; return a status."""
    dest = RAW / item["cat"] / item["file"]
    if dest.exists() and not force:
        return ("skip", item, f"{dest.name} exists")
    try:
        text, ctype = fetch(item["url"])
    except Exception as err:          # noqa: BLE001
        return ("fail", item, str(err)[:120])
    if is_markdown(item["url"], ctype):
        body = tidy(text)
    else:
        body = html_to_md(text, item["url"])
    if len(body) < 500:
        return ("fail", item,
                f"too short ({len(body)} chars)")
    today = dt.date.today().isoformat()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header(item, today) + body,
                    encoding="utf-8")
    return ("ok", item, f"{len(body):,} chars")


# --------------------------------------------------------------
def run(items, force=False, workers=8):
    """Download all items in parallel; return results."""
    results = []
    with cf.ThreadPoolExecutor(workers) as pool:
        futs = {
            pool.submit(download_one, it, force): it
            for it in items
        }
        for fut in cf.as_completed(futs):
            state, item, note = fut.result()
            results.append((state, item, note))
            flag = {"ok": "OK  ", "skip": "SKIP",
                    "fail": "FAIL"}[state]
            print(f"{flag} {item['cat']}/"
                  f"{item['file']}  {note}",
                  flush=True)
    return results


# --------------------------------------------------------------
def registry_body(items):
    """Render the per-category section of sources.md."""
    lines = ["# Raw Sources Registry", "",
             "Source URL for every file in `Raw/`. Files",
             "in `Raw/` are immutable — never edit them;",
             "re-download from the URL if needed.", "",
             "Format: `filename | title | source URL`", ""]
    for cat, title in CATEGORY_TITLES.items():
        lines += [f"## {title}", ""]
        rows = [i for i in items if i["cat"] == cat
                and (RAW / cat / i["file"]).exists()]
        if not rows:
            lines += ["(none yet)", ""]
            continue
        for item in sorted(rows, key=lambda i: i["file"]):
            lines += [f"- `{item['file']}` |",
                      f"  {item['title']} |",
                      f"  {item['url']}"]
        lines += [""]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------
def write_registry(items):
    """Rewrite sources.md, preserving its handwritten tail."""
    old = REGISTRY.read_text(encoding="utf-8")
    tail = ""
    if TAIL_MARK in old:
        tail = old[old.index(TAIL_MARK):]
    REGISTRY.write_text(
        registry_body(items) + tail, encoding="utf-8"
    )
    print(f"registry rewritten: {REGISTRY}")


# --------------------------------------------------------------
def select(items, argv):
    """Filter the source list by an --only substring."""
    if "--only" not in argv:
        return items
    needle = argv[argv.index("--only") + 1].lower()
    return [
        i for i in items
        if needle in i["file"].lower()
        or needle in i["cat"].lower()
        or needle in i["url"].lower()
    ]


# --------------------------------------------------------------
def report(results):
    """Print a summary and list every failed source."""
    counts = {"ok": 0, "skip": 0, "fail": 0}
    for state, _item, _note in results:
        counts[state] += 1
    print("\n--- summary ---")
    print(f"downloaded: {counts['ok']}   "
          f"skipped: {counts['skip']}   "
          f"failed: {counts['fail']}")
    fails = [(i, n) for s, i, n in results if s == "fail"]
    if fails:
        print("\nfailed sources:")
        for item, note in sorted(
            fails, key=lambda f: f[0]["file"]
        ):
            print(f"  {item['file']}  {item['url']}")
            print(f"      -> {note}")


# --------------------------------------------------------------
def main():
    """Download sources, then refresh the registry."""
    argv = sys.argv[1:]
    items = load_sources()
    if "--registry" in argv:
        write_registry(items)
        return
    force = "--force" in argv
    results = run(select(items, argv), force=force)
    report(results)
    write_registry(items)


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
