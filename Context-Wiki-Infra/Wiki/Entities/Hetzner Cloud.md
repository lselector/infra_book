---
type: Vendor
title: "Hetzner Cloud"
description: "European VPS provider with the best price-to-resource ratio in this book."
wikipedia: "https://en.wikipedia.org/wiki/Hetzner"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Hetzner Cloud

Cloud VMs from roughly EUR 4/month for a instance that
comfortably runs an app, a database and a reverse proxy.

## Why it appears here

Price per unit of RAM and CPU is markedly better than the
US hyperscalers, and generous traffic allowances are
included rather than metered. For [[One-Box Deployment]]
it is the default recommendation.

## Practical notes

- Data centres in Germany, Finland and the US.
- Snapshots and backups are cheap add-ons — enable
  backups, they are not a substitute for
  [[Database Backups]] but they are a fast rollback.
- Cloud firewalls available in addition to [[UFW]].

## Watch out for

- Account verification can take a little time on first
  signup; do not discover this on launch day.
- Fewer managed services than AWS or Google Cloud. That
  is the trade: you are buying a machine, not a platform.

## Related

[[One-Box Deployment]] · [[DigitalOcean]] ·
[[Ubuntu Server]] · [[Cost Control]] ·
[[VPS Instead of Hyperscaler]] · [[Kamal]] · [[Coolify]]

## Sources

- [[hetzner-create-a-server]]
