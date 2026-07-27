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
