# Wiki Server (local browsing UI)

`wiki_server.py` serves a context wiki as a local,
human-readable website in the style of Wikipedia —
navigable wiki links, search, infoboxes, and
backlinks. Read-only: it never modifies wiki files.

## Running

Recommended — the control scripts (background run,
PID file `.wiki_server.pid`, log `wiki_server.log`):

```bash
./server_start.sh     # start on port 8020 (restarts
                      #   if it is already in use)
./server_stop.sh      # stop (PID file, then any
                      #   process on the port)
./server_restart.sh   # stop + start
```

Or run in the foreground:

```bash
python wiki_server.py
# open http://localhost:8020
```

(`server_start.sh` uses whatever `python` is on your
PATH; override with `PYTHON=/path/to/python
./server_start.sh` if you keep the dependencies in a
particular virtualenv.)

If port 8020 is already in use, `server_start.sh` stops
whatever is holding it (by calling `server_stop.sh`) and
starts a fresh server — so starting twice restarts
rather than failing, and `server_restart.sh` is now just
the explicit spelling of the same thing. If the port is
*still* occupied after that — something not yours, which
`kill` cannot touch — it reports the port and exits 1
instead of launching a server that cannot bind.

`server_stop.sh` stops the recorded PID, then any stray
process left listening on the port.

Serve a different wiki:

```bash
WIKI_ROOT=/path/to/wiki python wiki_server.py
```

Requires `flask`, `markdown`, `pyyaml`.
Port: **8020** (constant `PORT` in the script).

## Features

| Feature | Details |
|---------|---------|
| Main page | Renders `Dashboards/Stacks.md` — the ladder of example stacks (constant `HOME_PAGE`) |
| Pinned nav | `Stacks` (top, bold), then `Development Setup` and `Index` above the section list (constant `NAV_PAGES`) |
| Wiki links | `[[Name]]` and `[[Name\|alias]]` become links; links to missing pages show in red |
| Sections | Sidebar navigation to Concepts, Entities, Summaries, Dashboards with page counts |
| Infobox | OKF frontmatter (type, description, wikipedia, website, resource, source_file, tags) rendered as a floating box; `resource` becomes a clickable source link and `source_file` links to the capture in `Raw/` |
| Outside links | Every Concept and Entity page links out: to its English Wikipedia article (labelled with the article title), or — where Wikipedia has no article — to the project's own site (labelled with the host). Both open in a new tab (`target="_blank"`, `rel="noopener noreferrer"`, ↗ marker) — see [d8_wikipedia_links.md](d8_wikipedia_links.md) |
| Raw captures | The immutable downloads in `Raw/` are browsable and readable, so every derived page can be traced to its source in one click |
| Backlinks | "What links here" at the bottom of every page |
| Search | Full-text, case-insensitive, ranked (title matches first, then hit count), with highlighted snippets |
| Live | Pages are re-read per request — edits to the wiki show up on refresh, no restart needed |

## URLs

| URL | Content |
|-----|---------|
| `/` | Main page — the `Stacks` ladder |
| `/wiki/Index` | The generated index of every page |
| `/wiki/<Page Name>` | One page |
| `/section/<Section>` | Section listing |
| `/raw/` | All immutable captures, grouped by category |
| `/raw/<category>/<file>.md` | One capture, read-only |
| `/search?q=...` | Search results |

### Following the trail

The three wiki layers are designed to be traceable, and
the server makes that a click each way:

```text
Concept / Entity page   e.g. /wiki/Automatic HTTPS
  -> ## Sources         [[caddy-automatic-https]]
Summary page            /wiki/caddy-automatic-https
  -> infobox source_file
Raw capture             /raw/03_deployments/caddy-automatic-https.md
  -> provenance header  original URL and retrieval date
```

Raw captures are served read-only. Paths are resolved
and checked against the `Raw/` directory, so `..`
traversal returns 404; only `.md` files inside `Raw/`
are readable.

Search covers the wiki pages, not the raw captures —
the captures are the source corpus (~615,000 words),
and each one already has a searchable summary page that
carries its lead text and heading outline.

## See also

- [d4_wiki_tools.md](d4_wiki_tools.md) — programmatic
  find / grep access to the same wiki.
- [d3_howto_context_wiki.md](d3_howto_context_wiki.md)
  — the wiki structure being served.
