---
type: Service
title: "Cloudflare Pages"
description: "Free static hosting on the edge, with Git builds, preview deployments and automatic TLS."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [deployments, static]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloudflare Pages

Static site hosting served from Cloudflare's edge network.
Rung 1 of [[The Ladder]].

## Two ways to deploy

- **Direct upload** — build locally, then
  `wrangler pages deploy ./site` via [[Wrangler]]. Full
  control of the build, no CI configuration.
- **Git integration** — connect the repository and
  Cloudflare builds on push. Zero local setup, and every
  branch gets a preview URL.

Direct upload suits a [[Static Build Pipeline]] with local
image processing; Git integration suits conventional
framework builds.

## What comes free

- TLS certificate, issued and renewed automatically.
- Global [[Content Delivery Network]] distribution.
- Preview deployment per branch and per pull request.
- Instant rollback to any previous deployment.
- Custom headers and redirects via `_headers` and
  `_redirects`.

## Watch out for

- File count and size limits on the free plan — check
  before uploading a large media library.
- Build minutes are metered on Git-integrated projects.
- Dynamic behaviour needs
  [[Cloudflare Pages Functions]]; Pages itself serves
  files only.

## Related

[[Cloudflare]] · [[Wrangler]] · [[Static Site Hosting]] ·
[[Cache Busting]] · [[Deployment Environments]]

## Sources

- [[cloudflare-pages-overview]] ·
  [[cloudflare-pages-direct-upload]] ·
  [[cloudflare-pages-git-integration]] ·
  [[cloudflare-pages-custom-domains]] ·
  [[cloudflare-pages-headers]] ·
  [[cloudflare-pages-limits]]
