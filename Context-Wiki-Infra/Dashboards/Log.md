# Cloud Infrastructure Context-Wiki — Operational Log

Chronological changelog of additions, removals,
and structural changes.

## 2026-07-27

* Initialized wiki directory structure
  (Inbox, Raw, Wiki/{Concepts,Entities,Summaries},
  Dashboards) per d3_howto_context_wiki.md, using
  a previous context-wiki vault as a template.
* Created 9 `Raw/` category folders matching the
  Parts of `myprompts/TOC_infra.md`:
  01_foundations, 02_architectures, 03_deployments,
  04_network_storage_db, 05_ops_cicd_security,
  06_product_patterns, 07_playbooks,
  08_scaling_maturity, 09_appendices.
* Seeded `Dashboards/Topics.md` with the main topics
  and keywords derived from `TOC_infra.md`
  (Step 1 of the build pipeline).
* Removed the template vault; repointed
  `wiki_tools.py` and `wiki_server.py` defaults to
  `Context-Wiki-Infra/`.
* Expanded `myprompts/TOC_infra.md` with 6 new
  chapters and 5 new recipes (Cloudflare registrar/
  DNS/Pages, Linux server setup, same-server
  PostgreSQL, Firebase authentication, landing-page
  email capture + autoresponder); chapters
  renumbered 1–51, Parts and appendices unchanged.
  Mirrored the new keywords into
  `Dashboards/Topics.md` sections 01, 02, 03, 04,
  05, 06, and 07. No new `Raw/` categories needed —
  the existing 9 still cover the material.
* Second TOC pass: added Caddy as the default
  reverse proxy / automatic-HTTPS option alongside
  Nginx (new ch. 16 + recipe), SQLite as the
  very-simple-app database (new ch. 23 + recipe),
  and smartphone support — responsive layout, PWA,
  mobile performance (new ch. 9 + recipe).
  Chapters renumbered 1–57; keywords mirrored into
  `Topics.md` sections 02, 03, 04, and 07.
* Third TOC pass, sourced from a working private
  project (a static catalog site: JSON+images
  inventory → Python build scripts → Cloudflare
  Pages): added file-based CMS, backend-free
  interactivity, Wrangler CLI deploys, the
  validate→build→cache-bust→deploy pipeline,
  catalog/inventory sites, Web3Forms forms, and
  AWeber autoresponder; plus Appendix D (case study)
  and 3 new recipes. Chapters renumbered 1–66,
  appendices now A–D. Keywords mirrored into
  `Topics.md` sections 02, 03, 06, 07, and 09.
  Registered it as a local reference implementation
  in `Raw/sources.md`.
  Note: AWeber is recorded as the chosen
  autoresponder per instruction — it is not
  referenced anywhere in that project's code.
* **Step 2 of the build pipeline — downloads.**
  Populated `Raw/` with 181 source documents
  (~441,000 words, 4.0 MB) covering every Part of
  `myprompts/TOC_infra.md`, fetched with the new
  `raw_download.py` from the list in
  `raw_sources.json`:
  01_foundations 16, 02_architectures 14,
  03_deployments 50, 04_network_storage_db 23,
  05_ops_cicd_security 26, 06_product_patterns 20,
  07_playbooks 12, 08_scaling_maturity 11,
  09_appendices 9.
  Sources are primary/vendor documentation wherever
  possible: Cloudflare (Pages, Wrangler, Registrar,
  DNS, R2), Caddy, nginx, Ubuntu Server, systemd,
  Let's Encrypt/Certbot, Hetzner, DigitalOcean, AWS,
  Fly.io, Render, Railway, Docker, Kubernetes,
  SQLite, PostgreSQL, Redis, RabbitMQ, GitHub
  Actions, GitLab CI, Firebase Auth, Supabase,
  Auth0, Clerk, OWASP, Google SRE Book, Prometheus,
  Grafana Loki, Web3Forms, AWeber, Mailchimp,
  Stripe, MDN, web.dev, Terraform, Pulumi.
  Every file carries a provenance header (title,
  source URL, retrieval date) and is registered in
  `Raw/sources.md`, which is now generated from
  `raw_sources.json`.
* Recorded 7 unreachable sources and their
  substitutes under "Known gaps" in
  `Raw/sources.md` — chiefly bot-blocked vendor
  help centres (MySQL, AWeber) and client-rendered
  pages (Terraform Registry, Stripe quickstarts).
  Nothing in the TOC is left without a source.
