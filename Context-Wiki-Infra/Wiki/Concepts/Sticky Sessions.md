---
type: Concept
title: "Sticky Sessions"
description: "Pinning a user to one backend instance - necessary for live connections, a crutch for everything else."
wikipedia: "https://en.wikipedia.org/wiki/Load_balancing_(computing)"
tags: [architectures, scaling, networking]
timestamp: "2026-07-28T00:00:00Z"
---

# Sticky Sessions

Also called *session affinity*. The load balancer sends
every request from one client to the same backend
instance, usually by setting its own cookie or hashing
the source address.

## Why it exists

The moment you run two app instances behind
[[Load Balancing]], anything a request left in the
memory of instance A is invisible to instance B. Logins
evaporate, shopping carts empty, uploads land in halves.

Stickiness makes that invisible: the same user keeps
hitting the same box, so in-memory state keeps working.

## The two very different reasons to use it

**1. Because your app is stateful — a crutch.** The real
fix is to put the state somewhere both instances can
see: sessions in [[Redis]] or [[PostgreSQL]], uploads in
[[Object Storage]], signed tokens
([[JSON Web Token]]) instead of server-side sessions.
Then any instance can serve any request, and a dead box
costs nobody their cart.

**2. Because the connection itself is stateful —
legitimate.** A WebSocket, an SSE stream or a long poll
is a live TCP connection to one process. There is
nothing to externalise; the connection *is* the state.
Affinity here is correct, not lazy.

## What it costs you

- **Uneven load.** Long-lived connections pin traffic;
  one instance ends up hot while a fresh one idles.
- **Deploys hurt.** Restarting an instance disconnects
  everyone pinned to it. Plan for reconnect-with-backoff
  on the client and connection draining on the balancer.
- **Autoscaling gets worse.** Scaling out helps only new
  sessions, so a spike takes longer to absorb.
- **A failed instance is a user-visible failure**, rather
  than a retried request.

## Doing it properly

- Externalise application state anyway, even when you
  need affinity for the socket. Then stickiness is an
  optimisation, not a correctness requirement.
- Prefer cookie-based affinity over IP hashing — mobile
  clients change IP constantly, and corporate NATs put
  thousands of users behind one address.
- Set a short affinity TTL, and enable connection
  draining so deploys empty an instance before it stops.
- Publish state changes over [[Message Queues]] or Redis
  pub/sub so any instance can push to any client.

## Related

[[Load Balancing]] · [[Read Replicas]] · [[Redis]] ·
[[Container Orchestration]] · [[Deployment Environments]] ·
[[Anti-Patterns]] · [[Event-Driven Architecture]] ·
[[Deployment Strategies]] · [[Cloudflare Workers]] ·
[[Streaming Responses]]

## Sources

- Upstream documentation: AWS Application Load Balancer
  target-group stickiness, and the Nginx `ip_hash` /
  `sticky` directives. Not part of the downloaded `Raw/`
  corpus — no capture to cite yet.
