---
type: Concept
title: "Managed PaaS"
description: "Push code, get a running service - paying money to not own a machine."
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Managed PaaS

The platform builds your repository, runs the process,
terminates TLS, and hands you logs and metrics. You never
see the operating system.

## Why it matters here

- It skips the whole of [[Linux Server Hardening]],
  [[Unattended Upgrades]] and [[systemd]]. For a solo
  developer that is real time saved every month.
- Preview environments and rollbacks come built in, which
  otherwise means work — see [[Deployment Environments]].
- Cost is the trade: $7-25 per service where a VPS running
  three services costs $6 total.

## The options in this wiki

[[Fly.io]] (deploys close to users, good for global
latency), [[Render]] (conventional, predictable),
[[Railway]] (fastest to first deploy).

## Watch out for

- Free tiers that sleep. A cold start on a marketing site
  is a bounced visitor.
- Egress and build-minute charges, which are where the
  bill surprises people.
- Managed databases on the same platform are convenient
  and considerably more expensive than the same database
  on your own box.

## Related

[[Cloud Service Models]] · [[One-Box Deployment]] ·
[[Serverless Architecture]] · [[Cost Control]]

## Sources

- [[flyio-getting-started-launch]] ·
  [[render-web-services]] · [[railway-quick-start]]
