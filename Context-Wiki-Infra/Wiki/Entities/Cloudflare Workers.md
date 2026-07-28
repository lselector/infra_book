---
type: Tool
title: "Cloudflare Workers"
description: "Code on Cloudflare's edge in V8 isolates - no cold start worth measuring, and a runtime that is not Node."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [deployments, serverless, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# Cloudflare Workers

Cloudflare's serverless runtime. Your code runs in a
**V8 isolate** — the same sandbox a browser tab uses —
rather than in a container or a VM, in data centres close
to the user.

## Why the isolate matters

Starting an isolate takes single-digit milliseconds and a
few megabytes, so Cloudflare can start one per request
without keeping anything warm. Practically, that means
**no cold start to design around** ([[Cold Starts]]) —
the trade every other serverless platform makes between
idle cost and first-request latency largely disappears.

The price is the runtime. An isolate is not a machine:
no filesystem, no TCP sockets in the general case, no
native modules, and limited CPU time per request. Code
that assumes Node.js APIs needs checking, though the
compatibility layer now covers a large part of them.
[[WebAssembly]] modules run here too, which is how
non-JavaScript languages get in.

## What it is for, at this wiki's scale

- The dynamic edge of an otherwise static site — a form
  handler, an auth check, an API proxy that hides a key.
  On [[Cloudflare Pages]] this is
  [[Cloudflare Pages Functions]], which *is* Workers with
  file-based routing.
- Rewriting requests and responses: redirects, headers,
  A/B splits, image transforms.
- A small API that needs to be near users everywhere
  without operating anything in multiple regions.

## The storage that goes with it

An isolate has no disk, so state lives in Cloudflare's
own services: KV (eventually consistent key-value), D1
(SQLite at the edge), Durable Objects (one coordinated
instance per key — the standard answer for realtime
state, and a genuine alternative to
[[Sticky Sessions]]), and [[Cloudflare R2]] for objects.
Secrets go in the Workers secret store, never in
`wrangler.toml` ([[Secrets Management]]).

## Deploying

[[Wrangler]] — `wrangler dev` locally, `wrangler deploy`
to ship, and the same CLI manages secrets and tails logs.

## Watch out for

- **Vendor gravity.** The runtime is portable-ish;
  KV, D1 and Durable Objects are not. Know which side of
  that line each piece of your app is on.
- **CPU limits.** Long computation is the wrong workload
  here; the model assumes short, I/O-bound requests.
- **Talking to your own database.** A Postgres connection
  from thousands of edge locations is a
  [[Connection Pooling]] problem — use Hyperdrive, a
  connection pooler, or an HTTP-based data API.

## Related

[[Cloudflare]] · [[Cloudflare Pages]] ·
[[Cloudflare Pages Functions]] · [[Wrangler]] ·
[[Cloudflare R2]] · [[Serverless Architecture]] ·
[[Cold Starts]] · [[Micro-VMs]] · [[WebAssembly]] ·
[[Content Delivery Network]] · [[Secrets Management]] ·
[[Sticky Sessions]]

## Sources

- [[cloudflare-wrangler-workers-commands]] ·
  [[cloudflare-workers-secrets]] ·
  [[cloudflare-pages-functions]] ·
  [[cloudflare-wrangler-install]]
