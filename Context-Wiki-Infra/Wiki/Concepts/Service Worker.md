---
type: Concept
title: "Service Worker"
description: "A script between your page and the network - the mechanism behind offline support and precaching."
wikipedia: "https://en.wikipedia.org/wiki/Web_worker"
tags: [architectures, mobile]
timestamp: "2026-07-27T00:00:00Z"
---

# Service Worker

A background script that intercepts network requests from
your pages and decides how to answer them: from the
network, from a cache, or both.

## Common caching strategies

- **Cache first** — for fingerprinted static assets. Fast,
  safe because the URL changes when content does. See
  [[Cache Busting]].
- **Network first, cache fallback** — for HTML and data
  that should be fresh but must not break offline.
- **Stale while revalidate** — serve the cache, refresh in
  the background.

## Why it matters here

It is the piece that turns a responsive site into an
installable [[Progressive Web App]], and it can
substantially cut repeat-visit load time even if you never
care about offline.

## Watch out for

- A service worker persists. A bad one can pin users to a
  broken version — always ship an update and unregister
  path before you need it.
- It only runs over HTTPS (localhost excepted).
- Caching HTML aggressively reproduces every
  cache-invalidation bug, now on the client where you
  cannot purge it.

## Related

[[Progressive Web App]] · [[Web App Manifest]] ·
[[Cache Busting]] · [[Caching]]

## Sources

- [[web-dev-service-worker-caching]] ·
  [[mdn-progressive-web-apps]]
