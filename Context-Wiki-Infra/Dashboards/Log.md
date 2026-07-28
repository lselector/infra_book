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
