#!/usr/bin/env python3
"""Serve a context wiki as a local, navigable website.

Renders the Markdown/OKF pages of a context wiki as a
Wikipedia-style site: navigable wiki links, per-section
listings, page infoboxes from OKF frontmatter, backlinks
("what links here"), and full-text search.

"/" serves the page named by HOME_PAGE (Stacks — the
ladder of example stacks); NAV_PAGES are pinned above
the section list in the sidebar.

Usage:
    python wiki_server.py
    # then open http://localhost:8020

    # or in the background, via the control scripts:
    ./server_start.sh / ./server_stop.sh
    ./server_restart.sh

    # serve a different wiki:
    WIKI_ROOT=/path/to/wiki python wiki_server.py

Requires: flask, markdown, pyyaml.

Created: 2026-07-15
Last updated: 2026-07-27
"""

import html
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote

import markdown as md
import yaml
from flask import Flask, abort, request

DEFAULT_ROOT = (
    Path(__file__).parent / "Context-Wiki-Infra"
)
WIKI_ROOT = Path(
    os.environ.get("WIKI_ROOT", DEFAULT_ROOT)
).resolve()
PORT = 8020

SECTION_DIRS = {
    "Concepts": "Wiki/Concepts",
    "Entities": "Wiki/Entities",
    "Summaries": "Wiki/Summaries",
    "Dashboards": "Dashboards",
}

# The page served at "/", and the pages pinned above
# the section list in the sidebar, in order.
HOME_PAGE = "Stacks"
NAV_PAGES = ["Development Setup", "Index"]

RAW_DIR = WIKI_ROOT / "Raw"

LINK_RX = re.compile(
    r"\[\[([^\]|#]+?)(?:\|([^\]]+))?\]\]"
)

MD_EXTS = ["tables", "fenced_code"]

CSS = """
body { margin:0; font-family:-apple-system,
  'Helvetica Neue', Arial, sans-serif;
  color:#202122; background:#f8f9fa; }
a { color:#3366cc; text-decoration:none; }
a:hover { text-decoration:underline; }
.missing { color:#dd3333; }
#topbar { background:#fff;
  border-bottom:1px solid #a7d7f9;
  padding:10px 20px; display:flex;
  align-items:center; gap:24px; }
#topbar h1 { font-size:1.3em; margin:0;
  font-family:'Linux Libertine', Georgia, serif; }
#topbar h1 a { color:#202122; }
#topbar form { margin-left:auto; }
#topbar input[type=text] { padding:6px 10px;
  border:1px solid #a2a9b1; border-radius:2px;
  width:260px; }
.layout { display:flex; max-width:1200px;
  margin:0 auto; }
nav { width:180px; padding:20px 12px;
  font-size:0.9em; flex-shrink:0; }
nav h3 { font-size:0.85em; color:#54595d;
  border-bottom:1px solid #c8ccd1;
  padding-bottom:4px; }
nav ul { list-style:none; padding-left:6px;
  margin:6px 0; }
nav li { margin:4px 0; }
nav li.home { font-weight:bold; }
nav hr { border:0;
  border-top:1px solid #eaecf0; margin:8px 6px; }
main { flex:1; background:#fff;
  border:1px solid #a7d7f9; padding:24px 32px;
  margin:16px 0; min-height:70vh; }
main h1, main h2, main h3 {
  font-family:'Linux Libertine', Georgia, serif;
  font-weight:normal;
  border-bottom:1px solid #a2a9b1;
  padding-bottom:4px; }
main h1 { font-size:1.9em; }
.pagetype { color:#54595d; font-size:0.85em;
  margin-top:-8px; }
.infobox { float:right; width:270px;
  background:#f8f9fa; border:1px solid #a2a9b1;
  margin:0 0 16px 20px; padding:10px 12px;
  font-size:0.85em; }
.infobox th { text-align:left;
  vertical-align:top; padding-right:8px;
  color:#54595d; white-space:nowrap; }
.infobox td { word-break:break-word; }
.backlinks { margin-top:32px; padding-top:8px;
  border-top:1px solid #c8ccd1;
  font-size:0.9em; color:#54595d; }
.snippet { color:#54595d; font-size:0.9em; }
.snippet b { background:#ffff66; }
.result { margin-bottom:14px; }
table { border-collapse:collapse; }
td, th { border:1px solid #c8ccd1;
  padding:4px 8px; }
code { background:#f8f9fa;
  border:1px solid #eaecf0; padding:1px 4px; }
a.ext::after { content:"\\2197"; font-size:0.75em;
  vertical-align:super; margin-left:1px; }
"""

