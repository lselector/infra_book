---
type: Service
title: "Cloudflare Pages Functions"
description: "Serverless endpoints alongside a Pages site, for the small amount of dynamic behaviour a static site needs."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [deployments, serverless]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloudflare Pages Functions

Files in a `functions/` directory become server-side
routes deployed with the static site.

## What it is good for

- Proxying an API call so a secret key stays off the
  client.
- Handling a form post without a third party.
- Redirects and A/B logic that need a decision at request
  time.
- A webhook receiver.

## What it is not good for

Long-running work, heavy computation, or anything needing
a persistent database connection — it runs in a Workers
runtime with execution limits and a non-Node API surface.

## Why it matters here

It extends rungs 1-3 of [[The Ladder]] just far enough
that many sites never need a server at all: static files
plus three endpoints is a complete product for a
surprising number of cases.

## Related

[[Cloudflare Pages]] · [[Serverless Architecture]] ·
[[Forms Without a Backend]] · [[Wrangler]] ·
[[Cloudflare Workers]] · [[Cold Starts]]

## Sources

- [[cloudflare-pages-functions]] ·
  [[cloudflare-workers-secrets]]
