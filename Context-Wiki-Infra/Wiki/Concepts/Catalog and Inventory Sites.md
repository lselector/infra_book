---
type: Concept
title: "Catalog and Inventory Sites"
description: "Products, categories, detail pages and photo galleries - with no database and no admin panel."
wikipedia: "https://en.wikipedia.org/wiki/Online_shopping"
tags: [product-patterns, architectures]
timestamp: "2026-07-27T00:00:00Z"
---

# Catalog and Inventory Sites

A very common shape: a few hundred items, each with
photos, attributes and a detail page, plus category
listings and a contact route.

## The stack that fits

- [[File-Based CMS]] for the items.
- [[Static Build Pipeline]] to render listings and detail
  pages.
- [[Backend-Free Interactivity]] for brand and category
  filtering.
- [[Forms Without a Backend]] for quote requests.
- [[Cloudflare Pages]] to serve it.

Total running cost: a domain. See Appendix D of the book
for a worked example.

## Details that matter commercially

- **Structured data.** Marking items up as
  `schema.org/Product` is what gets rich results in
  search — a direct commercial return for a small effort.
- **Image discipline.** Galleries are the page weight.
  Correct sizing and lazy loading decide
  [[Core Web Vitals]].
- **A stable URL per item**, so links from listings and
  from search stay valid as inventory changes.

## Related

[[File-Based CMS]] · [[Static Build Pipeline]] ·
[[Forms Without a Backend]] · [[Core Web Vitals]]

## Sources

- [[schema-org-product]] ·
  [[google-search-central-structured-data]] ·
  [[mdn-responsive-images]] · [[mdn-lazy-loading]]
