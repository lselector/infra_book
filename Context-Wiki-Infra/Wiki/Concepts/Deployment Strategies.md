---
type: Concept
title: "Deployment Strategies"
description: "Recreate, rolling, blue-green and canary - what each costs, and the one that suits one server."
wikipedia: "https://en.wikipedia.org/wiki/Software_deployment"
tags: [deployments, ops-and-security]
timestamp: "2026-07-28T00:00:00Z"
---

# Deployment Strategies

How new code replaces old code. The choice determines
whether users see downtime, how fast you can undo a bad
release, and how much infrastructure you pay for.

## The four, with the trade

| Strategy | Downtime | Extra capacity | Rollback |
|---|---|---|---|
| **Recreate** — stop, start | Seconds to a minute | None | Redeploy previous |
| **Rolling** — replace instances one at a time | None | 1 extra instance | Roll forward, slowly |
| **Blue-green** — two full environments, switch traffic | None | 2× during deploy | Instant: switch back |
| **Canary** — 5% of traffic to the new version, then more | None | Small | Instant: route back |

## Which one you should use

**One server, small product: recreate.** A 3-second
restart at 4am is not worth building around, and every
alternative adds a moving part. Add `restart:
unless-stopped` in [[Docker Compose]], drain gracefully,
and be honest that this is fine.

**Static sites get blue-green for free.** Every
[[Cloudflare Pages]] deploy is immutable, gets its own
preview URL, and production is a pointer you can move
back in one click. That is blue-green with no second
environment to pay for — the cheapest rollback story in
this wiki.

**Rolling** is the default on [[Kubernetes]],
[[AWS Fargate]] and [[Google Cloud Run]], and it is a
reasonable default — provided your app can run two
versions at once, which is a database question (below).

**Canary** is worth it when a bad release is expensive
and traffic is high enough that 5% is a meaningful
sample. Below that volume the canary tells you nothing
and you have added routing complexity for a rounding
error.

## The database is the hard part

Every zero-downtime strategy runs old and new code
simultaneously against **one database**. So schema
changes must be backwards-compatible, in two deploys:

1. **Expand.** Add the new column as nullable; write to
   both old and new; deploy. Old code ignores it.
2. **Contract.** Once every instance runs the new code
   and data is backfilled, stop writing the old column;
   deploy; then drop it.

Renaming a column in one migration is the classic way to
take a site down during a "zero-downtime" rolling deploy.

## Rollback is the feature

A deployment strategy is really a rollback strategy. Make
sure you can answer, right now:

- **What exactly do I roll back to?** An immutable
  artifact — an image digest ([[Container Images]]), a
  Pages deployment ID, a git tag. Not "rebuild from
  main".
- **How long does it take?** If the answer is "rebuild
  and redeploy, 6 minutes", that is your recovery time.
- **Is the migration reversible?** Often not — which is
  why expand/contract matters more than the deploy
  mechanism.

## Feature flags: deploy without releasing

Ship the code disabled, turn it on for yourself, then for
10% of users, then everyone — no deploy involved.
It separates the risky moment from the deploy, makes the
"rollback" a config change, and is the cheapest form of
canary for a small team. The cost is dead code paths and
flags nobody removes; delete them once the feature is
permanent.

## Watch out for

- **Health checks that lie.** If the new instance reports
  healthy before it can serve, a rolling deploy happily
  replaces every healthy instance with a broken one.
- **Draining.** In-flight requests need to finish; send
  `SIGTERM`, stop accepting new connections, wait, then
  exit ([[Container Images]] on exec-form `CMD`).
- **Sessions in process memory** break every strategy
  above ([[Sticky Sessions]] explains why, and why
  external session state is the fix).
- **Deploying and migrating in the same step** with no
  way to separate them, so a failed migration is also a
  failed deploy.

## Related

[[Continuous Integration and Delivery]] ·
[[Git-Driven Deployment]] · [[Deployment Environments]] ·
[[Container Images]] · [[Docker Compose]] ·
[[Cloudflare Pages]] · [[Kubernetes]] ·
[[Google Cloud Run]] · [[Sticky Sessions]] ·
[[Automated Testing]] · [[Failure Modes]] ·
[[Incident Response]]

## Sources

- [[github-actions-deployment]] · [[github-environments]]
  · [[martinfowler-feature-toggles]] ·
  [[cloudflare-pages-preview-deployments]] ·
  [[kubernetes-overview]] · [[docker-compose-production]]
