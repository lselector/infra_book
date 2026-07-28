---
type: Concept
title: "Caching"
description: "Keeping expensive answers around - and the two hard problems that come with it."
wikipedia: "https://en.wikipedia.org/wiki/Cache_(computing)"
tags: [storage-and-databases, performance]
timestamp: "2026-07-27T00:00:00Z"
---

# Caching

Store the result of expensive work so the next request
does not repeat it.

## The layers available, cheapest first

1. **HTTP caching** at the [[Content Delivery Network]] —
   free, no code, see [[Cache Busting]].
2. **In-process memory** — a dictionary with a TTL.
   Perfect for one box, wrong the moment there are two.
3. **[[Redis]]** — shared across processes, and also
   useful for sessions, rate limits and
   [[Message Queues]].
4. **Materialised results in the database** — a table you
   refresh on a schedule.

## Why it matters here

Reach for layers 1 and 2 before adding a component. Adding
Redis to a one-box app to cache a query that needs an
index is a net loss.

## Invalidation

The hard part. Prefer strategies that avoid it: short
TTLs, or content-addressed keys that change when the data
does. Explicit invalidation on write works until the
second place that writes forgets.

## Related

[[Content Delivery Network]] · [[Cache Busting]] ·
[[Redis]] · [[Read Replicas]] · [[Service Worker]]

## Sources

- [[redis-data-store-get-started]] ·
  [[cloudflare-cache-purge]]
