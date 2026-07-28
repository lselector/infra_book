---
type: Concept
title: "Cold Starts"
description: "The first request after idle, and why it is slow - what the platform contributes, and what your code does."
wikipedia: "https://en.wikipedia.org/wiki/Cold_start_(computing)"
tags: [deployments, performance, serverless]
timestamp: "2026-07-28T00:00:00Z"
---

# Cold Starts

The latency added when a request arrives and no instance
is running: the platform has to create one, load your
code, and initialise it before any work happens. The
price of scale-to-zero.

## The four parts, and who owns them

```text
[ platform boots the sandbox ]  5-200 ms   theirs
[ runtime starts             ]  10-400 ms  language
[ your init code runs        ]  0-5000 ms  YOURS
[ first request handled      ]
```

The part people optimise is the first; the part that
usually dominates is the third. A Python function that
imports pandas, reads a config file and opens a database
connection at import time can spend three seconds before
it ever sees the request — while the platform's
contribution was 150ms.

## Reducing your own share

- **Import lazily.** Move heavyweight imports inside the
  handler if only some paths need them.
- **Do not do network I/O at module scope.** Fetching
  secrets or config on every cold start is both slow and
  a hard dependency at the worst moment.
- **Reuse across invocations.** Connections and clients
  created *outside* the handler survive between warm
  invocations. Create them lazily on first use, not at
  import.
- **Ship less.** Package size affects load time; prune
  dev dependencies, use multi-stage builds
  ([[Container Images]]).
- **Choose the runtime knowingly.** JS and Go start fast;
  JVM and heavy Python stacks do not. Compiled
  [[Rust]] and [[WebAssembly]] are at the fast end.

## Reducing the platform's share

- **Edge runtimes** ([[Cloudflare Workers]]) start V8
  isolates in single-digit milliseconds — effectively no
  cold start, at the cost of a restricted runtime.
- **Micro-VM platforms** ([[Micro-VMs]], [[Fly.io]],
  [[AWS Lambda]]) boot in ~100ms.
- **Provisioned concurrency / min instances** keeps N
  instances warm. It works, and it deletes the reason you
  went serverless: you are now paying at idle.
- **A minimum of one instance** on [[Google Cloud Run]]
  or a [[Managed PaaS]] costs a few dollars a month and
  makes the problem vanish.

## When it does not matter

- Background jobs, webhooks, cron, queue consumers — no
  human is waiting.
- Low-traffic internal tools.
- Anything already behind a
  [[Content Delivery Network]] for its HTML and assets,
  where the slow path is a small fraction of requests.

## When it does

Interactive, user-facing, low-traffic — the worst
combination, because low traffic guarantees the instance
is always cold and a human is always waiting. That is the
case where a $6 VPS running one process
([[One-Box Deployment]]) beats serverless on both latency
and cost, and it is more common for small products than
the serverless marketing suggests.

## Watch out for

**Cold starts hide in your p99, not your average.** If
1% of requests take 3 seconds and the rest take 40ms, the
mean looks excellent and a real fraction of users have a
bad time. Measure percentiles
([[Service Level Objectives]]).

**Scale-up is repeated cold start.** A traffic spike
creates many new instances at once, each paying the full
cost, exactly when the system is busiest.

## Related

[[Micro-VMs]] · [[Serverless Architecture]] ·
[[Cloudflare Workers]] · [[Google Cloud Run]] ·
[[AWS Lambda]] · [[Fly.io]] · [[Managed PaaS]] ·
[[Connection Pooling]] · [[Container Images]] ·
[[Service Level Objectives]] · [[Core Web Vitals]] ·
[[Cost Control]]

## Sources

- [[aws-what-is-serverless]] · [[aws-lambda-welcome]] ·
  [[cloudflare-pages-functions]] · [[flyio-launch]] ·
  [[render-web-services]]
