---
type: Concept
title: "Core Web Vitals"
description: "The three user-experience metrics Google measures, and the small number of fixes that move them."
tags: [architectures, performance]
timestamp: "2026-07-27T00:00:00Z"
---

# Core Web Vitals

Three field metrics that stand in for perceived speed and
stability.

| Metric | Measures | Good |
|---|---|---|
| LCP | when the main content appears | < 2.5s |
| INP | responsiveness to input | < 200ms |
| CLS | unexpected layout shift | < 0.1 |

## What actually moves them on a small site

- **Images.** Correct format, correct size, `width` and
  `height` attributes set (which fixes most CLS), and
  lazy loading below the fold.
- **A CDN.** [[Content Delivery Network]] delivery is the
  single biggest LCP win for a global audience.
- **Fewer blocking scripts.** On a static site there is
  often nothing to remove — which is the point.
- **Font loading strategy**, which causes both shift and
  delay.

## Why it matters here

A static site on the edge starts near-perfect. Most Core
Web Vitals problems are self-inflicted by adding
frameworks, tag managers and unsized images.

## Related

[[Responsive Design]] · [[Content Delivery Network]] ·
[[Progressive Web App]] · [[Cache Busting]]

## Sources

- [[web-dev-vitals]] · [[mdn-lazy-loading]] ·
  [[web-dev-image-formats]]
