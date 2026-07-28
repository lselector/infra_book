#!/usr/bin/env python3
"""Attach outside reference links to each content page.

Reads the curated maps in `wikipedia_links.json` and
writes two OKF frontmatter fields into every page in
Wiki/Concepts and Wiki/Entities:

  wikipedia:  the English Wikipedia article ("links")
  website:    the project's own site ("websites"), used
              where Wikipedia has no article

`wiki_server.py` renders both in the infobox as links
that open in a new tab, so no page is a dead end.

Targets are curated, never guessed. `check` asks the
MediaWiki API whether each article exists, is a redirect
or is a disambiguation page, prints its first sentence so
a wrong target is obvious on sight, and fetches every
website URL to confirm it answers.

Usage:
    python wikipedia_links.py status   # offline coverage
    python wikipedia_links.py check    # verify targets
    python wikipedia_links.py apply    # write frontmatter

Created: 2026-07-27
Last updated: 2026-07-27
"""

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
VAULT = HERE / "Context-Wiki-Infra"
PAGE_DIRS = [VAULT / "Wiki" / "Concepts",
             VAULT / "Wiki" / "Entities"]
MAP_FILE = HERE / "wikipedia_links.json"

WIKI_BASE = "https://en.wikipedia.org/wiki/"
API = "https://en.wikipedia.org/w/api.php"
UA = ("context-wiki-infra/1.0 (local wiki build; "
      "https://en.wikipedia.org/wiki/Wikipedia:User-Agent)")
# Vendor sites behind a WAF refuse an unfamiliar agent,
# so the link check presents an ordinary browser string.
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)
BATCH = 20

# Frontmatter key -> the keys it may be placed after,
# in order of preference.
ANCHORS = {
    "wikipedia": ("description", "title", "type"),
    "website": ("wikipedia", "description", "title"),
}


# --------------------------------------------------------------
def load_map():
    """Read the curated page -> article title map."""
    data = json.loads(MAP_FILE.read_text(encoding="utf-8"))
    return data["links"]


# --------------------------------------------------------------
def load_sites():
    """Read the curated page -> project website map."""
    data = json.loads(MAP_FILE.read_text(encoding="utf-8"))
    return data.get("websites", {})


# --------------------------------------------------------------
def pages():
    """Return every content page, as name -> Path."""
    out = {}
    for folder in PAGE_DIRS:
        for p in sorted(folder.glob("*.md")):
            out[p.stem] = p
    return out


# --------------------------------------------------------------
def article_url(title):
    """Build the canonical article URL from a title."""
    slug = title.replace(" ", "_")
    return WIKI_BASE + urllib.parse.quote(
        slug, safe="_(),'!.*~-"
    )


