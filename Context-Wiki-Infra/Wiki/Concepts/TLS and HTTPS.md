---
type: Concept
title: "TLS and HTTPS"
description: "What a certificate proves, how it is issued and renewed, and why HTTPS is now the floor rather than an upgrade."
tags: [foundations, security]
timestamp: "2026-07-27T00:00:00Z"
---

# TLS and HTTPS

TLS encrypts the connection and proves the server is
really the host it claims to be. HTTPS is HTTP carried
over TLS.

## What a certificate actually asserts

A certificate binds a hostname to a public key, signed by
a certificate authority the browser already trusts. It
proves control of the hostname — not that the operator is
honest, competent, or the company you think.

## Why it matters here

- It is free and automatic now. [[Let's Encrypt]] issues
  certificates at no cost via [[ACME Protocol]], and
  [[Caddy]] or [[Cloudflare Pages]] handle issuance and
  renewal without configuration.
- Browsers penalise plain HTTP, and features such as
  service workers require a secure context — so
  [[Progressive Web App]] work depends on it.
- It is the [[Encryption in Transit]] control that every
  compliance framework asks about first.

## Practical baseline

- TLS 1.2 minimum, TLS 1.3 preferred.
- Redirect HTTP to HTTPS; then add HSTS once you are sure.
- Let something else own renewal. Expired certificates are
  a top cause of small-site outages.

## Watch out for

- HSTS is hard to undo — browsers remember it for the
  `max-age` you set. Start with a short one.
- A certificate on the CDN edge does not encrypt the hop
  from CDN to origin unless you configure that too.

## Related

[[Automatic HTTPS]] · [[ACME Protocol]] ·
[[Encryption in Transit]] · [[Security Headers]] ·
[[Reverse Proxy]]

## Sources

- [[cloudflare-what-is-ssl]] · [[owasp-tls-cheatsheet]] ·
  [[letsencrypt-how-it-works]] ·
  [[mdn-strict-transport-security]]
