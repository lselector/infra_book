---
type: Concept
title: "Managed PaaS"
description: "Push code, get a running service - paying money to not own a machine."
wikipedia: "https://en.wikipedia.org/wiki/Platform_as_a_service"
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

## The cheaper version of the same idea

Run the platform yourself on a rented box: [[Coolify]]
gives you the dashboard and push-to-deploy, [[Kamal]]
gives you just the deploy. You keep the ergonomics and
pay VPS prices — and inherit the operating. See
[[Self-Hosted PaaS]] and [[VPS Instead of Hyperscaler]].

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
[[Serverless Architecture]] · [[Cost Control]] ·
[[Self-Hosted PaaS]] · [[VPS Instead of Hyperscaler]]

## Sources

- [[flyio-getting-started-launch]] ·
  [[render-web-services]] · [[railway-quick-start]]