app = Flask(__name__)


# --------------------------------------------------------------
def page_index():
    """Map page name -> (section, Path) for all pages."""
    idx = {}
    for sec, rel in SECTION_DIRS.items():
        folder = WIKI_ROOT / rel
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("*.md")):
            idx[p.stem] = (sec, p)
    return idx


# --------------------------------------------------------------
def split_frontmatter(text):
    """Return (meta dict, body) for a markdown file."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            if isinstance(meta, dict):
                return meta, parts[2]
    return {}, text


# --------------------------------------------------------------
def wikify(text, idx):
    """Convert [[wiki links]] to HTML anchors."""

    # --------------------------------------
    def repl(m):
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        base = target.split("/")[-1]
        safe = html.escape(label)
        if base in idx:
            url = "/wiki/" + quote(base)
            return f'<a href="{url}">{safe}</a>'
        return f'<span class="missing">{safe}</span>'

    return LINK_RX.sub(repl, text)


# --------------------------------------------------------------
def raw_count():
    """Count captures; Raw/ may not be populated yet."""
    if not RAW_DIR.is_dir():
        return 0
    return len([
        p for p in RAW_DIR.rglob("*.md")
        if p.name != "sources.md"
    ])


# --------------------------------------------------------------
def nav_items(idx):
    """Pinned sidebar entries: home page, then key pages."""
    items = [
        '<li class="home"><a href="/">'
        f"{html.escape(HOME_PAGE)}</a></li>"
    ]
    for name in NAV_PAGES:
        if name not in idx:
            continue
        url = "/wiki/" + quote(name)
        items.append(
            f'<li><a href="{url}">'
            f"{html.escape(name)}</a></li>"
        )
    items.append("<hr>")
    return items


# --------------------------------------------------------------
def sidebar_html(idx):
    """Build the navigation sidebar."""
    counts = {}
    for sec, _ in idx.values():
        counts[sec] = counts.get(sec, 0) + 1
    items = nav_items(idx)
    for sec in SECTION_DIRS:
        n = counts.get(sec, 0)
        url = "/section/" + quote(sec)
        items.append(
            f'<li><a href="{url}">{sec}</a>'
            f" ({n})</li>"
        )
    n_raw = raw_count()
    if n_raw:
        items.append(
            f'<li><a href="/raw/">Raw captures</a>'
            f" ({n_raw})</li>"
        )
    return (
        "<nav><h3>Navigation</h3><ul>"
        + "".join(items)
        + "</ul></nav>"
    )


# --------------------------------------------------------------
def page_html(title, body, idx, q=""):
    """Wrap content in the site HTML shell."""
    safe_q = html.escape(q, quote=True)
    top = (
        '<div id="topbar">'
        '<h1><a href="/">Infra Context-Wiki</a></h1>'
        '<form action="/search" method="get">'
        f'<input type="text" name="q" value="{safe_q}"'
        ' placeholder="Search the wiki...">'
        "</form></div>"
    )
    return (
        "<!doctype html><html><head>"
        '<meta charset="utf-8">'
        f"<title>{html.escape(title)}</title>"
        f"<style>{CSS}</style></head><body>"
        + top
        + '<div class="layout">'
        + sidebar_html(idx)
        + f"<main>{body}</main>"
        + "</div></body></html>"
    )


# --------------------------------------------------------------
def raw_link(value):
    """Turn a Raw/... frontmatter path into a link."""
    rel = value.split("Raw/", 1)[-1]
    if not (RAW_DIR / rel).is_file():
        return value
    return f'<a href="/raw/{quote(rel)}">{value}</a>'


# --------------------------------------------------------------
def resolve_raw(rel):
    """Resolve a Raw/ path, refusing to escape the dir."""
    target = (RAW_DIR / rel).resolve()
    if not target.is_relative_to(RAW_DIR.resolve()):
        return None
    if target.suffix != ".md" or not target.is_file():
        return None
    return target


# --------------------------------------------------------------
def ext_link(url, label):
    """Off-site link: new tab, and no window.opener."""
    return (
        f'<a class="ext" href="{html.escape(url, True)}"'
        ' target="_blank" rel="noopener noreferrer">'
        f"{html.escape(label)}</a>"
    )


# --------------------------------------------------------------
def wikipedia_link(url):
    """Link to an article, labelled with its title."""
    slug = url.rsplit("/", 1)[-1]
    return ext_link(url, unquote(slug).replace("_", " "))


# --------------------------------------------------------------
def website_link(url):
    """Link to a project's own site, labelled by host."""
    label = re.sub(r"^https?://(www\.)?", "", url)
    return ext_link(url, label.rstrip("/"))