* Fourth TOC pass — **secrets, key management, and
  security testing**. Added 3 chapters to Part V
  (36 Storing Secrets Safely; 37 Key Management:
  KMS and HSMs — envelope encryption, rotation,
  AWS KMS / Google Cloud KMS / CloudHSM;
  39 Testing the Security of Your Website or App),
  3 recipes to Part VII (61 Get Secrets Out of Your
  Repository; 62 Encrypt Application Data with
  Envelope Encryption; 66 Run a Security Test Pass
  Before Launch), and Appendix E (Security Toolbox
  — secret stores, KMS/HSM options and testing
  tools side by side). Chapters renumbered 1–72,
  appendices now A–E. Keywords mirrored into
  `Topics.md` sections 05, 07 and 09.
* Downloaded 47 further sources into
  `Raw/05_ops_cicd_security/`, which now holds 73
  files. Secrets: AWS Secrets Manager and Parameter
  Store, Google Secret Manager, Azure Key Vault,
  HashiCorp Vault, Cloudflare Workers secrets,
  Docker Compose secrets, systemd credentials,
  GitHub secret scanning and push protection,
  Gitleaks, SOPS, IAM best practices. Keys: the AWS
  KMS product page (as requested), the KMS
  developer guide (overview, concepts, key
  policies, rotation), S3 SSE-KMS, AWS CloudHSM,
  Google Cloud KMS (overview, envelope encryption,
  HSM, rotation), NIST CMVP/FIPS 140-3, and the
  OWASP cryptographic-storage and key-management
  cheat sheets. Testing: OWASP WSTG (project page
  and stable checklist), ASVS, ZAP (getting
  started, desktop walkthrough, Docker baseline
  scan for CI), GitHub code scanning and Dependabot
  alerts, `npm audit`, `pip-audit`, Trivy, Lynis,
  PortSwigger Web Security Academy, the AWS
  penetration-testing policy, and the OWASP
  injection / XSS / CSRF / input-validation /
  vulnerable-dependency cheat sheets.
  `Raw/` total: 228 documents, ~531,000 words.
  Replaced the SSL Labs best-practices landing page
  (a link stub) with the OWASP WSTG stable
  checklist; TLS configuration guidance now comes
  from the OWASP TLS cheat sheet and the MDN
  practical implementation guides.
