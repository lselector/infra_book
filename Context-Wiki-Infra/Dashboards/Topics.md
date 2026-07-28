---
type: Dashboard
title: "Cloud Infrastructure - Topics and Keywords"
description: "The keyword plan behind the wiki, one section per Part of the book TOC."
tags: [topics, plan, orientation]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloud Infrastructure — Topics and Keywords

The plan and checklist for building this wiki
(Step 1 of d3_howto_context_wiki.md).
Derived from `myprompts/TOC_infra.md`; one section
per Part, matching the `Raw/` category folders.

See also [Stacks.md](Stacks.md) — the same material
arranged as a ten-rung ladder of example stacks in
increasing order of complexity — and
[Development Setup.md](Development%20Setup.md), the
tools on your own machine that come before rung 1.

## 00_dev_environment — Your Development Machine
keywords: unix-based development environment, Linux,
macOS, WSL, Windows Subsystem for Linux, WSL 2,
password manager, Bitwarden, master password,
recovery codes, MFA on developer accounts, terminal
emulator, iTerm2, Windows Terminal, split panes,
bash shell, shell basics, pipes and redirection,
shell scripting, set -euo pipefail, shellcheck,
coding editor, Zed, VS Code, Cursor, Sublime Text,
WebStorm, PyCharm, RustRover, Neovim, Vim, Helix,
format on save, AI coding agent, Claude Code,
CLAUDE.md conventions, reviewing agent diffs,
Homebrew, brew install, formulae and casks, uv,
Python project and package management, uv.lock,
just, justfile, command runner, recipes, just --list,
just vs make, GNU Make, gmake, make vs gmake, Makefile,
targets and prerequisites, .PHONY, tab-indented recipes,
make -j parallel builds, macOS make 3.81, dotenv-load,
Invoke, pyinvoke, tasks.py, @task decorator, inv --list,
c.run, task namespaces, Fabric, remote tasks over SSH,
task runner vs build system,
GitHub account, git config --global, .gitignore for
secrets, secret scanning, ssh configuration,
~/.ssh/config, ssh-keygen ed25519, key per host,
authorized_keys, file permissions on keys
note: no `Raw/` category folder — this Part is written
from first-hand practice and vendor sites, not from the
downloaded corpus.

## 10_languages_and_data — Languages, Frameworks, Data
keywords: Node.js, event loop, never block the event
loop, npm ci, package-lock.json, PM2, process per core,
Express, Fastify, Hono, React, components, SPA vs SSR
vs SSG, Next.js, App Router, server components,
hydration, ISR, output export, edge runtime, bundle
size, code splitting,
Rust, static binary, no garbage collector, Tokio, async
runtime, spawn_blocking, Axum, extractors, Tower
middleware, Actix Web, sqlx, tracing, small container
images, distroless,
Rust in the browser, WebAssembly, Wasm, wasm-bindgen,
wasm-pack, web-sys, wasm-opt, bundle size budget,
Leptos, Yew, Dioxus, signals, server functions,
pandas, DataFrame, dtypes, memory blowup, Polars, lazy
scan, predicate pushdown, multi-threaded, DuckDB,
embedded OLAP, SQL over Parquet, Apache Arrow, columnar
memory format, Parquet, one big machine first,
Apache Spark, PySpark, partitions, shuffle, wide vs
narrow transformations, broadcast join, data skew,
ephemeral clusters, Databricks, Delta Lake, Unity
Catalog, lakehouse, DBU cost, notebook drift
note: no `Raw/` category folder yet — these pages cite
upstream documentation directly.

## 01_foundations — Thinking About Infrastructure
keywords: infrastructure for web and SaaS, IaaS vs
PaaS vs serverless vs SaaS, DNS, SSL/TLS, HTTP,
domains, domain registrar, nameservers, DNS records
(A, CNAME, TXT, MX), CDN, load balancers, 12-factor
app, automation, "keep it boring"

