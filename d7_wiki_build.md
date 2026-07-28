# Building the Wiki from `Raw/`

`wiki_build.py` implements Steps 3-5 of the pipeline in
[d3_howto_context_wiki.md](d3_howto_context_wiki.md),
turning the immutable captures in `Raw/` into the
navigable OKF wiki under `Context-Wiki-Infra/Wiki/`.

```text
1. Topics & keywords   -->  Dashboards/Topics.md
2. Download            -->  Raw/                 (d6_raw_download.md)
3. Convert to Markdown -->  Wiki/Summaries/      <-- this script
4. Create OKF files    -->  Wiki/Concepts/, Wiki/Entities/
5. Index and log       -->  Dashboards/
```

## The three layers

The wiki deliberately separates **what a source said**
from **what we concluded**, because the two age
differently and carry different authority.

| Layer | Count | Written by | Contains |
|---|---|---|---|
| `Wiki/Summaries/` | one per capture | generated | extractive digest of one `Raw/` file |
| `Wiki/Concepts/` | one per idea | by hand | patterns, practices, trade-offs |
| `Wiki/Entities/` | one per thing | by hand | products, services, tools |

**Summaries are extractive, not interpretive.** They
carry the source's own lead paragraphs and heading
outline, quoted verbatim, plus a link to the capture.
Nothing is paraphrased, so a summary cannot drift from
its source or invent a claim. When you need to know what
a vendor actually says, the summary points at the file
that says it.

**Concepts and Entities are the interpreted layer.**
They are written by hand, state opinions ("use the
managed KMS; a dedicated HSM is for contracts that name
it"), and cite the summaries they rest on. That is where
the judgement lives, and it is clearly marked as such.

## Usage

```bash
python wiki_build.py summaries   # Raw/ -> Wiki/Summaries/
python wiki_build.py crosslink   # add [[Related]] to summaries
python wiki_build.py index       # regenerate Dashboards/Index.md
python wiki_build.py all         # all three, in order
```

Run order matters: `crosslink` links summaries against
whatever Concept and Entity pages exist *at the time it
runs*, so re-run it after adding pages by hand.

## Naming and linking conventions

The wiki server keys every page on its **filename stem**,
so links and filenames must agree exactly:

- Concepts and Entities use **Title Case with spaces** —
  `Envelope Encryption.md`, linked as
  `[[Envelope Encryption]]`.
- Summaries keep the **kebab-case stem of the capture** —
  `aws-kms-concepts.md`, linked as `[[aws-kms-concepts]]`.
  This also guarantees the two namespaces never collide.
- **No slashes in a page name.** A `/` breaks both the
  file path and the server's link parser, which resolves
  `[[a/b]]` to `b`. This is why the CI/CD page is called
  `Continuous Integration and Delivery`.
- **Never wrap a `[[link]]` across lines.** The parser
  matches across newlines and will produce a page name
  containing one.

## Frontmatter

Every non-reserved page carries OKF frontmatter. The
server renders `type`, `description`, `wikipedia`,
`website`, `resource`, `source_file` and `tags` as the
page infobox, so those are the fields worth filling in:

```yaml
---
type: Concept
title: "Envelope Encryption"
description: "Encrypt data with a data key, encrypt the data key with a KMS key."
wikipedia: "https://en.wikipedia.org/wiki/Key_wrap"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---
```

`wikipedia` and `website` are written by
`wikipedia_links.py` from a curated map rather than by
hand — see
[d8_wikipedia_links.md](d8_wikipedia_links.md).

`Dashboards/Index.md` and `Dashboards/Log.md` are OKF
reserved filenames and correctly have no frontmatter.

### Two escaping rules the generator enforces

Both were found by feeding real captured text through the
pipeline:

1. **No backslashes or `---` in a frontmatter value.** A
   backslash begins an escape sequence in a double-quoted
   YAML scalar; a literal `---` terminates the
   frontmatter block for any naive splitter, including
   the one in `wiki_server.py`. Captured Markdown
   contains both constantly.
2. **Escape `[[` in quoted source text** as `&#91;&#91;`.
   Some captures use `[[...]]` as their own syntax —
   `fly.toml` service blocks, for one — and would
   otherwise render as broken wiki links.

## Verifying the result

Three checks worth running after a build:

```bash
# 1. every page parses the way the server parses it
python3 -c "
import pathlib, sys; sys.path.insert(0, '.')
from wiki_server import split_frontmatter
for f in pathlib.Path('Context-Wiki-Infra').rglob('*.md'):
    if 'Raw' in f.parts: continue
    meta, body = split_frontmatter(f.read_text(encoding='utf-8'))
    if f.name.lower() not in ('index.md','log.md','claude.md') \\
       and not meta.get('type'):
        print('no type:', f)
"

# 2. no dangling [[links]]
python3 -c "
import pathlib, re, collections
V = pathlib.Path('Context-Wiki-Infra')
dirs = ['Wiki/Concepts','Wiki/Entities','Wiki/Summaries','Dashboards']
idx = {f.stem for d in dirs for f in (V/d).glob('*.md')}
rx = re.compile(r'\\[\\[([^\\]|\\n]+)(?:\\|[^\\]\\n]+)?\\]\\]')
bad = collections.Counter()
for d in dirs:
    for f in (V/d).glob('*.md'):
        for m in rx.findall(f.read_text(encoding='utf-8')):
            if m.strip().split('/')[-1] not in idx: bad[m.strip()] += 1
print('dangling:', dict(bad) or 'none')
"

# 3. it renders
./server_restart.sh && open http://localhost:8020
```

A dangling link is not fatal — OKF tolerates broken links
and the server renders them as greyed-out text — but it
usually means a page you meant to write, or a typo.

## Adding material later

1. Add the source to `raw_sources.json` and run
   `python raw_download.py` (see
   [d6_raw_download.md](d6_raw_download.md)). A whole new
   `Raw/` category also needs a line in `CATEGORY_TITLES`
   there and one in `CATEGORY_TAGS` here, which sets the
   tag every summary in that folder carries.
2. `python wiki_build.py summaries` — the new capture
   gets a summary.
3. Write or extend the Concept and Entity pages by hand,
   citing the new summary, and add `[[links]]` **both
   ways** — this is the Ripple Update Routine in
   `Context-Wiki-Infra/claude.md`.
4. `python wiki_build.py crosslink index`.
5. Add a dated entry to `Dashboards/Log.md` and commit.

## See also

* [d1_okf.md](d1_okf.md) — the Open Knowledge Format.
* [d2_docs2okf.md](d2_docs2okf.md) — converting one
  document into an OKF concept file.
* [d3_howto_context_wiki.md](d3_howto_context_wiki.md) —
  the full pipeline.
* [d6_raw_download.md](d6_raw_download.md) — Step 2.
* [d5_wiki_server.md](d5_wiki_server.md) — browsing the
  result on port 8020.

---

Created: 2026-07-27
Last updated: 2026-07-28