* Fifth TOC pass — **SOC 2 compliance**. Added
  ch. 40 (Making Your App SOC 2 Compliant: the
  Trust Services Criteria in plain English —
  encryption in transit and at rest, access control
  and access reviews, audit logging, change
  management, backups, vendor management) and
  ch. 74 (Getting Audited: Type I vs Type II,
  choosing an auditor, the observation window,
  compliance-automation platforms, SOC 2 vs
  ISO 27001); recipes 64 (Encrypt Everything, Then
  Prove It) and 69 (A SOC 2 Readiness Sprint for a
  Tiny Team); and Appendix F (SOC 2 Control Map —
  each criterion matched to the concrete thing you
  configure in this book, plus what you inherit
  from your provider's own report). Chapters
  renumbered 1–76, appendices now A–F. Keywords
  mirrored into `Topics.md` sections 05, 07, 08
  and 09.
* Downloaded 25 SOC 2 sources — 21 into
  `Raw/05_ops_cicd_security/` (now 94 files) and 4
  into `Raw/08_scaling_maturity/` (now 15).
  Criteria and provider posture: AICPA SOC 2
  overview, AWS SOC FAQs, AWS Artifact, Google
  Cloud SOC 2, Cloudflare Trust Hub, AWS
  Well-Architected security pillar. Encryption:
  EBS, RDS, Google default encryption at rest,
  CMEK, PostgreSQL encryption options, HSTS.
  Audit and change: CloudTrail, Google Cloud Audit
  Logs, AWS Config, OWASP logging cheat sheet.
  Access, availability, incident response: OWASP
  authorization cheat sheet, IAM Access Analyzer,
  AWS Backup, NIST SP 800-61, CIS Controls. Audit
  process: Vanta (what is SOC 2, compliance
  checklist), Drata, ISO 27001.
  `Raw/` total: 253 documents, ~579,000 words.
  Note: the AICPA does not publish the Trust
  Services Criteria document itself at a fetchable
  URL — only the overview page was captured, so
  criterion-level detail comes from the vendor
  guides and must be cross-checked against the
  official TSC PDF before anything is asserted as
  authoritative.
* Sixth TOC pass — **transactional email and the
  ladder**. Added ch. 47 (Sending Email from Your
  App: transactional email with Amazon SES —
  domain verification, DKIM/SPF/DMARC, leaving the
  sandbox, SMTP vs SDK, bounce and complaint
  handling, and when Postmark/Resend is worth the
  higher price) and recipe 63 (Send Your First
  Transactional Email with Amazon SES). Added
  ch. 6, "The Ladder", opening Part II. Chapters
  renumbered 1–79; appendices unchanged at A–F.
* Created `Dashboards/Stacks.md` — the example-based
  index of ten stacks in increasing order of
  complexity, each rung adding exactly one
  capability: (1) static site on Cloudflare Pages,
  (2) + build script / file-based CMS, (3) +
  Web3Forms, (4) + email capture and autoresponder,
  (5) + VPS with Caddy and FastAPI, (6) + SQLite or
  PostgreSQL, (7) + Amazon SES, (8) + Firebase
  Authentication, (9) + Stripe, secret manager and
  CI/CD, (10) + read replicas, IaC and SOC 2. Each
  rung records the stack, monthly cost, ops burden,
  the signal that says climb, and its chapter and
  `Raw/` citations; all 45 chapter references were
  checked against the TOC. Keywords mirrored into
  `Topics.md` sections 02 and 06.
* Downloaded 18 email sources into
  `Raw/06_product_patterns/` (now 38 files): the
  SES product and pricing pages, developer guide,
  identity verification, Easy DKIM, SPF, custom
  MAIL FROM, DMARC, production-access request,
  sending quotas, SMTP interface, SDK sending,
  event publishing, bounce/complaint deliverability,
  Cloudflare DNS email records, Google's bulk sender
  guidelines, Resend and Postmark.
  `Raw/` total: 271 documents, ~615,000 words.
* **Fixed an encoding bug in `raw_download.py`.**
  `requests` falls back to ISO-8859-1 for `text/*`
  responses that omit a charset, so UTF-8
  punctuation was landing as mojibake — 2,247
  occurrences across 61 files (worst: the systemd
  manual at 1,517). The fetcher now sniffs the
  encoding when the header does not declare one,
  and every file was re-downloaded with `--force`.
  Re-scan is clean; the only remaining non-ASCII
  flagged is legitimate French text in
  `schema-org-product.md`.

## 2026-07-27 — Steps 3 and 4: the wiki itself

* **Built the wiki from `Raw/`** per `d2_docs2okf.md`
  and `d3_howto_context_wiki.md`. The vault now holds
  **438 pages**, all OKF-conformant, joined by **3,201
  wiki links with no dangling targets**.
* Added `wiki_build.py` (`summaries`, `crosslink`,
  `index`, `all`) to generate the mechanical layers and
  regenerate the index. Documented in `d7_wiki_build.md`.
* **`Wiki/Summaries/` — 271 pages, one per capture.**
  Generated, and deliberately *extractive*: each carries
  the source's own lead paragraphs and heading outline
  quoted verbatim, the retrieval date, and a link to the
  immutable file in `Raw/`. Nothing is paraphrased, so a
  summary cannot drift from its source or invent a claim.
* **`Wiki/Concepts/` — 81 pages, hand-written.** The
  ideas and practices layer: `Cloud Service Models`,
  `The Ladder`, `Static Site Hosting`, `File-Based CMS`,
  `Reverse Proxy`, `Automatic HTTPS`,
  `Linux Server Hardening`, `Relational Databases`,
  `Database Backups`, `Secrets Management`,
  `Envelope Encryption`, `Hardware Security Module`,
  `Encryption at Rest` / `in Transit`, `Authentication`,
  `Authorization`, `Security Testing`, `SOC 2`,
  `Trust Services Criteria`, `Audit Logging`,
  `Access Review`, `Transactional Email`,
  `Email Authentication`, `Email Deliverability`,
  `Cost Control`, `Anti-Patterns`, and the rest.
* **`Wiki/Entities/` — 81 pages, hand-written.** The
  concrete layer: Cloudflare and its services, Wrangler,
  Caddy, Nginx, Ubuntu Server, systemd, UFW, Let's
  Encrypt, Certbot, Hetzner, DigitalOcean, EC2, Fly.io,
  Render, Railway, Docker, Compose, Kubernetes, Fargate,
  Lambda, API Gateway, S3, VPC, SQLite, PostgreSQL,
  MariaDB, RDS, PgBouncer, Redis, RabbitMQ, restic,
  FastAPI, Django, GitHub Actions, GitLab CI, Firebase
  Auth, Supabase, Auth0, Clerk, AWS KMS, Google Cloud
  KMS, CloudHSM, Secrets Manager, Parameter Store,
  Google Secret Manager, Azure Key Vault, Vault, SOPS,
  Gitleaks, OWASP, ZAP, Trivy, Lynis, Dependabot,
  CodeQL, Prometheus, Loki, Uptime Kuma, CloudTrail,
  Cloud Audit Logs, AWS Config, AWS Backup, AWS
  Artifact, AWS IAM, Vanta, Drata, Terraform, Pulumi,
  Web3Forms, AWeber, Mailchimp, Amazon SES, Postmark,
  Resend, Stripe.
* Every Concept and Entity page ends with `## Related`
  wiki links and a `## Sources` list citing the summary
  pages it rests on, so the graph is bi-directional and
  every claim traces back to an immutable capture. The
  server's backlink pane is populated as a result —
  `Envelope Encryption`, for instance, has 17 inbound
  links.
* `Dashboards/Index.md` regenerated from page
  frontmatter: 433 entries grouped by layer, each with
  its one-line description. Added OKF frontmatter to
  `Topics.md`, `Stacks.md` and `Projects.md`;
  `Index.md` and `Log.md` correctly have none, being OKF
  reserved filenames.
* **Three bugs found and fixed while building**, each
  surfaced by real captured text rather than by
  inspection:
  1. A page named `CI/CD Pipeline` — a slash breaks both
     the file path and the server's link parser, which
     keeps only the segment after the last slash.
     Renamed to `Continuous Integration and Delivery`.
  2. Frontmatter values containing `\` or `---` broke
     YAML parsing and, worse, truncated the body in
     `wiki_server.split_frontmatter`, which splits
     naively on `---`. The generator now strips both.
  3. Captures that use doubled square brackets as their
     own syntax (`fly.toml` service blocks) rendered as
     broken wiki links. Quoted source text is now
     escaped.
* Verified end to end: the server on port 8020 renders
  every layer, infoboxes populate from frontmatter,
  backlinks resolve, and search returns hits across all
  three layers.
* **Closed the traceability gap in `wiki_server.py`.**
  All 271 summaries carry a `source_file` pointing at a
  capture in `Raw/`, but `Raw/` was not served, so the
  trail dead-ended in the browser. Added `/raw/` (browse
  captures by category) and `/raw/<category>/<file>.md`
  (read one, provenance header stripped, with a link
  back to its wiki page), made `source_file` in the
  infobox a link, and added the captures to the sidebar.
  Paths are resolved and constrained to `Raw/`, so `..`
  traversal — plain or percent-encoded — returns 404,
  and only `.md` files inside `Raw/` are readable.
  The full trail is now one click each way:
  Concept -> Summary -> Raw capture -> original URL.

## 2026-07-27 — Front page, and rung zero

* **`Stacks` is now the front page.** `wiki_server.py`
  serves `Dashboards/Stacks.md` at `/` (constant
  `HOME_PAGE`), so the wiki opens on the ten-rung
  ladder rather than on a 444-line list of pages. The
  generated index is still one click away at
  `/wiki/Index`.
* **Sidebar reworked.** Three pinned entries above a
  rule, then the section counts: `Stacks` (bold, links
  to `/`), `Development Setup`, `Index`. The old
  "Main Page" entry is gone — the page it pointed at is
  `Index`, and it is now named that in the navigation.
  Pinned pages are the `NAV_PAGES` constant; the 404
  page points at the same two destinations.
* **New dashboard: `Development Setup`** — rung zero,
  the developer machine every rung of `Stacks` assumes.
  Nine sections, each ending in something checkable: a
  Unix-based environment (Linux / macOS / WSL), a
  password manager, a terminal, working `bash`
  knowledge, an editor, an AI coding agent, Homebrew
  with the starting `brew install` list, a GitHub
  account with `git config --global` and a secrets-aware
  `.gitignore`, and an `~/.ssh` setup with one key per
  purpose, a `config` file and the permissions SSH
  insists on. Ends with the whole thing as a
  nine-row checklist.
* **11 new Entity pages** to keep it linked rather than
  listed: `Homebrew`, `Bitwarden`, `iTerm2`, `Bash`,
  `Zed`, `Visual Studio Code`, `Claude Code`, `uv`,
  `Git`, `GitHub`, `Windows Subsystem for Linux`.
  Entities: 81 -> 92; the vault now holds 450 pages and
  3,399 links, still with no dangling targets.
  These are the first pages in the wiki with no `Raw/`
  capture behind them — the corpus was downloaded
  against `TOC_infra.md`, which starts at rung 1. Each
  cites its upstream documentation URL and says so
  explicitly in `## Sources`, so the gap is visible
  rather than papered over.
* Cross-referenced both ways: `Stacks` and `Topics`
  point at `Development Setup`, `Topics` gains a
  `00_dev_environment` keyword section (marked as
  having no `Raw/` folder), and `wiki_build.py index`
  now names it in the index preamble.
* Re-ran `wiki_build.py crosslink`: 7 summaries picked
  up genuinely relevant new links (Homebrew in the
  dev/prod-parity and server-setup captures, WSL in a
  DigitalOcean one, VS Code, Claude Code). `GitHub` and
  `Bash` went into `LINK_STOPLIST` first — a bare
  `github.com` URL appears in 116 captures, which would
  have made `[[GitHub]]` a link on almost every summary
  and meant nothing.
* Ripple update, by hand where it belonged: the
  `## Related` lines of `SSH Key Authentication`,
  `Secrets Management`, `Git-Driven Deployment`,
  `Linux Server Hardening`, `GitHub Actions` and
  `Static Build Pipeline` now point back at
  `Development Setup` and the new tool pages, so the
  graph is bi-directional rather than one-way. The new
  dashboard has 18 inbound links.
* Verified in the browser: `/` renders the ladder,
  `/wiki/Index` the index, all 11 new pages 200, the
  sidebar reads Stacks / Development Setup / Index,
  and the whole vault has zero dangling links.

## 2026-07-27 — Wikipedia links on every content page

* **All 173 content pages now carry an English Wikipedia
  link** — 156 with an article (128 distinct articles),
  17 deliberately without. It shows in the infobox,
  labelled with the *article's* title, and opens in a new
  tab (`target="_blank"`, `rel="noopener noreferrer"`,
  with a ↗ marker so an off-site link looks different
  from an internal one).
* **New field, new tooling.** `wikipedia:` is an optional
  OKF frontmatter field (documented in `d1_okf.md`),
  written by the new `wikipedia_links.py` from the
  curated map in `wikipedia_links.json`:
  `status` (offline coverage), `check` (verify against
  the MediaWiki API), `apply` (write the frontmatter,
  idempotently). Full write-up in `d8_wikipedia_links.md`.
* **Titles are curated, never guessed** — and `check`
  exists because guessing fails in ways that are hard to
  spot afterwards. It reports missing, redirected and
  disambiguation targets, and prints each article's first
  sentence. Caught during the first pass:
  `Trivy` is a commune in Saône-et-Loire, not the
  scanner; `Resend` redirects to *Retransmission (data
  networks)*; `Railway`, `Render`, `Postmark` and `Clerk`
  are all ordinary English words with articles about
  something else entirely; `Data at rest` and
  `Data in transit` both redirect to *Digital data*
  (used *Disk encryption* and *Transport Layer Security*
  instead); `Email deliverability` redirects to
  *Cold email* (used *Anti-spam techniques*).
* **Two rules produced the map.** Link the article about
  *this* thing where it exists; otherwise link the vendor
  or family article, never a generic concept — so the AWS
  services without articles point at *Amazon Web
  Services* and the six Cloudflare pages at *Cloudflare*,
  while the concept articles stay attached to the Concept
  pages that own them. Because the infobox shows the
  target title, a broader link is visible as one.
* **Nothing for the summaries.** A summary is about a
  specific captured document rather than a subject; its
  infobox already links the capture in `Raw/`.
* Verified twice over: `check` reports 0 problems across
  the 156 titles, and an HTTP sweep of all 128 distinct
  URLs returns 200 for every one, including the awkward
  forms — `Let's_Encrypt`, `Stripe,_Inc.`,
  `Zed_(text_editor)`, `1.1.1.1`.
* `status` fails loudly if a content page is missing from
  the map or the map names a page that no longer exists,
  so the two cannot drift apart; the librarian
  instructions in `claude.md` now make that Step 5.

## 2026-07-27 — Official-site links where Wikipedia has none

* **The 15 pages Wikipedia does not cover now link to the
  project's own site**, so no content page is a dead end.
  URLs supplied and used verbatim: AWeber, Clerk, Drata,
  Fly.io, Gitleaks, Postmark, Railway, Render, Resend,
  SOPS, Supabase Auth, Trivy, Uptime Kuma, uv, Web3Forms.
* **New `website:` OKF field**, rendered in the infobox
  exactly like `wikipedia:` — new tab, `noopener
  noreferrer`, ↗ marker — but labelled with the host and
  path rather than an article title (`trivy.dev`,
  `docs.astral.sh/uv`, `supabase.com/auth`). Wikipedia
  takes precedence where both could exist: it is the
  neutral description, the vendor site is the sales one.
* `wikipedia_links.json` gained a `websites` map beside
  `links`; `wikipedia_links.py` writes both fields,
  `status` counts both, and `check` now fetches every
  site URL as well as verifying every article title.
  All 15 answered 200. A `403` is reported as `WAF`
  rather than a failure — Drata's site sits behind a bot
  challenge that refuses automated clients, which says
  nothing about whether the URL is right.
* Coverage is now: 156 pages with a Wikipedia article,
  15 with their own site, and 2 with neither —
  `Cost Control` and `The Ladder`, which are this wiki's
  own framing rather than subjects anyone else describes.
* Note for later: the Uptime Kuma URL used is the one
  supplied, `uptimekuma.org`. The project's own docs live
  at `uptime.kuma.pet` (repo: `louislam/uptime-kuma`);
  both answer, so this is a choice, not an error.

## 2026-07-28 — Languages, data, and four more rungs

* **23 new pages** covering the requested topics, in the
  usual two layers. Concepts (7): `Sticky Sessions`,
  `Container Orchestration`, `Event-Driven Architecture`,
  `Distributed Data Processing`, `DataFrames`,
  `Server-Side Rendering`, `WebAssembly`. Entities (16):
  `Apache Spark`, `Databricks`, `pandas`, `Polars`,
  `DuckDB`, `Apache Arrow`, `Node.js`, `React`,
  `Next.js`, `Express`, `Rust`, `Axum`, `Actix Web`,
  `Tokio`, `wasm-bindgen`, `Leptos`.
  Concepts 81 -> 88, Entities 92 -> 108; the vault now
  holds 473 pages and 3,872 links, still with no dangling
  targets.
* Two pages were added beyond what was asked for, because
  the argument does not hold without them: `DuckDB` and
  `Apache Arrow`. The advice throughout is "try one
  machine first", and those are the two things that make
  it true — Arrow is why moving between pandas, Polars
  and DuckDB is free, and DuckDB is the SQL answer to
  the same problem Polars solves with method chains.
* **`Stacks` gained rungs 11–14**, above the audited-SaaS
  rung 10, each in the existing format (stack, cost, ops
  burden, climb-when signal):
  11 containers and a scheduler ([[Docker]] images in CI,
  [[AWS Fargate]] / Cloud Run / [[Kubernetes]]);
  12 realtime with [[Sticky Sessions]] (WebSocket tier,
  cookie affinity, [[Redis]] for shared state);
  13 distributed serverless ([[AWS Lambda]], SQS /
  EventBridge, dead-letter queues, idempotent consumers);
  14 a data platform (Parquet lake on [[Object Storage]],
  [[Apache Spark]] or [[Databricks]]).
* Stated plainly on the page and in [[The Ladder]]:
  **rungs 11–14 are not a sequence.** Above rung 10 you
  add whichever one your problem names. Most products
  that get there need one of the four; almost none need
  all of them. The rung-12 entry makes the distinction
  the whole topic turns on — affinity for a WebSocket is
  correct, affinity because sessions live in process
  memory is a crutch with a bill attached.
* The new rungs cite wiki pages rather than chapter
  numbers: `myprompts/TOC_infra.md` has no chapters for
  this material yet, and inventing citations would have
  been worse than admitting the gap.
* `Topics.md` gained a `10_languages_and_data` section
  (Node/React/Next, Rust/Tokio/Axum/Actix, Wasm via
  wasm-bindgen and Leptos, pandas/Polars/DuckDB/Arrow,
  Spark/Databricks) and the rung 11–14 keywords went into
  `02_architectures`. Marked as having no `Raw/` folder —
  these pages cite upstream documentation directly, like
  the `00_dev_environment` set.
* Outside links: 17 of the new pages got a Wikipedia
  article, 4 their own site. `check` caught two more
  name collisions of the kind that makes this map worth
  curating — **Axum** is a town in Ethiopia, and
  **Actix** redirects to a graphics-card maker that shut
  down in 1998. `DataFrames` gets nothing: Wikipedia's
  `Data frame` is about network frames.
* `LINK_STOPLIST` gained **Express** and **React** after
  reviewing what the crosslinker did with them: "S3
  Express One Zone", "SQL Server Express Edition",
  "express implicit dependency", and six summaries where
  "react" was the verb, as in "react to production
  issues". Roughly 40% noise in both cases. With them
  stopped, 35 summaries picked up genuinely relevant
  links instead — [[Node.js]] in 20, [[Rust]] in 9,
  [[Next.js]] in 7.

## 2026-07-28 — Failure modes, testing, micro-VMs, CI/CD

* **30 new pages.** Concepts (21): the ten failure
  modes — `Single Point of Failure`,
  `Cascading Failure`, `Retry Storm`, `Cache Stampede`,
  `Hot Partition`, `Replication Lag`,
  `Duplicate Processing`, `Queue Backlog`,
  `Poison Message`, `Split Brain` — under the overview
  page `Failure Modes`, plus `Idempotency`,
  `Chaos Engineering`, `Micro-VMs`, `Cold Starts`,
  `Automated Testing`, `Fuzz Testing`,
  `Red Team and Blue Team`, `Deployment Strategies`,
  `Container Images` and `Docker Build Cache`.
  Entities (9): `Firecracker`, `Cloudflare Workers`,
  `Google Cloud Run`, `pytest`, `Playwright`, `AFL++`,
  `OSS-Fuzz`, `MITRE ATT&CK`, `BuildKit`.
  Concepts 88 -> 109, Entities 108 -> 117; the vault now
  holds 503 pages and 4,760 links, still with no
  dangling targets.
* **The ten failure modes are one page each, indexed by
  a table.** Each states the shape, what makes it
  possible, the fix, and the metric that shows it —
  because the metric is usually not error rate.
  `Queue Backlog` and `Replication Lag` in particular
  are failures where every dashboard stays green.
  The overview page adds the part that belongs in this
  wiki specifically: **which of these you can even
  have**. At rungs 1–4 of [[Stacks]] most of the list
  is unreachable, and each rung up adds failure modes as
  reliably as it adds capability — the sharpest argument
  [[The Ladder]] has.
* Three supporting pages were written because the ten
  do not stand up without them: `Idempotency` (the
  property that makes retries and redelivery safe, cited
  by four of the ten), `Chaos Engineering` (the ten as
  experiments you can run in an afternoon, with a table
  of nine of them), and `Failure Modes` itself.
* **Micro-servers.** `Micro-VMs` covers the "starts in
  milliseconds" claim with the comparison that makes it
  meaningful — VM 30–60 s, micro-VM ~125 ms, container
  0.5–2 s, V8 isolate < 5 ms — and says plainly that you
  consume this rather than run it, unless isolating
  other people's code *is* the product. `Cold Starts`
  splits the latency into platform, runtime and **your
  own init code**, which is the part that usually
  dominates and the only part you control.
  `Firecracker`, `Cloudflare Workers` and
  `Google Cloud Run` are the three concrete platforms;
  Workers and Cloud Run also filled real gaps — the wiki
  had `Wrangler` and `Cloudflare Pages Functions` but no
  page for the runtime underneath them.
* **Testing.** `Automated Testing` ranks the layers by
  what a small team gets back per hour of maintenance,
  and names the first four tests to write (smoke test on
  the deployed URL, the money path, a test for every bug
  fixed, and a restore drill). `Fuzz Testing` separates
  coverage-guided fuzzing ([[AFL++]], [[OSS-Fuzz]]) from
  property-based testing, and says which one a web
  developer should actually reach for. `pytest` and
  `Playwright` are the tools; both are the first pages
  here about testing rather than about deploying.
* **Red team / blue team** is written against the
  confusion that matters: a red team engagement tests
  the *defenders*, a [[Penetration Testing]] engagement
  tests the *software*. A comparison table, what the blue
  team needs before an exercise means anything, and a
  two-hour version two people can run this month with no
  budget. `MITRE ATT&CK` gives both sides the vocabulary,
  reduced to the five techniques a small SaaS is actually
  breached by.
* **CI/CD.** `Continuous Integration and Delivery` was a
  short page; it now carries the anatomy of a real
  pipeline (stages ordered by failure probability ÷ run
  time), the two properties that matter more than the
  stage list — **build once, deploy many** and fast
  feedback first — how to keep it fast, and OIDC instead
  of long-lived cloud keys. `Deployment Strategies` is
  new alongside it: recreate / rolling / blue-green /
  canary with the trade table, the expand-contract
  migration that every zero-downtime strategy actually
  depends on, and the observation that a deployment
  strategy is really a rollback strategy.
* **Docker.** `Container Images` (layers, multi-stage,
  non-root, exec-form `CMD`, `.dockerignore`, tags vs
  digests) and `Docker Build Cache` (the invalidation
  rules, the dependency-manifest-first ordering, cache
  export in CI, cache mounts), with `BuildKit` as the
  engine page — build secrets and `--mount=type=cache`
  are the two features worth adopting immediately. The
  existing `Docker` and `Docker Compose` pages were
  deliberately left short and now link out to these
  rather than growing.
* Ripple update across **31 existing pages**: the
  queue pages point at the four queue failures,
  `Read Replicas` at `Replication Lag` and `Split Brain`,
  `Caching` at `Cache Stampede`, `Load Balancing` at the
  first two failure modes, `Serverless Architecture` at
  the micro-VM cluster, `Security Testing` and
  `Penetration Testing` at the testing cluster, and
  `Docker`, `Kubernetes`, `AWS Fargate`, `Fly.io`,
  `AWS Lambda`, `Cloudflare`, `Wrangler` and the rest at
  the new pages that describe what they do.
* Outside links: 30 curated titles verified with
  `wikipedia_links.py check` before `apply`. Four were
  wrong on the first pass and the check caught all four —
  `AFL++` redirects to *American Fuzzy Lop (software)*,
  `Reliable messaging` redirects to *Reliability
  (computer networking)*, `MITRE ATT&CK` is filed under
  *ATT&CK*, and **OSS-Fuzz has no article at all**, so it
  joins the twenty pages that link to their own site.
  Coverage is now 203 Wikipedia articles, 20 project
  sites, 3 with neither.
* `Topics.md` gained an `11_reliability_and_failure`
  section and new keyword blocks in `03_deployments`
  (micro-VMs, cold starts, Dockerfile, build cache,
  deployment strategies) and `05_ops_cicd_security`
  (pipeline design, automated testing, fuzzing, red and
  blue team). Marked as having no `Raw/` folder: the
  reliability pages rest on captures already held under
  other categories, and are cited as such.
* Re-ran `wiki_build.py crosslink`: 47 summaries picked
  up new links, [[Cloudflare Workers]] in 8 and
  [[Container Images]] in 3. Nothing needed adding to
  `LINK_STOPLIST` this round — the new names are
  specific enough not to collide with ordinary prose.

## 2026-07-28 — `just` as the project command runner

* **New Entity page `just`** — the command runner, added
  in place of `make`/`gmake` for the job almost everyone
  actually uses `make` for: a menu of project commands.
  A worked `justfile` for a stack in this wiki (clean,
  images, build, serve, deploy with an argument, test,
  fmt), and a nine-row comparison table covering the
  specific `make` traps it removes — timestamp skipping,
  required tabs, `.PHONY`, one shell per line, doubled
  `$$`, and failing when run from a subdirectory.
  Entities 117 -> 118; the vault now holds 504 pages and
  4,811 links, no dangling targets.
* Positioned honestly: **it is not a build system.** If
  you need incremental rebuilds from file times, that is
  still `make` or `ninja`. What `just` gives this wiki's
  stacks is one committed file where the build and deploy
  commands live, so [[Continuous Integration and Delivery]]
  can call the same recipe a laptop does and the two
  cannot drift.
* Ripple update: `Development Setup` adds
  `brew install just` to the rung-zero list and names it
  in the checklist; `Static Build Pipeline` gains it as
  the front door over the `s1_`…`s4_` scripts;
  `Continuous Integration and Delivery`, `Homebrew` and
  `uv` link to it.
* Outside link: Wikipedia has no article — `Just
  (command runner)` and `Just (software)` are both
  missing — so it joins the pages linking to their own
  site, <https://just.systems/>. Now 21 such pages.
* **`just` went straight into `LINK_STOPLIST`.** As a
  four-letter ordinary English word it matched 83
  summaries on the first `crosslink` run ("just add",
  "just works"), which would have made the link
  meaningless. Stoplisted and re-run: 0 false matches,
  and the 47 genuinely-changed summaries from the earlier
  pass are unaffected.

## 2026-07-28 — gmake and Invoke, cross-linked with just

* **Two new Entity pages**, completing the task-runner
  family: `GNU Make` (the page a search for *gmake*
  lands on) and `Invoke`, the Python task runner.
  Entities 118 -> 120; the vault now holds 506 pages and
  4,880 links, no dangling targets.
* `GNU Make` is deliberately **not** written as the
  loser of the earlier `just` comparison. It leads with
  what Make is uniquely good at — incremental work driven
  by file timestamps, and `make -j` parallelism for free
  — and states the test plainly: *if you find yourself
  writing "skip this if the output is newer" in a script,
  you are reimplementing Make badly.* The friction list
  follows, framed as the cost of a build system charged
  to a use case that is not a build.
* It also answers the question the name raises.
  **`gmake` is GNU Make under a name that distinguishes
  it from BSD make** — and on macOS `/usr/bin/make` is
  GNU Make **3.81 from 2006**, kept for licence reasons,
  which is why `brew install make` ships 4.x as `gmake`
  and why documentation writes `gmake` at all.
* `Invoke` covers what neither runner can do: tasks are
  **Python functions**, so they can loop, branch, import
  and raise. The `@task` signature becomes the CLI —
  parameters to options, booleans to flags, docstrings
  to help. Two things get named that are easy to miss:
  **Fabric** is the same `@task` functions aimed at a
  server over SSH (the honest middle ground between
  hand-run commands and [[Infrastructure as Code]] for a
  [[One-Box Deployment]]), and the **bootstrap problem**
  — `inv` cannot create the Python environment it lives
  in, which [[uv]] solves with `uv run inv build`.
* **All three now cross-link both ways**, and each
  carries the comparison from its own angle rather than
  one table copied three times. The decision rule is
  stated identically on each page: the tool decides
  whether the work is needed → [[GNU Make]]; you decide,
  and it is a one-liner → [[just]]; the task needs real
  programming or a remote host → [[Invoke]].
  `Static Build Pipeline`,
  `Continuous Integration and Delivery`,
  `Development Setup`, `Homebrew` and `uv` link to all
  three.
* **`Invoke` joined `just` in `LINK_STOPLIST`** before
  the first crosslink run — it is an ordinary English
  verb, and "invoke the function" / "Lambda invoke"
  appears throughout the corpus. `GNU Make` needed no
  guard: as a two-word phrase it matches nothing by
  accident. Result: 0 false links from either.
* Outside links: `GNU Make` -> *Make (software)*;
  Wikipedia has nothing for `Invoke` (`Invoke
  (software)` and `Pyinvoke` are both missing), so it
  links to <https://www.pyinvoke.org/>. Coverage is now
  204 articles, 22 project sites, 3 with neither.
