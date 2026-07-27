---
type: Concept
title: "Content Delivery Network"
description: "Caching copies of your site near users - the cheapest performance win available to a small site."
tags: [foundations, performance]
timestamp: "2026-07-27T00:00:00Z"
---

# Content Delivery Network

A network of edge servers that cache your content close
to visitors, so requests are answered without crossing an
ocean to your origin.

## Why it matters here

- For a static site it is not an optimisation, it *is*
  the hosting. [[Cloudflare Pages]] serves from the edge
  by default at no cost.
- It absorbs traffic spikes that would flatten a $5 VPS,
  and hides your origin address.
- It removes most of the reason to run multiple app
  servers early — cache first, scale later.

## What caches well

- Immutable assets with a fingerprint in the URL — see
  [[Cache Busting]].
- Whole HTML pages, if the site is static.
- Not: authenticated pages, anything user-specific.

## Watch out for

- A CDN in front of a stale origin serves stale content
  confidently. Know how to purge.
- Long cache lifetimes on un-fingerprinted HTML or CSS is
  the classic "why is my update not live" bug.

## Related

[[Cache Busting]] · [[Static Site Hosting]] ·
[[Caching]] · [[Load Balancing]]

## Sources

- [[cloudflare-what-is-a-cdn]] ·
  [[cloudflare-cache-purge]] ·
  [[cloudflare-pages-headers]]
