---
type: Tool
title: "Next.js"
description: "The React framework that renders per route - static, server or client, with the hosting bill to match."
wikipedia: "https://en.wikipedia.org/wiki/Next.js"
tags: [frontend, deployments, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# Next.js

A full-stack framework around [[React]]: file-based
routing, server components, API routes, image
optimisation, and a choice of rendering strategy **per
route**.

## The choice that decides your infrastructure

| Rendering | What it needs to run |
|---|---|
| Static (SSG / `output: export`) | A CDN. [[Cloudflare Pages]] and nothing else |
| ISR — static, revalidated | A host that supports it, or a rebuild hook |
| SSR / React Server Components | A live [[Node.js]] or edge runtime, always on |
| API routes | The same runtime — this is a backend |

The framework makes these look like a one-line
difference. Operationally they are rung 1 versus rung 5
of [[Stacks]]. Decide it on purpose: a marketing site
that quietly became SSR is now a server you patch,
monitor and pay for.

## Hosting honestly

Vercel is the frictionless path and prices per usage.
Self-hosting is a Node process behind [[Caddy]], or a
container ([[Docker]]) on any host — supported, but you
own image optimisation, ISR cache and revalidation.
`output: standalone` produces the lean build for that.
If the whole site can be `output: export`, take the CDN
and skip the tier entirely.

## Watch out for

- **Accidental dynamism.** One `cookies()` call turns a
  static route dynamic. Check what the build reports.
- **Version-to-version churn.** Pages Router, App
  Router, server actions — this framework moves faster
  than the rest of your stack. Pin it.
- **Edge runtime is not Node.** No native modules, no
  filesystem, a different set of APIs.
- **Bundle creep.** Server components help; they do not
  absolve you of [[Core Web Vitals]].

## Related

[[React]] · [[Node.js]] · [[Server-Side Rendering]] ·
[[Cloudflare Pages]] · [[Cloudflare Pages Functions]] ·
[[Static Site Hosting]] · [[Docker]] · [[Caddy]] ·
[[Core Web Vitals]] ·
[[Vercel AI SDK]]

## Sources

- Upstream documentation: <https://nextjs.org/docs>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
