---
type: Concept
title: "Responsive Design"
description: "One layout that works from a phone to a desktop - viewport, fluid layout, media queries, touch targets."
tags: [architectures, mobile]
timestamp: "2026-07-27T00:00:00Z"
---

# Responsive Design

A single codebase that adapts to the screen it is on,
rather than a separate mobile site.

## The checklist that covers most of it

- `<meta name="viewport" content="width=device-width,
  initial-scale=1">` — without it a phone renders a
  desktop-width page and shrinks it.
- Fluid layout with CSS grid or flexbox; avoid fixed pixel
  widths.
- Media queries for the few places layout must genuinely
  change.
- Touch targets around 44px; hover-only interactions have
  no equivalent on a phone.
- Responsive images with `srcset` so phones do not
  download desktop-sized files.

## Why it matters here

- Most traffic to a small site is mobile. A site that is
  awkward on a phone is awkward for the majority.
- Image weight is the usual performance problem, and it
  hits mobile hardest — see [[Core Web Vitals]].

## Watch out for

Testing only in a desktop browser's device emulator. Real
devices differ on fonts, scroll behaviour and network.

## Related

[[Progressive Web App]] · [[Core Web Vitals]] ·
[[Static Site Hosting]]

## Sources

- [[mdn-responsive-design]] ·
  [[mdn-viewport-meta-element]] ·
  [[mdn-media-queries-using]] · [[mdn-responsive-images]]
