---
type: Concept
title: "The Ladder"
description: "Fourteen example stacks in increasing complexity, each adding exactly one capability to the one below."
tags: [architectures, orientation]
timestamp: "2026-07-27T00:00:00Z"
---

# The Ladder

The organising idea of this wiki: infrastructure choices
form a ladder, and you should climb it one rung at a time
in response to a real signal — never in anticipation.

The full worked index, with costs and per-rung sources,
is [[Stacks]].

## The rungs

1. Static site — [[Cloudflare Pages]]
2. + build script — [[File-Based CMS]]
3. + [[Forms Without a Backend]] — [[Web3Forms]]
4. + [[Landing Page Email Capture]] — [[AWeber]]
5. + a server — [[One-Box Deployment]], [[Caddy]],
   [[FastAPI]]
6. + a database — [[SQLite]] or [[PostgreSQL]]
7. + [[Transactional Email]] — [[Amazon SES]]
8. + [[Authentication]] — [[Firebase Authentication]]
9. + payments and hygiene — [[Stripe]],
   [[Secrets Management]], [[Continuous Integration and Delivery]]
10. + [[SOC 2]], [[Read Replicas]],
    [[Infrastructure as Code]]

Then four specialist rungs, taken singly rather than in
order, when a specific problem names one:

11. + [[Container Orchestration]] — several services,
    scheduled across machines ([[Docker]],
    [[AWS Fargate]], [[Kubernetes]])
12. + realtime and [[Sticky Sessions]] — WebSockets,
    affinity, [[Redis]] for shared state
13. + [[Event-Driven Architecture]] — distributed
    serverless, queues, [[AWS Lambda]], dead-letter
    queues
14. + [[Distributed Data Processing]] — a Parquet lake
    on [[Object Storage]], [[Apache Spark]] or
    [[Databricks]]

## The two observations worth carrying

- **Rungs 1 to 4 have no server at all.** Content,
  catalog, lead capture and email nurture are all
  achievable with nothing to patch and nothing to page you.
- **The expensive jump is 4 to 5**, where you take on a
  machine. Everything above rung 5 is incremental by
  comparison. Check hard whether a rung-3 or rung-4 answer
  really is impossible before climbing.
- **Rungs 11 to 14 are not a sequence.** Most products
  that reach them need exactly one — the one their
  problem names — and almost none need all four.

## Related

[[Stacks]] · [[Cloud Service Models]] ·
[[One-Box Deployment]] · [[Cost Control]] ·
[[Container Orchestration]] · [[Sticky Sessions]] ·
[[Event-Driven Architecture]] ·
[[Distributed Data Processing]] · [[Failure Modes]] ·
[[Micro-VMs]] · [[Deployment Strategies]]
