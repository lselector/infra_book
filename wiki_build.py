#!/usr/bin/env python3
"""Build wiki layers from the Raw/ source captures.

Implements Steps 3-5 of the pipeline in
d3_howto_context_wiki.md for the Context-Wiki-Infra
vault:

  summaries  Raw/*.md            -> Wiki/Summaries/
  crosslink  add [[Related]] links to the summaries,
             based on the Concept / Entity pages that
             exist at the time it runs
  index      regenerate Dashboards/Index.md from the
             frontmatter of every wiki page

Summaries are *extractive*: lead paragraphs plus the
source document's own heading outline. Nothing is
paraphrased, so every statement stays traceable to the
immutable capture in Raw/. The interpreted knowledge
lives in the hand-written Concept and Entity pages.

Usage:
    python wiki_build.py summaries
    python wiki_build.py crosslink
    python wiki_build.py index
    python wiki_build.py all

Created: 2026-07-27
Last updated: 2026-07-27
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
VAULT = HERE / "Context-Wiki-Infra"
RAW = VAULT / "Raw"
SUMMARIES = VAULT / "Wiki" / "Summaries"
CONCEPTS = VAULT / "Wiki" / "Concepts"
ENTITIES = VAULT / "Wiki" / "Entities"
INDEX = VAULT / "Dashboards" / "Index.md"

LEAD_LINES = 4
LEAD_CHARS = 300
MAX_HEADINGS = 18
REL_MARK = "## Related pages"

CATEGORY_TAGS = {
    "01_foundations": "foundations",
    "02_architectures": "architectures",
    "03_deployments": "deployments",
    "04_network_storage_db": "storage-and-databases",
    "05_ops_cicd_security": "ops-and-security",
    "06_product_patterns": "product-patterns",
    "07_playbooks": "playbooks",
    "08_scaling_maturity": "scaling",
    "09_appendices": "reference",
}

# Page names too short or too common to auto-link
# safely when scanning summary text. "Express" also
# collides with "S3 Express One Zone" and "SQL Server
# Express"; "React" with the verb, as in "react to".
LINK_STOPLIST = {"Caching", "Firewall", "Monitoring",
                 "Bash", "GitHub", "Express", "React",
                 "just", "Invoke"}


# --------------------------------------------------------------
def raw_files():
    """Return every immutable capture under Raw/."""
    return sorted(
        p for p in RAW.rglob("*.md")
        if p.name != "sources.md"
    )


# --------------------------------------------------------------
def parse_capture(path):
    """Split a Raw capture into its header and body."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    for key in ("title", "source", "retrieved"):
        m = re.search(rf"^{key}: (.+)$", text, re.M)
        if m:
            meta[key] = m.group(1).strip()
    parts = text.split("\n---\n", 1)
    body = parts[1] if len(parts) > 1 else text
    return meta, body.strip()


# --------------------------------------------------------------
def quote_safe(text):
    """Neutralise [[...]] so quoted source text is inert."""
    # Captured pages may contain [[ ]] as their own syntax
    # (fly.toml, for one). Escaping the opening bracket
    # stops the wiki server rendering it as a broken link.
    return text.replace("[[", "&#91;&#91;")


# --------------------------------------------------------------
def lead_paragraphs(body):
    """Take the first few prose lines of a document."""
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "|", ">")):
            continue
        if line.startswith(("*", "-", "```", "<a ")):
            continue
        if len(line) > LEAD_CHARS:
            line = line[:LEAD_CHARS].rsplit(" ", 1)[0] + " ..."
        out.append(quote_safe(line))
        if len(out) >= LEAD_LINES:
            break
    return out


# --------------------------------------------------------------
def outline(body):
    """List the source document's own headings."""
    heads = []
    for line in body.splitlines():
        m = re.match(r"^(#{1,3}) +(.+?)\s*$", line)
        if not m:
            continue
        text = re.sub(r"\[(.+?)\]\(.*?\)", r"\1",
                      m.group(2))
        text = text.replace("`", "").strip()
        if not text or len(text) > 90:
            continue
        heads.append((len(m.group(1)), quote_safe(text)))
        if len(heads) >= MAX_HEADINGS:
            break
    return heads