# --------------------------------------------------------------
def infobox_value(key, val):
    """Render one infobox value according to its key."""
    if isinstance(val, list):
        val = ", ".join(str(v) for v in val)
    val = str(val)
    if key == "wikipedia":
        return wikipedia_link(val)
    if key == "website":
        return website_link(val)
    safe = html.escape(val)
    if key == "resource":
        return f'<a href="{safe}">source&nbsp;link</a>'
    if key == "source_file":
        return raw_link(safe)
    return safe


# --------------------------------------------------------------
def infobox_html(meta):
    """Render OKF frontmatter as a floating infobox."""
    rows = []
    for key in ("type", "description", "wikipedia",
                "website", "resource", "source_file",
                "tags"):
        val = meta.get(key)
        if not val:
            continue
        rows.append(
            f"<tr><th>{key}</th>"
            f"<td>{infobox_value(key, val)}</td></tr>"
        )
    if not rows:
        return ""
    return (
        '<table class="infobox">'
        + "".join(rows)
        + "</table>"
    )


# --------------------------------------------------------------
def backlinks_html(name, idx):
    """List pages that link to the given page."""
    hits = []
    for other, (_, path) in sorted(idx.items()):
        if other == name:
            continue
        text = path.read_text(encoding="utf-8")
        if (f"[[{name}]]" in text
                or f"[[{name}|" in text):
            url = "/wiki/" + quote(other)
            hits.append(
                f'<a href="{url}">'
                f"{html.escape(other)}</a>"
            )
    if not hits:
        return ""
    return (
        '<div class="backlinks">'
        "<b>What links here:</b> "
        + " &middot; ".join(hits)
        + "</div>"
    )


# --------------------------------------------------------------
def make_snippet(text, pos, qlen):
    """Return an HTML snippet around a match position."""
    start = max(0, pos - 80)
    end = min(len(text), pos + qlen + 80)
    before = html.escape(text[start:pos])
    match = html.escape(text[pos:pos + qlen])
    after = html.escape(text[pos + qlen:end])
    return f"...{before}<b>{match}</b>{after}..."


# --------------------------------------------------------------
@app.route("/")
def home():
    """Main page: the Stacks ladder."""
    idx = page_index()
    if HOME_PAGE in idx:
        _, path = idx[HOME_PAGE]
        text = path.read_text(encoding="utf-8")
        _, body = split_frontmatter(text)
        content = md.markdown(
            wikify(body, idx), extensions=MD_EXTS
        )
    else:
        content = (f"<h1>{html.escape(HOME_PAGE)} page"
                   " not found</h1>")
    return page_html(HOME_PAGE, content, idx)


# --------------------------------------------------------------
@app.route("/wiki/<name>")
def wiki_page(name):
    """Render one wiki page by its name."""
    idx = page_index()
    if name not in idx:
        abort(404)
    sec, path = idx[name]
    meta, body = split_frontmatter(
        path.read_text(encoding="utf-8")
    )
    content = md.markdown(
        wikify(body, idx), extensions=MD_EXTS
    )
    ptype = html.escape(str(meta.get("type", sec)))
    article = (
        f"<h1>{html.escape(name)}</h1>"
        f'<div class="pagetype">{ptype}'
        f" &middot; {sec}</div>"
        + infobox_html(meta)
        + content
        + '<div style="clear:both"></div>'
        + backlinks_html(name, idx)
    )
    return page_html(name, article, idx)


# --------------------------------------------------------------
@app.route("/section/<sec>")
def section_page(sec):
    """List all pages in one section."""
    idx = page_index()
    if sec not in SECTION_DIRS:
        abort(404)
    items = []
    for name, (s, path) in sorted(idx.items()):
        if s != sec:
            continue
        meta, _ = split_frontmatter(
            path.read_text(encoding="utf-8")
        )
        desc = html.escape(
            str(meta.get("description", ""))
        )
        url = "/wiki/" + quote(name)
        items.append(
            f'<li><a href="{url}">'
            f"{html.escape(name)}</a>"
            f" &mdash; {desc}</li>"
        )
    body = (
        f"<h1>{html.escape(sec)}</h1>"
        f"<p>{len(items)} pages</p><ul>"
        + "".join(items)
        + "</ul>"
    )
    return page_html(sec, body, idx)