## 02_architectures — Static to SaaS
keywords: the ladder, stacks in increasing
complexity, rungs 11-14 above the main climb,
container orchestration, scheduler, rolling deploy,
service discovery, stateless containers,
realtime tier, WebSockets, sticky sessions, session
affinity, cookie-based affinity, connection draining,
distributed serverless, event-driven architecture,
event bus, fan-out, idempotent consumers, dead-letter
queue, correlation IDs, data platform, Parquet lake,
rung, worked example per stage,
climb-when signal, cost per stage, ops burden,
when to stay put, no-server stack, first server,
incremental architecture (see `Stacks.md`),
static site hosting, landing page,
monolithic web app, CRUD SaaS, admin panels,
API-first backend, SPA + API, multi-tenant SaaS,
shared DB vs per-tenant DB, tenant isolation,
choosing architecture by stage and budget,
file-based CMS, content as files, JSON content
directory, item.json, one directory per item,
images beside the data, static site generator,
build script, generated data file, brands.js,
vanilla JavaScript, no framework, progressive
enhancement, shared navigation component,
client-side filtering, localStorage persistence,
image gallery with thumbnails, modal dialog,
catalog / inventory site, category and detail
pages,
mobile-friendly web app, responsive design,
mobile-first CSS, viewport meta tag, media queries,
fluid layout, touch target size, progressive web
app (PWA), web app manifest, service worker,
offline support, add to home screen, installable
web app, mobile performance, Core Web Vitals,
image optimization, lazy loading, device testing,
PWA vs native app

## 03_deployments — Cheap and Simple Deployments
keywords: Cloudflare, Cloudflare Registrar,
Cloudflare DNS, Cloudflare Pages, direct upload
deploy, GitHub-connected build, Wrangler,
wrangler pages deploy, --project-name,
--commit-dirty, npx, preview vs production
deployment, rollback, cache purge, cache busting,
versioned asset query string, build pipeline,
numbered build scripts, JSON validation step,
image optimization step, local dev server,
python http.server, no-cache headers for local
testing, preview deployments, custom domain,
free TLS certificate,
one-box deployment, cheap VPS, Hetzner,
DigitalOcean, EC2, Linux server setup, Ubuntu,
sudo user, SSH keys, disable password login, ufw
firewall, fail2ban, reverse proxy, Caddy, Caddyfile,
automatic HTTPS, ACME, automatic certificate
renewal, reverse_proxy directive, Caddy vs Nginx,
Nginx, systemd service, Let's Encrypt, certbot,
unattended upgrades, swap file, managed PaaS,
Render, Fly.io,
Railway, Heroku, serverless full-stack, Lambda,
API Gateway, Docker Compose in production, ECS,
Fargate, when you need Kubernetes,
micro-servers, micro-VMs, Firecracker, boot in
milliseconds, KVM, jailer, gVisor, Kata Containers,
V8 isolate, Cloudflare Workers, Durable Objects, D1,
KV, Google Cloud Run, scale to zero, min-instances,
concurrency per instance, cold start, warm start,
provisioned concurrency, lazy imports, connection
reuse across invocations, p99 latency,
Dockerfile, image layers, multi-stage build,
distroless, non-root USER, exec-form CMD, SIGTERM
handling, .dockerignore, image tags vs digests,
build cache, layer invalidation, dependency layer
ordering, BuildKit, buildx, cache mounts, build
secrets, cache-from / cache-to, multi-platform
build, deployment strategies, recreate, rolling
deploy, blue-green, canary, expand/contract
migration, feature flags, draining, rollback
artifact

## 04_network_storage_db — Networking, Storage, DBs
keywords: VPC, subnets, security groups, firewalls,
object storage, S3, GCS, Azure Blob, SQLite,
single-file database, embedded database, serverless
database, WAL mode, SQLite concurrency limits,
Litestream, when to use SQLite, SQLite to
PostgreSQL migration, PostgreSQL,
MySQL, managed database, self-hosted PostgreSQL,
same-server database, apt install postgresql,
psql, roles and privileges, pg_hba.conf,
localhost-only listen_addresses, connection string,
connection pooling, pg_dump, pgBackRest, nightly
backup cron, restore drill, caching, Redis, queues,
RabbitMQ, multi-region, cheap resilience

