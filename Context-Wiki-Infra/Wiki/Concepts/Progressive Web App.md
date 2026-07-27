---
type: Concept
title: "Progressive Web App"
description: "A website that installs to the home screen and works offline, without an app store."
tags: [architectures, mobile]
timestamp: "2026-07-27T00:00:00Z"
---

# Progressive Web App

A normal website that meets a few extra requirements and
consequently can be installed, launched from the home
screen, and run without a network.

## The three ingredients

1. **HTTPS** — required for the APIs involved. See
   [[TLS and HTTPS]].
2. **[[Web App Manifest]]** — name, icons, start URL,
   display mode.
3. **[[Service Worker]]** — intercepts requests and serves
   from a cache, enabling offline use.

## Why it matters here

- It is the cheapest route to "we have an app". No store
  review, no separate codebase, no native build chain.
- Deployment is unchanged — it is still files on
  [[Cloudflare Pages]].
- It composes with [[Responsive Design]]: make the site
  work on a phone first, then make it installable.

## Honest limits

- iOS support is real but narrower than Android; push
  notifications and install prompts behave differently.
- Anything needing deep OS integration still wants a
  native app.
- An offline-capable app has a cache-invalidation problem
  you must design for, not discover.

## Related

[[Responsive Design]] · [[Web App Manifest]] ·
[[Service Worker]] · [[Core Web Vitals]]

## Sources

- [[mdn-progressive-web-apps]] ·
  [[mdn-pwa-making-installable]] ·
  [[web-dev-service-worker-caching]]
