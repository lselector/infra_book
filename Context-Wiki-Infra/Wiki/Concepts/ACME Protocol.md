---
type: Concept
title: "ACME Protocol"
description: "The automated exchange that proves domain control and issues a certificate."
wikipedia: "https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment"
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# ACME Protocol

The standard by which a client proves it controls a
hostname and receives a certificate, with no human in the
loop.

## The challenge types

- **HTTP-01** — serve a token at
  `/.well-known/acme-challenge/`. Needs port 80 open.
  Cannot issue wildcards.
- **DNS-01** — publish a `TXT` record. Needs DNS API
  credentials, but works for wildcards and for hosts not
  publicly reachable.
- **TLS-ALPN-01** — proves control during the TLS
  handshake on port 443.

## Why it matters here

It is the machinery under [[Automatic HTTPS]]. You rarely
invoke it directly, but knowing which challenge is in play
explains most issuance failures: a blocked port 80, a
proxy intercepting the challenge path, or DNS that has not
propagated.

## Related

[[Automatic HTTPS]] · [[Let's Encrypt]] · [[Certbot]] ·
[[Caddy]] · [[DNS Record Types]]

## Sources

- [[letsencrypt-how-it-works]] ·
  [[caddy-automatic-https]] · [[certbot-using]]