## 05_ops_cicd_security — CI/CD, Monitoring, Security
keywords: git-driven deployment, CI/CD pipeline,
GitHub Actions, GitLab CI, logging, metrics,
alerts, observability, HTTPS, secrets management,
least privilege, authentication, Firebase
Authentication, Firebase Auth SDK, ID token
verification, email/password sign-in, Google
sign-in, OAuth 2.0, OIDC, JWT, sessions vs tokens,
password reset, MFA, Auth0, Clerk, Supabase Auth,
authorization vs authentication, cost control,
budget guardrails,
storing secrets, environment variables, .env file,
never commit secrets, .gitignore for secrets,
secret store, secret manager, AWS Secrets Manager,
AWS Systems Manager Parameter Store, Google Secret
Manager, Azure Key Vault, HashiCorp Vault,
Cloudflare Workers secrets, GitHub Actions secrets,
systemd LoadCredential, Docker Compose secrets,
SOPS, age, encrypted secrets in git, secret
scanning, push protection, Gitleaks, leaked
credential rotation, IAM roles instead of keys,
short-lived credentials, least-privilege policy,
KMS, key management service, AWS KMS, Google Cloud
KMS, customer managed key (CMK), data encryption
key (DEK), key encryption key (KEK), envelope
encryption, encryption at rest, SSE-KMS, key
policy, grants, key rotation, key aliases,
cryptographic erasure, HSM, hardware security
module, AWS CloudHSM, Google Cloud HSM, FIPS 140-3,
FIPS 140-2 Level 3, NIST CMVP, tamper resistance,
key ceremony, BYOK,
security testing, vulnerability scanning, DAST,
SAST, OWASP ZAP, ZAP baseline scan, ZAP in CI,
OWASP Top 10, OWASP WSTG, OWASP ASVS, penetration
testing, authorized testing, AWS pentest policy,
bug bounty, dependency audit, npm audit,
pip-audit, Dependabot alerts, CodeQL, code
scanning, Trivy, container image scanning, Lynis,
server hardening audit, TLS configuration test,
security headers test, CSP, HSTS, SQL injection,
XSS, CSRF, input validation, fix-and-retest loop,
SOC 2, SOC 2 compliance, Trust Services Criteria,
TSC, security criterion, availability,
confidentiality, processing integrity, privacy,
common criteria (CC1-CC9), control, control
objective, evidence collection, audit trail,
encryption in transit, encryption at rest, TLS 1.2
minimum, HSTS enforcement, encrypted EBS volume,
RDS encryption, S3 default encryption, CMEK,
customer-managed key, encrypted backups, key
rotation policy, access control, role-based access
control, quarterly access review, offboarding,
MFA enforcement, SSO, audit logging, CloudTrail,
Cloud Audit Logs, log retention, AWS Config,
configuration drift, change management, pull
request approval, separation of duties, backup and
restore testing, disaster recovery, RTO, RPO,
incident response plan, NIST SP 800-61, vendor
management, subprocessors, shared responsibility
model, AWS Artifact, provider SOC 2 report,
security policies, risk assessment, security
awareness training, CIS Controls,
CI/CD pipeline stages, fail fast ordering, build
once deploy many, artifact promotion, dependency
caching in CI, matrix builds, path filters, OIDC
keyless deploy, pinning actions to a SHA,
automated testing, test pyramid, unit vs
integration vs end-to-end, smoke test after deploy,
regression test for every bug, flaky tests, pytest,
fixtures, parametrize, Playwright, auto-waiting,
trace viewer, config validation tests, migration
tests, fuzz testing, fuzzing, coverage-guided
fuzzing, AFL++, libFuzzer, OSS-Fuzz,
ClusterFuzzLite, property-based testing, Hypothesis,
shrinking, sanitizers, ASan, seed corpus,
dictionary, crash triage, red team, blue team,
purple team, adversary simulation, detection gap,
game day, tabletop exercise, MITRE ATT&CK, tactics
and techniques, T1078 valid accounts, T1190 exploit
public-facing application, authorized testing rules
of engagement

