---
type: Tool
title: "Redis"
description: "In-memory data store - cache, session store, rate limiter and simple queue."
wikipedia: "https://en.wikipedia.org/wiki/Redis"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Redis

An in-memory key-value store with useful data structures,
optional persistence, and microsecond latency.

## What it is used for here

- **[[Caching]]** shared across processes, which an
  in-process dictionary cannot do.
- **Sessions**, so any app instance can serve any user.
- **Rate limiting** — atomic counters with expiry.
- **A simple queue** for [[Message Queues]] work, with a
  worker library on top.

## When to add it

Not on day one. A single-process app can cache in memory,
and a database table is an acceptable queue at low volume.
Redis earns its place when there is more than one process,
or when the cache must survive a restart.

## Watch out for

- **It is memory.** Set `maxmemory` and an eviction
  policy, or it will consume the box.
- Default persistence settings may not match your
  expectation — decide whether you are willing to lose the
  contents on restart.
- Never expose it publicly. Bind to localhost; it has
  historically been a favourite of automated scanners.

## Related

[[Caching]] · [[Message Queues]] · [[RabbitMQ]] ·
[[Linux Server Hardening]] · [[Cache Stampede]] ·
[[Hot Partition]] · [[Queue Backlog]]

## Sources

- [[redis-data-store-get-started]]
