---
type: Dashboard
title: "The Ladder - Infra Stacks in Increasing Complexity"
description: "Ten example stacks, each adding one capability, with cost, ops burden and the signal to climb."
tags: [ladder, stacks, orientation, architectures]
timestamp: "2026-07-27T00:00:00Z"
---

# The Ladder — Infra Stacks in Increasing Complexity

An example-based index. Ten rungs, each a working
stack you could ship this week. Every rung adds
**one** capability to the one below it.

Read it two ways:

* **Bottom-up** — start at rung 1 and climb only when
  a rung's "climb when" signal actually fires.
* **Top-down** — find the rung that matches what you
  are building, then read everything below it, because
  those pieces are still in your stack.

The golden rule: **climb one rung at a time, and only
in response to a real signal.** Every rung you skip is
complexity you pay for before you need it.

Costs are rough monthly figures for a small project in
2026, ignoring free-tier promotions.

---

## Rung 1 — Static site

**Example:** a five-page marketing site, a résumé, a
docs site.

| | |
|---|---|
| **Stack** | [[Cloudflare Pages]] + [[Cloudflare Registrar]] + [[Cloudflare DNS]] |
| **You write** | HTML, CSS, a little JS |
| **Deploy** | `wrangler pages deploy ./site` — or connect the GitHub repo |
| **State** | none |
| **Cost** | ~$0 (domain ~$10/yr) |
| **Ops burden** | zero — no server, no certificates, no patching |

TLS, CDN, and HTTP/3 come free and automatic. There is
no server to be hacked or to fall over.

**Climb when:** you need to *generate* pages from data
rather than hand-write them.

*Chapters 7, 15–17, 52–53 · Raw: `03_deployments/cloudflare-pages-*`*

---

## Rung 2 — Static site built from data files

**Example:** a vehicle inventory, a product catalog,
a photo portfolio. See Appendix D.

| | |
|---|---|
| **Adds** | a build step and a file-based CMS |
| **Stack** | rung 1 + a folder of `item.json` + images + a Python build script |
| **Deploy** | `s1_validate.py → s2_images.py → s3_build.py → s4_deploy.py` |
| **State** | JSON files in Git |
| **Cost** | ~$0 |
| **Ops burden** | zero |

Still no database and no server. Content edits are Git
commits, which means version history and rollback for
free.

**Climb when:** non-technical people must edit content,
or the data changes many times a day.

*Chapters 8, 18, 44, 54 · Raw: `02_architectures/`, `09_appendices/`*

---

## Rung 3 — Static site + third-party form

**Example:** the catalog above, plus "Request a quote".

| | |
|---|---|
| **Adds** | inbound messages, without a backend |
| **Stack** | rung 2 + [[Web3Forms]] (public access key, honeypot) |
| **State** | submissions land in your inbox |
| **Cost** | ~$0 |
| **Ops burden** | zero |

The first taste of "dynamic" behaviour with no server
at all. A `POST` to someone else's API.

**Climb when:** you need to *do* something with a
submission beyond reading it — store it, act on it,
reply automatically.

*Chapters 45, 56 · Raw: `06_product_patterns/web3forms-*`*

---

## Rung 4 — Static site + email capture + autoresponder

**Example:** a landing page that collects name and
email and starts a welcome sequence.

| | |
|---|---|
| **Adds** | a mailing list and marketing automation |
| **Stack** | rung 3 + [[AWeber]] / Mailchimp / Kit, double opt-in, drip sequence |
| **State** | lives in the email provider |
| **Cost** | $0–20 |
| **Ops burden** | near zero |

Note this is *marketing* email — bulk, scheduled,
consent-driven. It is a different job from the
transactional email at rung 7.

**Climb when:** you need logged-in users, or data your
provider cannot model.

*Chapters 46, 62 · Raw: `06_product_patterns/aweber-*`, `mailchimp-*`*

---

## Rung 5 — One box: Caddy + FastAPI

**Example:** a CRUD app, an internal tool, an API with
a handful of endpoints.

| | |
|---|---|
| **Adds** | your own server-side code |
| **Stack** | Hetzner/DigitalOcean VPS + Ubuntu + [[Caddy]] reverse proxy + [[FastAPI]] under systemd |
| **Deploy** | `git pull && systemctl restart app` |
| **State** | in memory or flat files |
| **Cost** | $5–12 |
| **Ops burden** | **first real jump** — you now patch a machine |

Caddy earns its place here: two lines of Caddyfile and
HTTPS certificates are issued and renewed
automatically. This is the rung where you inherit SSH
keys, a firewall, unattended upgrades, and backups.

**Climb when:** you need data to survive a restart, or
to query it.

*Chapters 10, 19–21, 57–59 · Raw: `03_deployments/caddy-*`, `ubuntu-*`, `07_playbooks/fastapi-*`*

---

## Rung 6 — Add a database

**Example:** the app above, with users, orders, or
records that must persist.

| | |
|---|---|
| **Adds** | durable, queryable state |
| **Stack** | rung 5 + [[SQLite]] (one file) — or [[PostgreSQL]] on the same box |
| **Backups** | nightly `pg_dump` / file copy to object storage, plus a restore drill |
| **Cost** | $5–12 (same box) |
| **Ops burden** | +backups, +restore testing, +migrations |

Start with SQLite. It is a single file, needs no
server, and comfortably handles a read-heavy app with
modest write traffic. Move to PostgreSQL when you need
concurrent writers, multiple app servers, or types and
extensions SQLite lacks.

**Climb when:** you must send email your provider's
marketing tool cannot — receipts, password resets,
notifications.

