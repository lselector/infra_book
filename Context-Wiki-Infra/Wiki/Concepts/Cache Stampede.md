---
type: Concept
title: "Cache Stampede"
description: "A popular key expires and every request rebuilds it at once - the outage caused by the cache working as designed."
wikipedia: "https://en.wikipedia.org/wiki/Cache_stampede"
tags: [ops-and-security, reliability, performance]
timestamp: "2026-07-28T00:00:00Z"
---

# Cache Stampede

One hot cache entry expires; every concurrent request
misses, and all of them run the expensive query that the
cache existed to avoid. Also called dog-piling or the
thundering herd. Failure mode 4 of [[Failure Modes]].

## Why it is dangerous

The cache was hiding the fact that the origin cannot
serve the real traffic. A 99% hit rate means the database
sees 1% of requests — and at the moment of expiry it sees
100%. A stampede is the system briefly running with no
cache at all, which it was never sized for.

It happens most reliably to the most valuable key: the
homepage, the pricing table, the session lookup.

## The three fixes

**Lock on miss (mutex / single flight).** The first
request to miss takes a lock and recomputes; the others
wait briefly for it, or serve the stale value. This is
the general answer and the one to reach for first.

```python
val = cache.get(key)
if val is None:
    if cache.add(key + ":lock", 1, ttl=10):   # I won
        val = expensive()
        cache.set(key, val, ttl=300)
    else:                                      # someone else is on it
        val = cache.get_stale(key) or wait_briefly()
```

**Stale-while-revalidate.** Serve the expired value
immediately and refresh it in the background. The HTTP
cache directive of the same name gives you this at the
[[Content Delivery Network]] layer for free — one line in
`Cache-Control`, no application code.

**Jittered TTLs.** Never `ttl=3600` for everything
written in the same loop: `3600 + random(0, 300)`. This
alone prevents the mass-expiry version, where a whole
cohort of keys written together expires together.

## The related trap: cold cache

A restart, a flush, or a failover empties the cache
entirely and every key stampedes at once. It is why
"just restart Redis" during an incident can be the thing
that finally takes the site down. Warm the important keys
before sending traffic, and bring instances back
gradually.

## Watch out for

**A cache that is load-bearing.** If the origin cannot
survive a cache flush, the cache is not an optimisation —
it is infrastructure, and it needs the same redundancy
thinking as the database ([[Single Point of Failure]]).
Ask periodically: what happens if [[Redis]] is empty
right now? The honest answer is your real capacity.

**Caching instead of indexing.** A missing database index
hidden behind a cache is still a missing index, and the
stampede is when you find out ([[Anti-Patterns]]).

## Related

[[Failure Modes]] · [[Caching]] · [[Redis]] ·
[[Retry Storm]] · [[Cascading Failure]] ·
[[Content Delivery Network]] · [[Cache Busting]] ·
[[Hot Partition]] · [[Core Web Vitals]]

## Sources

- [[redis-data-store-get-started]] ·
  [[cloudflare-what-is-a-cdn]] ·
  [[web-dev-service-worker-caching]] ·
  [[sre-book-index]]
