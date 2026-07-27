---
type: Concept
title: "Single Page Application and API"
description: "A static frontend calling a separate backend - clean separation, at the cost of CORS and auth plumbing."
tags: [architectures]
timestamp: "2026-07-27T00:00:00Z"
---

# Single Page Application and API

The frontend is a static bundle served from a CDN. It
calls a backend API for data. The two deploy
independently.

## Why it matters here

- The frontend becomes rung-1 infrastructure: free
  hosting, global CDN, atomic deploys.
- The backend shrinks to JSON endpoints, which makes it
  easier to put behind [[Managed PaaS]] or
  [[Serverless Architecture]].
- Mobile apps and third parties can reuse the same API.

## The costs you take on

- **[[CORS]] configuration** between two origins.
- **Token handling** — the browser now holds credentials,
  so [[JSON Web Token]] verification and refresh become
  your problem. [[Firebase Authentication]] removes most
  of this.
- **Two deploy pipelines**, and version skew between them.
- **SEO** needs thought; a client-rendered page is not
  what a crawler prefers.

## When it is worth it

When you genuinely have multiple clients, or a frontend
team that must ship independently. For a single web app
with one team, [[Monolithic Web App]] is usually less
work.

## Related

[[Monolithic Web App]] · [[Authentication]] ·
[[Serverless Architecture]] · [[Managed PaaS]]

## Sources

- [[mdn-cors]] · [[mdn-fetch-api-using]] ·
  [[web-dev-rendering-on-the-web]]
