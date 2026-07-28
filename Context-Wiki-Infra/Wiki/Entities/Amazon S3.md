---
type: Service
title: "Amazon S3"
description: "The original object store - durable, ubiquitous, and metered on the way out."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_S3"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon S3

Object storage with very high durability, an API every
tool speaks, and lifecycle rules for tiering old data to
cheaper classes.

## What to use it for

- [[Database Backups]] shipped off the server.
- User uploads.
- Static website hosting, though [[Cloudflare Pages]] is
  simpler for that.

## Security defaults worth checking

- Block Public Access is on by default now — leave it on
  and serve through a CDN or signed URLs.
- New objects are encrypted at rest automatically; use
  SSE-KMS with a customer-managed [[AWS KMS]] key when you
  want the audit trail and revocation.
- Versioning protects against accidental deletion and
  ransomware.

## Watch out for

**Egress cost.** For user-facing media this is routinely
the largest line on the bill. [[Cloudflare R2]] is
S3-compatible and charges no egress — for anything served
to users, prefer it.

## Related

[[Object Storage]] · [[Cloudflare R2]] ·
[[Encryption at Rest]] · [[AWS KMS]] · [[Cost Control]]

## Sources

- [[aws-s3-welcome]] · [[aws-s3-website-hosting]] ·
  [[aws-s3-sse-kms]]
