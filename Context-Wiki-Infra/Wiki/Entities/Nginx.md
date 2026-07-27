---
type: Tool
title: "Nginx"
description: "The incumbent reverse proxy and web server - more configuration, more control, certificates sold separately."
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Nginx

A high-performance web server and reverse proxy, and the
most widely deployed option in this role.

## Where it is the right choice

- You already run it and it works.
- You need fine-grained control: complex rewrites, rate
  limiting, caching rules, mixed protocol handling.
- Your hosting environment or team standard assumes it.

## What it does not do

Obtain certificates. TLS is configured by pointing at
files that something else — usually [[Certbot]] — puts
there and renews on a timer. That is one more moving part,
and the part that fails silently until a certificate
expires.

## The comparison in one line

Nginx is more capable and more work; [[Caddy]] is
sufficient for the reverse-proxy job and removes the
certificate problem entirely. This book defaults to Caddy
and expects you to reach for Nginx deliberately.

## Watch out for

Forgetting `proxy_set_header X-Forwarded-For` and
`X-Forwarded-Proto`, after which the app sees every
request as local plaintext.

## Related

[[Reverse Proxy]] · [[Caddy]] · [[Certbot]] ·
[[TLS and HTTPS]] · [[One-Box Deployment]]

## Sources

- [[nginx-beginners-guide]] · [[nginx-reverse-proxy-guide]]
