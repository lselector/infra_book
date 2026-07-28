---
type: Concept
title: "Cache Busting"
description: "Changing an asset URL when its contents change, so caches can be told to keep everything forever."
wikipedia: "https://en.wikipedia.org/wiki/Cache_invalidation"
tags: [architectures, performance]
timestamp: "2026-07-27T00:00:00Z"
---

# Cache Busting

Give every version of an asset a distinct URL. Then you
can cache aggressively without ever serving a stale file.

## Two ways to do it

- **Query string** — `style.css?v=2026072710`. Trivial to
  generate from a timestamp; works everywhere.
- **Filename hash** — `style.a3f9c1.css`. Cleaner, and
  survives caches that ignore query strings.

The HTML that references them must stay short-lived; the
assets it points at can be immutable.

## Why it matters here

- It is the difference between "my CSS update is live" and
  a support thread. On a [[Content Delivery Network]] this
  is the single most common self-inflicted bug.
- It lets you set `Cache-Control: max-age=31536000,
  immutable` on assets with a clear conscience.

## The rule

**Fingerprint the assets, never the HTML.** HTML is the
entry point and must be re-fetched; everything it
references can be cached forever because its URL changes
when it does.

## Related

[[Content Delivery Network]] · [[Static Build Pipeline]] ·
[[HTTP]] · [[Caching]]

## Sources

- [[cloudflare-pages-headers]] ·
  [[cloudflare-cache-purge]]
