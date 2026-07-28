---
type: Vendor
title: "Cloudflare"
description: "Registrar, DNS, CDN and static hosting in one account - the cheap front door for almost any small site."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [deployments, vendor]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloudflare

A single account that can register the domain, host the
DNS, serve the site from a global edge network, and issue
the TLS certificate — at no cost for a small project.

## What you get for free

- [[Cloudflare Registrar]] — domains at wholesale, no
  markup.
- [[Cloudflare DNS]] — authoritative DNS with a fast API.
- [[Cloudflare Pages]] — static hosting with CI and
  preview deployments.
- CDN, TLS, HTTP/3 and DDoS absorption by default.
- [[Cloudflare R2]] for object storage with no egress fee.

## Why it is the default here

The alternative is four vendors, four bills and four
support relationships. Consolidating them removes most of
the setup for rungs 1-4 of [[The Ladder]] and makes the
whole thing free.

## Watch out for

- Concentration risk: one account outage or lockout
  affects your domain, DNS and hosting at once. Enable
  [[Multi-Factor Authentication]] and keep the registrar
  recovery email elsewhere.
- Proxied ("orange cloud") records hide your origin IP,
  which is usually what you want — but breaks non-HTTP
  protocols on that hostname.

## Related

[[Cloudflare Pages]] · [[Cloudflare DNS]] ·
[[Cloudflare Registrar]] · [[Cloudflare R2]] ·
[[Content Delivery Network]] · [[Cloudflare Workers]] ·
[[Cloudflare Pages Functions]]

## Sources

- [[cloudflare-pages-overview]] ·
  [[cloudflare-registrar-overview]] ·
  [[cloudflare-trust-hub-compliance]]
