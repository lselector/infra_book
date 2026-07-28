---
type: Service
title: "Cloudflare R2"
description: "S3-compatible object storage with no egress charges."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloudflare R2

Object storage with an S3-compatible API and, notably, no
fee for data leaving the network.

## Why that one difference matters

Egress is frequently the largest line on an
[[Amazon S3]] bill for anything user-facing — images,
downloads, video. R2 removes it, so cost becomes a
function of what you store rather than how popular you
are.

## What to use it for

- User uploads from an application.
- [[Database Backups]] shipped off the box.
- Large media referenced by a static site.

## Practical notes

- The S3 API compatibility means existing SDKs and tools
  work with an endpoint change.
- Public access can be served through a custom domain on
  the Cloudflare edge.
- Class A (write) and Class B (read) operations are
  charged; storage is per GB-month.

## Related

[[Object Storage]] · [[Amazon S3]] · [[Cloudflare]] ·
[[Database Backups]] · [[Cost Control]]

## Sources

- [[cloudflare-r2-overview]] · [[aws-s3-welcome]]