# --------------------------------------------------------------
def one_sentence(lines, limit=190):
    """Build a short description from lead lines."""
    text = " ".join(lines).strip()
    text = re.sub(r"\[(.+?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text)
    m = re.match(r"^(.{40,%d}?[.!?])\s" % limit, text)
    out = m.group(1) if m else text[:limit]
    return out.replace('"', "'").strip()


# --------------------------------------------------------------
def yaml_line(key, value):
    """Emit one always-quoted YAML scalar."""
    # Backslashes start an escape sequence inside a
    # double-quoted YAML scalar, and a literal --- ends
    # the frontmatter block for any naive splitter.
    # Captured source text contains both.
    safe = str(value).replace("\\", " ")
    safe = safe.replace('"', "'")
    safe = re.sub(r"-{2,}", "-", safe)
    return f'{key}: "{" ".join(safe.split())}"'


# --------------------------------------------------------------
def summary_header(path, meta, desc):
    """Build the OKF frontmatter for a summary page."""
    cat = path.parent.name
    rel = f"Raw/{cat}/{path.name}"
    tags = [CATEGORY_TAGS.get(cat, cat), "summary"]
    return "\n".join([
        "---",
        "type: Summary",
        yaml_line("title", meta.get("title", path.stem)),
        yaml_line("description", desc),
        yaml_line("resource", meta.get("source", "")),
        yaml_line("source_file", rel),
        "tags: [" + ", ".join(tags) + "]",
        yaml_line("timestamp",
                  meta.get("retrieved", "") + "T00:00:00Z"),
        "---",
        "",
        "",
    ])


# --------------------------------------------------------------
def summary_body(path, meta, lead, heads):
    """Build the readable body of a summary page."""
    cat = path.parent.name
    out = [f"# {meta.get('title', path.stem)}", ""]
    out += [
        "Extractive digest of the immutable capture in",
        f"`Raw/{cat}/{path.name}`",
        f"(retrieved {meta.get('retrieved', 'n/a')}).",
        "Lead text and headings are quoted verbatim from",
        "the source; read the capture for the full text.",
        "",
        f"Source: <{meta.get('source', '')}>",
        "",
    ]
    if lead:
        out += ["## Opening", ""]
        out += [f"> {ln}" for ln in lead] + [""]
    if heads:
        out += ["## Contents of the source document", ""]
        for depth, text in heads:
            out.append("  " * (depth - 1) + f"- {text}")
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------
def build_summaries():
    """Generate one summary page per Raw capture."""
    SUMMARIES.mkdir(parents=True, exist_ok=True)
    made = 0
    for path in raw_files():
        meta, body = parse_capture(path)
        lead = lead_paragraphs(body)
        desc = one_sentence(lead) or meta.get("title", "")
        page = (summary_header(path, meta, desc)
                + summary_body(path, meta, lead,
                               outline(body)))
        dest = SUMMARIES / path.name
        dest.write_text(page, encoding="utf-8")
        made += 1
    print(f"summaries written: {made}")
    return made


# --------------------------------------------------------------
def page_names():
    """Return Concept and Entity page names."""
    names = set()
    for folder in (CONCEPTS, ENTITIES):
        if folder.is_dir():
            names |= {p.stem for p in folder.glob("*.md")}
    return sorted(names - LINK_STOPLIST)


# --------------------------------------------------------------
def matches(name, haystack):
    """True when a page name occurs as a whole phrase."""
    if len(name) < 4:
        return False
    rx = re.compile(
        r"(?<![\w-])" + re.escape(name) + r"(?![\w-])",
        re.IGNORECASE,
    )
    return bool(rx.search(haystack))


# --------------------------------------------------------------
def related_for(raw_path, names, limit=12):
    """Pick page names that occur in a Raw capture."""
    text = raw_path.read_text(encoding="utf-8")
    hits = [n for n in names if matches(n, text)]
    hits.sort(key=lambda n: (-len(n), n))
    return sorted(hits[:limit])


# --------------------------------------------------------------
def strip_related(text):
    """Remove a previously generated Related section."""
    return text.split(REL_MARK)[0].rstrip() + "\n"


# --------------------------------------------------------------
def crosslink():
    """Append [[Related pages]] links to each summary."""
    names = page_names()
    if not names:
        print("no Concept/Entity pages yet - skipping")
        return 0
    by_name = {p.name: p for p in raw_files()}
    linked = 0
    for page in sorted(SUMMARIES.glob("*.md")):
        raw = by_name.get(page.name)
        if raw is None:
            continue
        rel = related_for(raw, names)
        text = strip_related(
            page.read_text(encoding="utf-8")
        )
        if rel:
            links = " · ".join(f"[[{n}]]" for n in rel)
            text += f"\n{REL_MARK}\n\n{links}\n"
            linked += 1
        page.write_text(text, encoding="utf-8")
    print(f"summaries cross-linked: {linked}"
          f" (against {len(names)} pages)")
    return linked


# --------------------------------------------------------------
def read_meta(path):
    """Read title and description from frontmatter."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    for key in ("title", "description", "type"):
        m = re.search(rf'^{key}: "?(.*?)"?\s*$',
                      text, re.M)
        if m:
            meta[key] = m.group(1).strip()
    meta.setdefault("title", path.stem)
    return meta


# --------------------------------------------------------------
def index_section(heading, folder, note):
    """Render one section of Dashboards/Index.md."""
    pages = sorted(folder.glob("*.md")) if folder.is_dir() \
        else []
    out = [f"## {heading} ({len(pages)})", "", note, ""]
    for p in pages:
        meta = read_meta(p)
        desc = meta.get("description", "")
        line = f"- [[{p.stem}]]"
        if desc:
            line += f" — {desc}"
        out.append(line)
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------
def build_index():
    """Regenerate Dashboards/Index.md from the pages."""
    parts = [
        "# Cloud Infrastructure Context-Wiki — Index",
        "",
        "Structural anchor for browsing: every page in",
        "the wiki, grouped by layer. Generated by",
        "`wiki_build.py index` — do not hand-edit.",
        "",
        "Start with [[Stacks]] for the ten-rung ladder of",
        "example stacks — it is also the site's front",
        "page. [[Development Setup]] covers the tools on",
        "your own machine first; [[Topics]] is the keyword",
        "plan.",
        "",
        index_section(
            "Concepts", CONCEPTS,
            "Ideas, patterns and practices — the "
            "\"what and why\" layer."),
        index_section(
            "Entities", ENTITIES,
            "Concrete products, services and tools — the "
            "\"which one\" layer."),
        index_section(
            "Summaries", SUMMARIES,
            "One extractive digest per immutable capture "
            "in `Raw/`."),
    ]
    INDEX.write_text("\n".join(parts), encoding="utf-8")
    print(f"index written: {INDEX}")


# --------------------------------------------------------------
def main():
    """Run one build step, or all of them in order."""
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("summaries", "all"):
        build_summaries()
    if cmd in ("crosslink", "all"):
        crosslink()
    if cmd in ("index", "all"):
        build_index()
    if cmd not in ("summaries", "crosslink",
                   "index", "all"):
        print("usage: wiki_build.py "
              "summaries|crosslink|index|all")


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
