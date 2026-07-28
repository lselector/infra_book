# Downloading Sources into `Raw/`

`raw_download.py` implements Step 2 of the context-wiki
build pipeline described in
[d3_howto_context_wiki.md](d3_howto_context_wiki.md):

```text
1. Define topics & keywords   -->  Dashboards/Topics.md
2. Download content           -->  Raw/            <-- this script
3. Convert content to .md     -->  Wiki/Summaries/
4. Create OKF files           -->  Wiki/Concepts/, Wiki/Entities/
```

It fetches a curated list of source documents, converts
them to clean Markdown, files them under
`Context-Wiki-Infra/Raw/<category>/`, and regenerates the
source registry `Raw/sources.md`.

## The source list

All sources live in [raw_sources.json](raw_sources.json) —
a flat array of objects, one per document:

```json
{
  "cat":   "03_deployments",
  "file":  "caddy-automatic-https.md",
  "title": "Caddy — automatic HTTPS (certificate issuance and renewal)",
  "url":   "https://caddyserver.com/docs/automatic-https"
}
```

* `cat` — one of the ten `Raw/` category folders, which
  mirror the Parts of [myprompts/TOC_infra.md](myprompts/TOC_infra.md),
  plus `12_ai_in_saas` for the AI-assistant material
  added later. A new folder needs an entry in
  `CATEGORY_TITLES` here and in `CATEGORY_TAGS` in
  `wiki_build.py`.
* `file` — the destination filename inside that folder.
* `title` — human-readable title, used in the provenance
  header and in `Raw/sources.md`.
* `url` — the source URL, later reused as the OKF
  `resource` field.

To add material, append an entry and re-run the script.

## Usage

```bash
python raw_download.py            # fetch everything missing
python raw_download.py --force    # re-fetch every source
python raw_download.py --only caddy   # filter by substring
python raw_download.py --registry     # rebuild sources.md only
```

`--only` matches against the filename, the category, and
the URL, so `--only 03_deployments`, `--only caddy`, and
`--only cloudflare.com` all work.

Downloads run eight at a time. Sources already on disk
are skipped unless `--force` is given, so the script is
cheap to re-run after fixing a handful of dead URLs.

## What a downloaded file looks like

Every file gets an HTML-comment provenance header, so a
capture is self-describing even if it is moved:

```markdown
<!--
title: Caddy — automatic HTTPS (certificate issuance and renewal)
source: https://caddyserver.com/docs/automatic-https
retrieved: 2026-07-27
category: 03_deployments
note: immutable source capture - do not edit
-->

# Caddy — automatic HTTPS (certificate issuance and renewal)

Source: <https://caddyserver.com/docs/automatic-https>

---

...page content as Markdown...
```

Per the Source Immutability rule in
[Context-Wiki-Infra/claude.md](Context-Wiki-Infra/claude.md),
these files are never edited by hand. To refresh one,
re-download it.

## How the conversion works

1. **Fetch** with a browser `User-Agent` and three
   retries.
2. **Pass through** responses that are already Markdown
   or plain text (for example the `index.md` variants
   that the Cloudflare docs site serves).
3. **Absolutize** every `href` and `src` against the page
   URL, so links still resolve once the page is a local
   file.
4. **Pick the main container** — the first of `main`,
   `article`, `[role=main]`, `#content`, `.markdown-body`
   and friends that holds more than 400 characters of
   text, falling back to `<body>`.
5. **Strip chrome** *inside* that container: scripts,
   styles, nav, header, footer, aside, sidebars,
   breadcrumbs, cookie banners.
6. **Convert** to Markdown with `html2text`
   (`body_width = 0`, images dropped), then collapse
   runs of blank lines.

Step 4 deliberately precedes step 5. Some doc sites ship
malformed HTML in which an unclosed `<nav>` swallows the
rest of the document — stripping first would delete the
whole page. If the stripped result is under 500
characters the script retries the conversion unstripped.

A capture shorter than 500 characters is reported as a
failure rather than saved, which catches JavaScript-only
pages that return an empty shell to `curl`.

## Registry and gaps

After each run the script rewrites `Raw/sources.md`:

* the per-category listing is generated from
  `raw_sources.json`, limited to files that actually
  exist on disk;
* everything from the `## Local reference
  implementations` heading onward is preserved verbatim,
  so the handwritten notes about local projects and the
  **Known gaps** section survive regeneration.

Record any source that could not be captured — and what
was used instead — under **Known gaps**. Bot-blocked
vendor help centres and client-rendered documentation
sites are the two usual causes.

## Watching out for navigation-only captures

Section landing pages (`.../pages/functions/`,
`.../wrangler/commands/`) often convert into a few
hundred words of pure link list. To find them:

```bash
cd Context-Wiki-Infra/Raw
python3 -c "
import pathlib
for p in sorted(pathlib.Path('.').rglob('*.md')):
    if p.name == 'sources.md': continue
    w = len('\n'.join(p.read_text().splitlines()[12:]).split())
    if w < 300: print(f'{w:5d}w  {p}')
"
```

Replace anything that is genuinely a table of contents
with the concrete page beneath it, and delete the
superseded capture so the registry stays accurate.

## See also

* [d3_howto_context_wiki.md](d3_howto_context_wiki.md) —
  the full four-stage pipeline.
* [d2_docs2okf.md](d2_docs2okf.md) — Step 4: turning
  these captures into OKF concept files.
* [Context-Wiki-Infra/Raw/sources.md](Context-Wiki-Infra/Raw/sources.md)
  — the generated registry.

---

Created: 2026-07-27
Last updated: 2026-07-28
