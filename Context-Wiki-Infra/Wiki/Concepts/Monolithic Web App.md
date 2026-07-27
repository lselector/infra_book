---
type: Concept
title: "Monolithic Web App"
description: "One deployable process serving HTML and handling writes - the right default for a small team."
tags: [architectures]
timestamp: "2026-07-27T00:00:00Z"
---

# Monolithic Web App

A single application process that renders pages, handles
form posts, and talks to the database. One repository, one
deploy, one thing to restart.

## Why it matters here

- It is rung 5 of [[The Ladder]] and the correct shape for
  almost every small SaaS, admin panel and internal tool.
- Debugging is tractable: one log stream, one stack trace,
  no distributed tracing required.
- It deploys as `git pull && systemctl restart`, which is
  a complete and honest deployment strategy at this size.

## The standard build

[[Caddy]] in front for TLS and static files,
[[FastAPI]] or [[Django]] behind it under [[systemd]],
[[SQLite]] or [[PostgreSQL]] on the same box.

## When to split

Later than you think. Martin Fowler's argument for
monolith-first applies with force to teams under about ten
people: you cannot draw good service boundaries before you
understand the domain, and wrong boundaries are far more
expensive than a large module.

## Related

[[One-Box Deployment]] · [[Reverse Proxy]] ·
[[Single Page Application and API]] ·
[[Multi-Tenant SaaS]] · [[The Ladder]]

## Sources

- [[martinfowler-monolith-first]] ·
  [[martinfowler-microservice-premium]] ·
  [[django-deployment-checklist]] ·
  [[fastapi-deployment-concepts]]
