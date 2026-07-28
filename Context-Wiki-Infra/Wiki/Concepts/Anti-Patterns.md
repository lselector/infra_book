---
type: Concept
title: "Anti-Patterns"
description: "The expensive mistakes small teams reliably make, and the cheaper thing to do instead."
wikipedia: "https://en.wikipedia.org/wiki/Anti-pattern"
tags: [scaling, orientation]
timestamp: "2026-07-27T00:00:00Z"
---

# Anti-Patterns

Recurring choices that cost far more than they return at
small scale.

| Anti-pattern | Cheaper answer |
|---|---|
| Kubernetes for one app | [[One-Box Deployment]] or [[Managed PaaS]] |
| Microservices before product-market fit | [[Monolithic Web App]] |
| Managed database for ten users | [[SQLite]], then [[PostgreSQL]] on the same box |
| Building [[Authentication]] yourself | [[Firebase Authentication]] |
| Multi-region before one region is stable | [[Database Backups]] with a tested restore |
| A database when files would do | [[File-Based CMS]] |
| [[Infrastructure as Code]] for one server | click it, write it down |
| Editing files on the production server | [[Git-Driven Deployment]] |
| Secrets in the repository | [[Secrets Management]] |
| Caching before indexing | fix the query first |

## The pattern behind the patterns

Each is adopting the operational model of a much larger
organisation before having its problems. The cost is
rarely the tool's price — it is the ongoing attention it
demands, taken from building the product.

## The counter-question

Before adding a component, ask: **what signal told me I
need this?** If the answer is a blog post, a conference
talk, or a future you are imagining, wait. See
[[The Ladder]].

## The honourable exceptions

Security and backups. Do those early, because retrofitting
them after an incident is the one thing that really is
more expensive later.

## Related

[[The Ladder]] · [[Cost Control]] ·
[[Monolithic Web App]] · [[Kubernetes]] ·
[[Infrastructure as Code]] · [[Failure Modes]] ·
[[Split Brain]] · [[Cascading Failure]] ·
[[Deployment Strategies]]

## Sources

- [[martinfowler-monolith-first]] ·
  [[martinfowler-microservice-premium]] ·
  [[kubernetes-overview]] · [[martinfowler-feature-toggles]]
