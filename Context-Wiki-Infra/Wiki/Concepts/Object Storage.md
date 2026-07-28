---
type: Concept
title: "Object Storage"
description: "Buckets of files addressed by key - where user uploads, backups and big assets belong."
wikipedia: "https://en.wikipedia.org/wiki/Object_storage"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Object Storage

Flat key-value storage for files, reached over HTTP, with
effectively unlimited capacity and per-GB pricing.

## What belongs there

- User uploads — never on the app server's disk, which is
  the smallest and least backed-up storage you own.
- [[Database Backups]] shipped off the box.
- Large media referenced by a static site.

## Why it matters here

It decouples data from the machine. A VPS can be destroyed
and rebuilt without losing anything, which is what makes
[[One-Box Deployment]] survivable.

## The egress trap

[[Amazon S3]] charges for data leaving the network, and
for a media-heavy site that line can exceed the storage
cost several times over. [[Cloudflare R2]] charges no
egress fee and is S3-API compatible, which makes it the
default recommendation here for anything served to users.

## Watch out for

- Public buckets. Default to private and serve through a
  CDN or signed URLs.
- Storing structured data as thousands of tiny objects
  when a database row would do.

## Related

[[Amazon S3]] · [[Cloudflare R2]] · [[Database Backups]] ·
[[Cost Control]] · [[Encryption at Rest]]

## Sources

- [[aws-s3-welcome]] · [[cloudflare-r2-overview]] ·
  [[gcp-cloud-storage-overview]]