*Chapters 28–30, 60–61 · Raw: `04_network_storage_db/sqlite-*`, `postgresql-*`*

---

## Rung 7 — Add transactional email

**Example:** password resets, receipts, "your order
shipped", alerts.

| | |
|---|---|
| **Adds** | outbound email your app controls |
| **Stack** | rung 6 + [[Amazon SES]] (or Postmark / Resend) |
| **Setup** | verify the domain → publish DKIM + SPF records in Cloudflare DNS → request production access to leave the sandbox → send via SMTP or SDK → route bounces and complaints to SNS |
| **Cost** | SES ~$0.10 per 1,000 emails; Postmark/Resend ~10–15× that |
| **Ops burden** | +deliverability: DMARC, bounce handling, reputation |

SES is by far the cheapest at volume, and the fiddliest
to set up — the sandbox, the domain verification, and
the bounce handling are all real work. Postmark and
Resend cost more per email and remove most of that
work. Below a few thousand emails a month the price
difference is noise; pick on setup time, not cost.

Whatever you choose, **you** own deliverability: publish
SPF, DKIM, and DMARC, and process bounces and
complaints or your reputation degrades.

**Climb when:** users need accounts.

*Chapter 47, recipe 63 · Raw: `06_product_patterns/aws-ses-*`, `google-bulk-sender-guidelines.md`*

---

## Rung 8 — Add authentication

**Example:** a real SaaS with per-user data.

| | |
|---|---|
| **Adds** | identity |
| **Stack** | rung 7 + [[Firebase Authentication]] (or Auth0 / Clerk / Supabase Auth) |
| **Backend** | verify the ID token on every request; store your own `users` row keyed by the provider's UID |
| **Cost** | $0–25 |
| **Ops burden** | +token verification, +session handling, +account recovery |

Do not roll your own. Password hashing, reset flows,
MFA, and OAuth are a large surface area to get wrong.

**Climb when:** you need to charge money, or the
security bar rises (customers start sending
questionnaires).

*Chapters 39, 64 · Raw: `05_ops_cicd_security/firebase-auth-*`*

---

## Rung 9 — Add payments, secrets discipline, and CI/CD

**Example:** a paid SaaS with a handful of employees.

| | |
|---|---|
| **Adds** | revenue, and the operational hygiene that has to come with it |
| **Stack** | rung 8 + [[Stripe]] Checkout/Billing + a secret manager + GitHub Actions + [[AWS KMS]] for data you must encrypt yourself |
| **Also** | staging environment, monitoring and alerts, audit logging, nightly restore-tested backups |
| **Cost** | $30–150 |
| **Ops burden** | +change management, +on-call of a sort |

This is where secrets move out of `.env` files on the
box and into a managed store, and where deploys become
reviewed pull requests rather than `git pull` over SSH.

**Climb when:** enterprise customers ask for a SOC 2
report, or a single box can no longer carry the load.

*Chapters 33–38, 42, 48, 65–67 · Raw: `05_ops_cicd_security/`*

---

## Rung 10 — Compliance and scale

**Example:** a SaaS selling to companies that audit
their vendors.

| | |
|---|---|
| **Adds** | provable controls, and horizontal headroom |
| **Stack** | rung 9 + managed PostgreSQL with read replicas + multiple app instances behind a load balancer + IaC + [[SOC 2]] evidence collection |
| **Also** | access reviews, policies, incident response plan, vendor management, an observation window and an auditor |
| **Cost** | $200–1,000+ (plus $10–40k for the audit itself) |
| **Ops burden** | high — this is a job, not a side task |

Most projects never need this rung, and the ones that
do usually reach it because a *customer* asked, not
because of load.

**Climb when:** you genuinely cannot serve demand, or a
contract requires it.

*Chapters 41, 77–78, recipe 72 · Raw: `05_ops_cicd_security/`, `08_scaling_maturity/`*

---

## The whole ladder at a glance

| # | Stack | Adds | ~$/mo | Ops |
|---|---|---|---|---|
| 1 | Cloudflare Pages | a website | 0 | none |
| 2 | + build script | generated pages | 0 | none |
| 3 | + Web3Forms | inbound messages | 0 | none |
| 4 | + autoresponder | a mailing list | 0–20 | none |
| 5 | + VPS, Caddy, FastAPI | your own code | 5–12 | a machine |
| 6 | + SQLite / PostgreSQL | durable state | 5–12 | backups |
| 7 | + Amazon SES | outbound email | +$0.10/1k | deliverability |
| 8 | + Firebase Auth | user accounts | 0–25 | tokens |
| 9 | + Stripe, secrets, CI/CD | revenue + hygiene | 30–150 | change mgmt |
| 10 | + replicas, IaC, SOC 2 | proof and scale | 200–1,000+ | a real job |

## Two things worth noticing

**Rungs 1–4 have no server.** You can get a real
business — content, catalog, lead capture, email
nurture — with nothing to patch and nothing to page
you at 3am. A surprising number of projects should
stop here permanently.

**The jump from 4 to 5 is the expensive one.** It is
not the money; it is that you have taken on a machine.
Everything above rung 5 is incremental by comparison.
Before you climb it, check whether a rung-3 or rung-4
answer really is impossible.

## See also

* [[Topics]] — the keyword plan behind these rungs.
* `myprompts/TOC_infra.md` — chapter 6 narrates this
  ladder; the per-rung chapter numbers are cited above.
* `Raw/sources.md` — the source document for every
  technology named here.

---

Created: 2026-07-27
Last updated: 2026-07-27
