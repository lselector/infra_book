---
type: Concept
title: "Static Site Hosting"
description: "Serving pre-built files from a CDN - no server, no patching, effectively no cost."
tags: [architectures, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Static Site Hosting

The host serves files that were built ahead of time. There
is no application process, no database, and nothing that
executes per request.

## Why it matters here

- It is rung 1 of [[The Ladder]] and the correct answer
  far more often than people expect: marketing sites,
  documentation, portfolios, catalogs, even whole
  businesses.
- The security surface is close to zero. There is no
  server process to exploit and no credentials on the host.
- [[Cloudflare Pages]] gives free TLS, a global
  [[Content Delivery Network]], preview deployments and
  rollback without any of it being configured.

## What you give up

- Nothing renders per user. Personalisation must happen in
  the browser, or not at all.
- Search, comments and forms need a third party — see
  [[Forms Without a Backend]].

## What you do not give up

Dynamic-*looking* behaviour is still available:
[[Backend-Free Interactivity]] covers filtering, sorting
and galleries driven by generated data files.

## Related

[[File-Based CMS]] · [[Static Build Pipeline]] ·
[[Backend-Free Interactivity]] · [[Cache Busting]] ·
[[The Ladder]]

## Sources

- [[cloudflare-pages-overview]] ·
  [[cloudflare-pages-deploy-anything]] ·
  [[aws-s3-website-hosting]] ·
  [[web-dev-rendering-on-the-web]]
