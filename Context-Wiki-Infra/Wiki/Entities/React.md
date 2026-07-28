---
type: Tool
title: "React"
description: "The component library most frontends are built with - and the question of whether your site needs one at all."
wikipedia: "https://en.wikipedia.org/wiki/React_(software)"
tags: [frontend, product-patterns, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# React

A JavaScript library for building user interfaces out of
components: state goes in, markup comes out, and React
updates the DOM when the state changes.

## Where it belongs in this wiki

React is the right answer for **application** UI — a
dashboard, an editor, a booking flow, anything with
substantial client-side state. It is the wrong answer
for a marketing site, a catalog, or a blog, which are
rungs 1–2 of [[Stacks]] and want
[[Static Site Hosting]] plus a little
[[Backend-Free Interactivity]].

The infrastructure consequence is direct: a React SPA is
static files on a CDN plus an API
([[Single Page Application and API]]). Nothing to
operate. It is only when you add
[[Server-Side Rendering]] that you take on a
[[Node.js]] tier — a real step up in ops burden, taken
deliberately or not at all.

## How it is shipped

| Shape | What you run |
|---|---|
| SPA (Vite build) | Static files — [[Cloudflare Pages]], any CDN |
| SSG ([[Next.js]] export) | Static files, prerendered per route |
| SSR / RSC ([[Next.js]]) | A Node or edge runtime, always on |

## Watch out for

- **Bundle size.** Every dependency ships to every
  visitor. [[Core Web Vitals]] is the scoreboard; code-
  split, lazy-load routes, and check what a date library
  costs you.
- **State management sprawl.** Server state is not UI
  state — a data-fetching library handles caching,
  retries and invalidation better than global stores do.
- **SEO on a pure SPA.** Crawlers do run JS, imperfectly.
  If organic search matters, prerender.
- **The hydration bill.** SSR sends HTML *and* the
  bundle; done carelessly, users wait for both.
- **Rewriting a static site as an app** because the team
  knows React. That is an [[Anti-Patterns|anti-pattern]]
  with a monthly invoice.

## Related

[[Node.js]] · [[Next.js]] · [[Server-Side Rendering]] ·
[[Single Page Application and API]] ·
[[Static Site Hosting]] · [[Progressive Web App]] ·
[[Responsive Design]] · [[Core Web Vitals]] ·
[[Cache Busting]]

## Sources

- Upstream documentation: <https://react.dev>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
