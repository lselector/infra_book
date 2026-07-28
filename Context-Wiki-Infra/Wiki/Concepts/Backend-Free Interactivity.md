---
type: Concept
title: "Backend-Free Interactivity"
description: "Filtering, sorting, galleries and saved state in the browser, against generated data files."
wikipedia: "https://en.wikipedia.org/wiki/Dynamic_web_page"
tags: [architectures, product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Backend-Free Interactivity

A static site can feel dynamic. The build step emits a
data file; the browser does the rest.

## The pattern

1. The build writes a small generated file — say
   `brands.js` or `items.json` — alongside the pages.
2. Vanilla JavaScript fetches or imports it.
3. Filtering, sorting and search happen in memory.
4. User preferences persist in `localStorage`.

No framework is required, and no server is involved.

## Why it matters here

- It stretches rung 2 of [[The Ladder]] a long way. A
  catalog with a few hundred items filters instantly
  client-side and costs nothing to host.
- It keeps the deployment story trivial — still just files
  on [[Cloudflare Pages]].

## Limits

- The whole dataset ships to the browser. Fine at
  hundreds of items, wrong at tens of thousands.
- Nothing is secret. Anything in the data file is public.
- No writes. Persisting anything shared needs rung 5+.

## Related

[[File-Based CMS]] · [[Static Site Hosting]] ·
[[Catalog and Inventory Sites]] ·
[[Single Page Application and API]]

## Sources

- [[mdn-web-storage-api]] · [[mdn-fetch-api-using]] ·
  [[web-dev-rendering-on-the-web]]
