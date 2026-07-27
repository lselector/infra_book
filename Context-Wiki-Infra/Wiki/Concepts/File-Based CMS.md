---
type: Concept
title: "File-Based CMS"
description: "A directory of JSON plus images as the content store - version-controlled, no database, no admin panel."
tags: [architectures, product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# File-Based CMS

Content lives as files in the repository: one folder per
item, an `item.json` describing it, and the images beside
it. A build script turns that tree into pages.

## Why it matters here

- It removes the database from rung 2 of [[The Ladder]]
  entirely. No schema, no migrations, no backups beyond
  Git.
- Content history, review and rollback come free — every
  edit is a commit.
- It scales further than expected. Hundreds of catalog
  items build in seconds and serve as static files.

## The shape that works

```
inventory/
  used/
    john-deere-5075e/
      item.json
      photo-01.jpg
```

A validation step runs first and refuses to build on a
malformed `item.json`, which keeps a typo from reaching
production. See [[Static Build Pipeline]].

## When to stop using it

- Non-technical people must edit content without Git.
- Items change many times a day.
- You need per-user or per-request views.

At that point you have arrived at rung 6 and want a real
database — [[SQLite]] first.

## Related

[[Static Build Pipeline]] · [[Static Site Hosting]] ·
[[Catalog and Inventory Sites]] ·
[[Backend-Free Interactivity]]

## Sources

- `Raw/sources.md` — local reference implementation
  (private) · [[schema-org-product]] ·
  [[google-search-central-structured-data]]
