---
type: Tool
title: "Node.js"
description: "JavaScript on the server - one language across the stack, and an event loop you must not block."
wikipedia: "https://en.wikipedia.org/wiki/Node.js"
tags: [architectures, deployments, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# Node.js

A JavaScript runtime built on V8. It is the server half
of the [[React]] world: the same language, and often the
same code, on both sides of the wire.

## The operational shape

Node runs your app in **one thread**, driving an event
loop. I/O — database calls, HTTP requests, file reads —
is asynchronous and cheap, so a single process handles
thousands of concurrent connections happily.

The corollary is the rule that matters: **never block
the event loop.** A synchronous loop over a large array,
a `JSON.parse` of 50 MB, a bcrypt round with too high a
cost factor — while that runs, *every* request is
stalled. Offload CPU work to a worker thread, a queue
([[Event-Driven Architecture]]), or a different service.

## Deploying it

- Run one process per core (`node --run`, PM2 cluster,
  or just N containers) behind [[Caddy]] or
  [[Nginx]] — see [[Reverse Proxy]].
- Supervise with [[systemd]] or a container restart
  policy; a crashed process must come back.
- `npm ci` from a committed `package-lock.json` in the
  build; never `npm install` in production.
- Configuration in the environment
  ([[Twelve-Factor App]]), never in the image.
- Health endpoint for the load balancer, and graceful
  shutdown on `SIGTERM` so deploys drain connections.

## What it is genuinely good at

Realtime and I/O-heavy work: WebSockets, chat, live
dashboards, API gateways, streaming proxies, and
[[Server-Side Rendering]] of a React app — the one job
only a JS runtime can do.

## Watch out for

- **Dependency surface.** A small app pulls hundreds of
  transitive packages. `npm audit`, [[Dependabot]], and
  lockfile discipline are not optional
  ([[Dependency Auditing]]).
- **CPU-bound work.** See above. This is the failure
  mode.
- **Version churn.** Track an LTS release and pin it in
  the image and in CI.
- **Memory.** The default heap is smaller than you
  think; set `--max-old-space-size` deliberately in
  containers.

## Related

[[React]] · [[Next.js]] · [[Express]] ·
[[Server-Side Rendering]] · [[FastAPI]] ·
[[Reverse Proxy]] · [[Twelve-Factor App]] ·
[[Container Orchestration]] · [[Sticky Sessions]] ·
[[Vercel AI SDK]]

## Sources

- Upstream documentation: <https://nodejs.org/docs/latest/api/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