# --------------------------------------------------------------
@app.route("/raw/")
def raw_index():
    """Browse the immutable captures, by category."""
    idx = page_index()
    out = ["<h1>Raw source captures</h1>",
           "<p>Immutable downloads. Never edited; the "
           "wiki pages above are derived from these.</p>"]
    if not raw_count():
        out.append("<p>Not downloaded yet. Run "
                   "<code>python raw_download.py</code> "
                   "to fetch them.</p>")
    folders = sorted(p for p in RAW_DIR.iterdir()
                     if p.is_dir()) if RAW_DIR.is_dir() \
        else []
    for folder in folders:
        files = sorted(folder.glob("*.md"))
        out.append(f"<h2>{html.escape(folder.name)} "
                   f"({len(files)})</h2><ul>")
        for f in files:
            rel = f"{folder.name}/{f.name}"
            out.append(
                f'<li><a href="/raw/{quote(rel)}">'
                f"{html.escape(f.stem)}</a></li>"
            )
        out.append("</ul>")
    return page_html("Raw captures", "".join(out), idx)


# --------------------------------------------------------------
@app.route("/raw/<path:rel>")
def raw_page(rel):
    """Render one immutable capture, read-only."""
    idx = page_index()
    target = resolve_raw(rel)
    if target is None:
        abort(404)
    text = target.read_text(encoding="utf-8")
    text = re.sub(r"^<!--.*?-->", "", text,
                  count=1, flags=re.S)
    body = md.markdown(text, extensions=MD_EXTS)
    return page_html(
        target.stem, raw_banner(target, idx) + body, idx
    )


# --------------------------------------------------------------
def raw_banner(target, idx):
    """Header shown above an immutable capture."""
    name = target.stem
    back = ""
    if name in idx:
        back = (f' &middot; wiki page: '
                f'<a href="/wiki/{quote(name)}">'
                f"{html.escape(name)}</a>")
    return (
        '<div class="pagetype">Raw capture &middot; '
        f"{html.escape(target.parent.name)}{back}</div>"
        '<p class="backlinks" style="margin-top:8px">'
        "Immutable source capture &mdash; not edited. "
        'See <a href="/raw/">all captures</a>.</p>'
    )


# --------------------------------------------------------------
@app.route("/search")
def search():
    """Full-text search across all wiki pages."""
    idx = page_index()
    q = request.args.get("q", "").strip()
    if not q:
        return page_html(
            "Search", "<h1>Search</h1>"
            "<p>Type a query above.</p>", idx
        )
    results = []
    for name, (sec, path) in idx.items():
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        count = low.count(q.lower())
        in_title = q.lower() in name.lower()
        if not count and not in_title:
            continue
        pos = max(low.find(q.lower()), 0)
        snip = make_snippet(text, pos, len(q))
        score = (100 if in_title else 0) + count
        results.append((score, name, sec, snip))
    results.sort(key=lambda r: (-r[0], r[1]))
    return page_html(
        f"Search: {q}",
        search_results_html(q, results), idx, q
    )


# --------------------------------------------------------------
def search_results_html(q, results):
    """Render the search results list."""
    safe_q = html.escape(q)
    out = [
        f"<h1>Search results for "
        f"&ldquo;{safe_q}&rdquo;</h1>",
        f"<p>{len(results)} pages found</p>",
    ]
    for _, name, sec, snip in results:
        url = "/wiki/" + quote(name)
        out.append(
            f'<div class="result">'
            f'<a href="{url}">'
            f"<b>{html.escape(name)}</b></a>"
            f" <small>({sec})</small><br>"
            f'<span class="snippet">{snip}</span>'
            "</div>"
        )
    return "".join(out)


# --------------------------------------------------------------
@app.errorhandler(404)
def not_found(_err):
    """Friendly 404 page."""
    idx = page_index()
    return page_html(
        "Page not found",
        "<h1>Page not found</h1>"
        '<p>Try the <a href="/">Stacks</a> ladder, the '
        '<a href="/wiki/Index">Index</a>, or the search '
        "box above.</p>", idx
    ), 404


# --------------------------------------------------------------
if __name__ == "__main__":
    print(f"Serving wiki: {WIKI_ROOT}")
    print(f"Open: http://localhost:{PORT}")
    app.run(host="127.0.0.1", port=PORT)
