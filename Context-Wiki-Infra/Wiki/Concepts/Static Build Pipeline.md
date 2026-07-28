---
type: Concept
title: "Static Build Pipeline"
description: "Validate, optimise images, build, cache-bust, deploy - numbered scripts you run in order."
wikipedia: "https://en.wikipedia.org/wiki/Build_automation"
tags: [architectures, playbooks]
timestamp: "2026-07-27T00:00:00Z"
---

# Static Build Pipeline

A short chain of scripts, each doing one thing, numbered
so the order is obvious to anyone who opens the folder.

## The five stages

1. **Validate** — parse every `item.json`, fail loudly on
   bad data, remove stray `.DS_Store` files.
2. **Optimise images** — resize, strip metadata, generate
   thumbnails. See [[web-dev-image-formats]].
3. **Build** — render JSON into HTML pages, plus any
   generated data files the frontend needs.
4. **Cache-bust** — stamp CSS and JS references. See
   [[Cache Busting]].
5. **Deploy** — `wrangler pages deploy` via [[Wrangler]].

## Why it matters here

- Numbered scripts are self-documenting. `s1_`, `s2_`,
  `s3_`, `s4_` tells a newcomer the order without a README.
- A `justfile` on top names the chain once — `just build`,
  `just deploy` — so nobody runs stage 4 having skipped
  stage 1, and CI calls the same recipe you do
  ([[just]]).
- Each stage is independently runnable, so a failed deploy
  does not mean re-optimising every image.
- The same chain runs identically on a laptop and in
  [[GitHub Actions]], which is what makes the move to
  [[Continuous Integration and Delivery]] a non-event.

## Watch out for

Validation that only warns. If stage 1 does not exit
non-zero on bad input, stage 3 will happily build a broken
page.

## Related

[[File-Based CMS]] · [[Cache Busting]] · [[Wrangler]] ·
[[Continuous Integration and Delivery]] · [[Git-Driven Deployment]] ·
[[uv]] · [[just]] · [[Development Setup]]

## Sources

- [[cloudflare-wrangler-pages-commands]] ·
  [[cloudflare-pages-build-config]] ·
  [[web-dev-image-formats]]