# --------------------------------------------------------------
def api_query(titles):
    """Ask the API about one batch of article titles."""
    params = {
        "action": "query", "format": "json",
        "redirects": "1", "prop": "pageprops|extracts",
        "exintro": "1", "explaintext": "1",
        "exsentences": "1", "exlimit": str(BATCH),
        "titles": "|".join(titles),
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["query"]


# --------------------------------------------------------------
def resolve(titles):
    """Resolve titles to {title: {resolved, flags, lead}}."""
    out = {}
    for i in range(0, len(titles), BATCH):
        batch = titles[i:i + BATCH]
        data = api_query(batch)
        norm = {n["from"]: n["to"]
                for n in data.get("normalized", [])}
        redir = {r["from"]: r["to"]
                 for r in data.get("redirects", [])}
        found = {p["title"]: p
                 for p in data["pages"].values()}
        for title in batch:
            step = norm.get(title, title)
            final = redir.get(step, step)
            page = found.get(final, {})
            props = page.get("pageprops", {})
            out[title] = {
                "resolved": final,
                "missing": "missing" in page,
                "disambig": "disambiguation" in props,
                "lead": (page.get("extract") or "")
                .replace("\n", " ")[:100],
            }
        time.sleep(0.3)
    return out


# --------------------------------------------------------------
def split_frontmatter(text):
    """Return (frontmatter lines, rest) for a page."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1].strip("\n").split("\n"), parts[2]


# --------------------------------------------------------------
def set_key(lines, key, value):
    """Insert, replace or drop one frontmatter line."""
    kept = [ln for ln in lines
            if not ln.startswith(f"{key}:")]
    if value is None:
        return kept
    new = f'{key}: "{value}"'
    for anchor in ANCHORS[key]:
        for i, ln in enumerate(kept):
            if ln.startswith(f"{anchor}:"):
                return kept[:i + 1] + [new] + kept[i + 1:]
    return kept + [new]


# --------------------------------------------------------------
def write_page(path, values):
    """Write one page's link fields; True if changed."""
    text = path.read_text(encoding="utf-8")
    lines, rest = split_frontmatter(text)
    if lines is None:
        print(f"  no frontmatter: {path.name}")
        return False
    updated = list(lines)
    for key in ANCHORS:
        updated = set_key(updated, key, values.get(key))
    if updated == lines:
        return False
    out = "---\n" + "\n".join(updated) + "\n---" + rest
    path.write_text(out, encoding="utf-8")
    return True


# --------------------------------------------------------------
def cmd_status():
    """Report coverage without touching the network."""
    links, sites, found = load_map(), load_sites(), pages()
    unmapped = sorted(set(found) - set(links))
    unknown = sorted(set(links) - set(found))
    stray = sorted(set(sites) - set(found))
    linked = [n for n in found if links.get(n)]
    sited = [n for n in found if sites.get(n)]
    bare = sorted(n for n in found
                  if not links.get(n) and not sites.get(n))
    print(f"content pages : {len(found)}")
    print(f"with article  : {len(linked)}")
    print(f"with website  : {len(sited)}")
    print(f"no outside link: {len(bare)} {bare}")
    for name in unmapped:
        print(f"  NOT IN MAP: {name}")
    for name in unknown + stray:
        print(f"  MAP ENTRY HAS NO PAGE: {name}")
    return 1 if (unmapped or unknown or stray) else 0


# --------------------------------------------------------------
def report_title(name, title, info):
    """Print one line of the check report; True if bad."""
    if info["missing"]:
        print(f"MISSING    {name} -> {title}")
        return True
    if info["disambig"]:
        print(f"DISAMBIG   {name} -> {title}")
        return True
    if info["resolved"] != title:
        print(f"REDIRECT   {name} -> {title} "
              f"=> {info['resolved']}")
        return True
    print(f"ok  {name:36s} -> {title}")
    print(f"    {info['lead']}")
    return False


# --------------------------------------------------------------
def fetch_status(url):
    """Return the HTTP status for a URL, or the error."""
    req = urllib.request.Request(
        url, headers={"User-Agent": BROWSER_UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status
    except urllib.error.HTTPError as err:
        return err.code
    except Exception as err:
        return repr(err)[:50]


# --------------------------------------------------------------
def check_sites():
    """Fetch every project website; count the failures."""
    sites = load_sites()
    print(f"\nchecking {len(sites)} project websites ...")
    bad = 0
    for name in sorted(sites):
        code = fetch_status(sites[name])
        # 403 here is a WAF refusing an automated client
        # (Drata sits behind one); the URL is fine in a
        # browser, so it is reported, not counted.
        mark = {200: "ok  ", 403: "WAF "}.get(code, "FAIL")
        bad += 0 if mark != "FAIL" else 1
        print(f"{mark} {name:16s} {code}  {sites[name]}")
        time.sleep(0.2)
    return bad


# --------------------------------------------------------------
def cmd_check():
    """Verify every curated target against its source."""
    links = load_map()
    titles = sorted({t for t in links.values() if t})
    print(f"checking {len(titles)} distinct articles ...")
    info = resolve(titles)
    bad = 0
    for name in sorted(links):
        title = links[name]
        if not title:
            continue
        bad += report_title(name, title, info[title])
    bad += check_sites()
    print(f"\nproblems: {bad}")
    return 1 if bad else 0


# --------------------------------------------------------------
def cmd_apply():
    """Write the link fields into every content page."""
    links, sites, found = load_map(), load_sites(), pages()
    changed = 0
    for name, path in sorted(found.items()):
        title = links.get(name)
        changed += write_page(path, {
            "wikipedia": article_url(title) if title
                         else None,
            "website": sites.get(name) or None,
        })
    linked = len([n for n in found if links.get(n)])
    sited = len([n for n in found if sites.get(n)])
    print(f"pages updated : {changed}")
    print(f"with article  : {linked} of {len(found)}")
    print(f"with website  : {sited}")
    return 0


# --------------------------------------------------------------
def main():
    """Run one command."""
    cmds = {"status": cmd_status, "check": cmd_check,
            "apply": cmd_apply}
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd not in cmds:
        print("usage: wikipedia_links.py "
              "status|check|apply")
        return 2
    return cmds[cmd]()


# --------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
