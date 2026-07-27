---
type: Service
title: "Let's Encrypt"
description: "A free, automated certificate authority - the reason HTTPS stopped being a line item."
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Let's Encrypt

A non-profit certificate authority issuing free,
domain-validated TLS certificates through the
[[ACME Protocol]].

## What to know operationally

- Certificates are valid for 90 days; renewal is expected
  to be automatic and typically happens at 60 days.
- Domain validation only — it proves control of the
  hostname, nothing about the organisation.
- Wildcard certificates are available, but require the
  DNS-01 challenge.
- Rate limits apply per registered domain per week. Use
  the staging environment while experimenting or you will
  lock yourself out for days.

## How you will actually use it

Indirectly. [[Caddy]] talks to it for you, and
[[Cloudflare Pages]] handles certificates without
involving you at all. [[Certbot]] is the explicit route
when running [[Nginx]].

## Related

[[TLS and HTTPS]] · [[Automatic HTTPS]] ·
[[ACME Protocol]] · [[Caddy]] · [[Certbot]]

## Sources

- [[letsencrypt-getting-started]] ·
  [[letsencrypt-how-it-works]] · [[certbot-using]]
