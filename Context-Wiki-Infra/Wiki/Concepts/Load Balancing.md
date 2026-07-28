---
type: Concept
title: "Load Balancing"
description: "Spreading requests across several servers - and why a small project usually should not have one yet."
wikipedia: "https://en.wikipedia.org/wiki/Load_balancing_(computing)"
tags: [foundations, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Load Balancing

A load balancer accepts requests and distributes them
across a pool of backends, removing unhealthy ones from
rotation.

## What it buys you

- **Horizontal scale** — more backends behind one address.
- **Availability** — one dead backend stops receiving
  traffic instead of returning errors.
- **A TLS termination point** — often the same box.

## Why it matters here

Mostly as a thing to *defer*. A single well-configured box
behind a [[Content Delivery Network]] serves a great deal
of traffic. Introducing a load balancer means at least two
app servers, which means shared session state, shared
uploads, and a database that is no longer on the same
machine — three problems you did not have before.

Add one when a single instance genuinely cannot serve
demand, or when you need zero-downtime deploys badly
enough to pay for the complexity.

## Watch out for

- Sticky sessions are a workaround, not a design. Keep
  application servers stateless instead.
- Health checks that only test the port, not the app, will
  happily route traffic into a broken process.

## Related

[[Reverse Proxy]] · [[One-Box Deployment]] ·
[[Read Replicas]] · [[The Ladder]] ·
[[Single Point of Failure]] · [[Cascading Failure]] ·
[[Sticky Sessions]] · [[Failure Modes]]

## Sources

- [[cloudflare-what-is-load-balancing]] ·
  [[aws-well-architected-reliability]]