## 06_product_patterns — Patterns by Product Type
keywords: marketing/content site infra, catalog
site, inventory site, product detail page, quote
request form, landing page, email capture form,
name and email opt-in, autoresponder, drip
sequence, welcome sequence, double opt-in, lead
magnet, form endpoint, forms without a backend,
Web3Forms, api.web3forms.com/submit, public access
key, honeypot, spam protection, form validation,
success/error handling, AWeber, Formspree,
Cloudflare Pages Functions, Mailchimp,
Kit (formerly ConvertKit), MailerLite, Buttondown,
Brevo, GDPR/CAN-SPAM consent and unsubscribe,
transactional email, Amazon SES, AWS SES, SES
sandbox, request production access, sending quota,
sending rate, verified identity, domain
verification, Easy DKIM, BYODKIM, SPF record,
custom MAIL FROM domain, DMARC policy, MX record
for bounces, SMTP endpoint, SES SDK / boto3,
bounce handling, complaint handling, SNS
notifications, event publishing, suppression list,
deliverability, sender reputation, dedicated IP,
Google bulk sender guidelines, one-click
unsubscribe, spam rate threshold, transactional vs
marketing email, Postmark, Resend, SendGrid,
password reset email, receipt email,
small SaaS with auth and billing, admin panel,
API products, developer tools, internal
line-of-business apps, prototype infra to real
infra

## 07_playbooks — Playbooks and Recipes
keywords: deploy static site, domain + DNS + SSL +
CDN, Cloudflare Pages recipe, JSON folder to
deployed site in four commands, preview locally
before shipping, add a Web3Forms contact form,
provision and harden an Ubuntu server, Caddy in
front of an app, app + PostgreSQL on one box with
nightly backups, ship a tiny app on SQLite, landing
page to autoresponder recipe, add Firebase Auth to
a SPA, make an app mobile-friendly, monolithic SaaS
on a single VPS, SPA + API on PaaS, serverless
full-stack with auth and payments,
get secrets out of a repository, scan git history
for secrets, rotate leaked keys, envelope
encryption in 30 lines, encrypt data with AWS KMS,
encrypt data with Google Cloud KMS, pre-launch
security test pass, ZAP baseline scan in CI,
dependency audit before release, encrypt
everything and prove it, auditor evidence
screenshots, SOC 2 readiness sprint, minimum
viable policy set, turn on audit logging, first
access review, start the observation window,
production-readiness checklist

## 08_scaling_maturity — Growing Up Without Overkill
keywords: staging and preview environments,
infrastructure as code, Terraform, Pulumi,
Serverless Framework, policies, SSO, compliance,
sharding, read replicas, horizontal scaling,
anti-patterns, overengineering,
SOC 2 Type I vs Type II, observation window,
readiness assessment, gap analysis, choosing an
auditor, CPA firm, audit cost and timeline,
compliance automation platform, Vanta, Drata,
Secureframe, continuous control monitoring,
ISO 27001, SOC 2 vs ISO 27001, customer security
questionnaire, trust center

## 11_reliability_and_failure — How Systems Break
keywords: failure modes, typical types of failures,
single point of failure, redundancy, fake redundancy,
domain and certificate expiry as outages, cascading
failure, load shedding, circuit breaker, bulkhead,
headroom, graceful degradation, N-1 capacity, retry
storm, exponential backoff, jitter, retry budget,
retry at one layer, Retry-After, 429, cache stampede,
dog-pile, thundering herd, single flight, mutex on
miss, stale-while-revalidate, jittered TTL, cold
cache, hot partition, data skew, partition key
cardinality, key salting, celebrity key, replication
lag, read-your-own-writes, routing reads, RPO,
duplicate processing, at-least-once delivery,
exactly-once myth, idempotency, idempotency key,
unique constraint dedup, queue backlog, oldest
message age, backpressure, bounded queue, autoscale
on queue depth, poison message, dead-letter queue,
redelivery count, replay, split brain, quorum,
witness node, fencing, STONITH, leases, manual
promotion, chaos engineering, steady state
hypothesis, blast radius, game day, restore drill
note: no `Raw/` category folder — these pages rest on
captures already held elsewhere: the SRE Book
(`09_appendices`, `05_ops_cicd_security`), AWS
Well-Architected reliability (`08_scaling_maturity`),
RabbitMQ work queues (`04_network_storage_db`) and
the PostgreSQL standby/partitioning docs.

## 09_appendices — Reference Material
keywords: starter stacks by use case, reference
architectures, infra diagrams, further reading,
DevOps, SRE, cloud architecture courses, case
study, catalog inventory site, real-world
static site walkthrough, security toolbox,
secret store comparison, KMS/HSM options by cloud,
free vs paid security scanners, SOC 2 control map,
criterion to configuration mapping, inherited
controls from the cloud provider
