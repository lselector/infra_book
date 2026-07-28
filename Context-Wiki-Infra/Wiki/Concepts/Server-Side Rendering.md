---
type: Concept
title: "Server-Side Rendering"
description: "Sending HTML instead of an empty div - the choice between CSR, SSR and SSG, and what each costs to run."
wikipedia: "https://en.wikipedia.org/wiki/Server-side_scripting"
tags: [architectures, product-patterns, frontend]
timestamp: "2026-07-28T00:00:00Z"
---

# Server-Side Rendering

Three ways to get a page in front of a user, in
increasing order of what they cost you to operate:

| | How | What it needs |
|---|---|---|
| **SSG** — static generation | HTML built once, at deploy time | A CDN. Nothing else ([[Static Site Hosting]]) |
| **SSR** — server rendering | HTML built per request, then *hydrated* into a live app | A running [[Node.js]] process, or an edge runtime |
| **CSR** — client rendering | Empty shell + JS bundle; the browser fetches data and builds the DOM | A CDN plus an API ([[Single Page Application and API]]) |

[[Next.js]] does all three, per route, which is why it
has taken over — and also why teams end up running a
server for a site that could have been files.

## Choosing, honestly

- **Content that is the same for everyone** — marketing,
  docs, catalogs, blogs: **SSG**. It is rung 1–2 of
  [[Stacks]], it costs nothing, and it cannot fall over.
- **Content personalised per request, where SEO and
  first paint matter** — a storefront, a dashboard
  landing: **SSR**.
- **An app behind a login** — the SEO argument
  evaporates: **CSR** is fine and simpler to host.

## What SSR actually costs

- **A server tier**, with all that follows: deploys,
  restarts, memory limits, an autoscaling story, and
  [[Load Balancing]] once there are two of them.
- **Double the work**, done twice — once on the server,
  once again during hydration in the browser. Get the
  data-fetching wrong and the client refetches
  everything you just rendered.
- **A cache to reason about.** Per-user HTML cannot sit
  on a CDN the way static files can; ISR/stale-while-
  revalidate is a real feature with real edge cases.

## The middle road most people want

Static-generate everything that can be, render the rest
at the edge, and keep the truly dynamic parts as client
fetches against an API. That is the [[Cloudflare Pages]]
+ [[Cloudflare Pages Functions]] shape at rung 2–3, and
it stays a CDN deployment rather than a fleet.

Whatever you pick, [[Core Web Vitals]] is the scoreboard:
SSR that ships 900 KB of JavaScript loses to plain HTML
every time.

## Related

[[Node.js]] · [[React]] · [[Next.js]] ·
[[Static Site Hosting]] · [[Single Page Application and API]] ·
[[Core Web Vitals]] · [[Cloudflare Pages]] ·
[[Progressive Web App]] · [[Responsive Design]]

## Sources

- Upstream documentation: the Next.js rendering guide
  and the React server-components documentation. Not
  part of the downloaded `Raw/` corpus — no capture to
  cite yet.
