# context-wiki

Notes on how to create and maintain your own knowledge base wiki (context wiki) based on markdown files in OKF format

## Quick start

```bash
pip install flask markdown pyyaml requests html2text beautifulsoup4

python raw_download.py       # fetch the 307 source documents into Raw/
python wiki_build.py all     # build summaries, cross-link, rebuild the index
python wikipedia_links.py apply   # add the Wikipedia link to each page
./server_start.sh            # browse at http://localhost:8020
```

The first step is needed because `Context-Wiki-Infra/Raw/`
is **not** checked in — it holds verbatim copies of other
people's documentation (AWS, Cloudflare, MDN, OWASP and
others), which are theirs to distribute, not mine. The
source list, the registry and the downloader are all
here, so `python raw_download.py` reproduces the corpus
exactly. Everything else — the 250 hand-written wiki
pages, the 307 summaries, the dashboards — is checked in
and readable without downloading anything.

## Documents

- [d1_okf.md](d1_okf.md) — Open Knowledge Format (OKF):
  definition, frontmatter fields, conventions,
  and short example files.
- [d2_docs2okf.md](d2_docs2okf.md) — tutorial on converting
  an existing document into OKF format.
- [d3_howto_context_wiki.md](d3_howto_context_wiki.md) —
  how to create and maintain your own context wiki: topics →
  raw downloads → Markdown → interlinked OKF files.

- [d4_wiki_tools.md](d4_wiki_tools.md) — Python
  find / grep / read utilities for the wiki, usable
  from Python, the command line, Claude Code, or as
  claude-agent-sdk tools.

- [d5_wiki_server.md](d5_wiki_server.md) — local
  Wikipedia-style browsing UI for the wiki
  (`wiki_server.py`, port 8020): navigation, search,
  infoboxes, backlinks.

- [d6_raw_download.md](d6_raw_download.md) — downloading
  source documents into `Raw/` (Step 2 of the pipeline):
  the source list, HTML→Markdown conversion, provenance
  headers, and the generated source registry.

- [d7_wiki_build.md](d7_wiki_build.md) — building the
  wiki from `Raw/` (Steps 3–5): the three page layers,
  naming and linking conventions, frontmatter rules, and
  the checks to run afterwards.

- [d8_wikipedia_links.md](d8_wikipedia_links.md) — the
  outside link attached to every content page: the
  English Wikipedia article, or the project's own site
  where Wikipedia has none. The curated maps, how targets
  are verified, and why exactly three pages have neither.

## Code

- [wiki_tools.py](wiki_tools.py) — stdlib-only find /
  grep / read module (see d4_wiki_tools.md).
- [wiki_server.py](wiki_server.py) — local wiki web
  server on port 8020 (see d5_wiki_server.md).
- [raw_download.py](raw_download.py) — downloads the
  sources listed in [raw_sources.json](raw_sources.json)
  into `Raw/` and regenerates `Raw/sources.md`
  (see d6_raw_download.md).
- [wiki_build.py](wiki_build.py) — generates
  `Wiki/Summaries/` from `Raw/`, cross-links them, and
  regenerates `Dashboards/Index.md`
  (see d7_wiki_build.md).
- [wikipedia_links.py](wikipedia_links.py) — verifies the
  curated targets in
  [wikipedia_links.json](wikipedia_links.json) — article
  titles against the MediaWiki API, project sites by
  fetching them — and writes the `wikipedia:` and
  `website:` fields into every content page
  (see d8_wikipedia_links.md).
- `server_start.sh` / `server_stop.sh` /
  `server_restart.sh` — control scripts for the wiki
  server.
- [.claude/hooks/allow_local_dev.py](.claude/hooks/allow_local_dev.py)
  — Claude Code `PreToolUse` hook that auto-approves the
  routine loop of this repo (the four build scripts, curl
  against localhost, read-only filters like `head` and
  `grep`) so it runs without a permission prompt.
  Everything else falls through to the normal rules.
  Registered in `.claude/settings.local.json`, which is
  per-machine and gitignored, so copy that `hooks` block
  over after a fresh clone.

## Wikis

- [Context-Wiki-Infra/](Context-Wiki-Infra/) — context
  wiki about cheap and simple cloud infrastructure for
  Web and SaaS, structured per d3_howto_context_wiki.md.
  It is the default wiki root for `wiki_tools.py` and
  `wiki_server.py`.

  Topic plan: [Topics.md](Context-Wiki-Infra/Dashboards/Topics.md),
  derived from [myprompts/TOC_infra.md](myprompts/TOC_infra.md).
  Start here for orientation:
  [Stacks.md](Context-Wiki-Infra/Dashboards/Stacks.md) —
  *Simple Architecture, Simple Deploys*, an
  example-based ladder of fifteen stacks in
  increasing order of complexity, from a static site on
  Cloudflare Pages up to a replicated, SOC 2-audited
  SaaS, and then the five specialist rungs beside it
  (containers and a scheduler, realtime with sticky
  sessions, distributed serverless, a data platform, and
  an AI assistant panel), with the cost, ops burden, and
  "climb when" signal for each rung. It is also the wiki server's front page,
  where the sidebar links to it as **Practical Deploys**.
  Before rung 1:
  [Development Setup.md](Context-Wiki-Infra/Dashboards/Development%20Setup.md)
  — the tools on your own machine (Unix environment,
  password manager, terminal, bash, editor, AI coding
  agent, Homebrew, GitHub and SSH config).
  Rung 15 is **adding an AI assistant** — the side-panel
  chat most SaaS products now ship. It attaches at rung 8
  rather than above rung 14: the server-side proxy
  endpoint, streaming to the panel, per-tenant rate
  limits and usage quotas, protection from unauthorised
  use and bots, prompt injection, retrieval and tool
  calling.
  Sources collected in `Raw/` are grouped into ten
  category folders (`01_foundations` …
  `09_appendices`, plus `12_ai_in_saas`) and registered in
  [Raw/sources.md](Context-Wiki-Infra/Raw/sources.md).

  `Raw/` is populated by `python raw_download.py` (it is
  gitignored — see Quick start above) and holds
  **307 documents (~692,000 words)** from vendor and
  standards
  documentation — Cloudflare, Caddy, nginx, Ubuntu,
  systemd, Let's Encrypt, AWS, Fly.io, Docker,
  Kamal, Coolify, Kubernetes, SQLite, PostgreSQL, Redis, GitHub Actions,
  Firebase Auth, AWS KMS and Google Cloud KMS, HashiCorp
  Vault, OWASP (Top 10, WSTG, ASVS, cheat sheets), OWASP
  ZAP, CloudTrail and Cloud Audit Logs, NIST, CIS
  Controls, SOC 2 guidance, Amazon SES, the Google SRE
  Book, Web3Forms, AWeber, Stripe, MDN, web.dev,
  Terraform, the Anthropic Claude API docs, the OWASP
  LLM Top 10, pgvector and others.
  Refresh or extend them with `python raw_download.py`
  (see [d6_raw_download.md](d6_raw_download.md)).

  The wiki built from them holds **563 OKF pages** joined
  by **5,744 wiki links**: 307 extractive summaries (one
  per capture), 121 hand-written concept pages, 129
  hand-written entity pages, and the dashboards. Browse
  it with `./server_start.sh` at
  <http://localhost:8020>, or rebuild the generated
  layers with `python wiki_build.py all`
  (see [d7_wiki_build.md](d7_wiki_build.md)).
