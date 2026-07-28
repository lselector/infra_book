---
type: Concept
title: "Encryption in Transit"
description: "TLS everywhere, including the hops you forgot - proxy to app, app to database, app to backup."
wikipedia: "https://en.wikipedia.org/wiki/Transport_Layer_Security"
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Encryption in Transit

Data is encrypted while moving between components. The
public hop is the obvious one; the internal hops are the
ones that get missed.

## The hops to check

1. **Browser to edge** — [[TLS and HTTPS]], handled by
   [[Automatic HTTPS]].
2. **Edge to origin** — a CDN in flexible mode can leave
   this leg in plaintext. Use full/strict.
3. **Proxy to app** — on `127.0.0.1` this is acceptable;
   across a network it is not.
4. **App to database** — [[PostgreSQL]] supports SSL
   connections and you should require them once the
   database is not on the same host.
5. **App to backup storage** — HTTPS endpoints.

## The enforcement layer

Redirect HTTP to HTTPS, then add HSTS so browsers refuse
plaintext before they even try. TLS 1.2 minimum.

## Why it matters here

It pairs with [[Encryption at Rest]] as the two encryption
controls every auditor and every questionnaire asks about,
and both are close to free on modern infrastructure.

## Related

[[TLS and HTTPS]] · [[Automatic HTTPS]] ·
[[Encryption at Rest]] · [[Security Headers]] · [[SOC 2]]

## Sources

- [[owasp-tls-cheatsheet]] ·
  [[mdn-strict-transport-security]] ·
  [[postgresql-ssl-tcp]] ·
  [[mdn-security-practical-guides]]
