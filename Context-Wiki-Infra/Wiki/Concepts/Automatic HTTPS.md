---
type: Concept
title: "Automatic HTTPS"
description: "Certificates obtained, installed and renewed with no cron job and no human - the modern default."
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Automatic HTTPS

The server obtains a certificate the first time it needs
one, installs it, and renews it before expiry — without
being asked.

## How it works

The server proves control of the hostname to a certificate
authority using [[ACME Protocol]], usually by answering an
HTTP challenge on port 80 or a DNS challenge, then keeps a
renewal timer.

## Why it matters here

- Expired certificates are a leading cause of small-site
  outages, and they always happen at a weekend. Removing
  the human from renewal removes the outage class.
- [[Caddy]] does this by default: name a hostname in the
  Caddyfile and HTTPS is on. [[Cloudflare Pages]] does it
  invisibly.
- It makes [[Encryption in Transit]] a configuration
  default rather than a project.

## Requirements to be aware of

- A public DNS name that resolves to the machine — see
  [[DNS Record Types]].
- Port 80 reachable for the HTTP challenge, or DNS API
  credentials for the DNS challenge.
- Rate limits at the CA. Use staging endpoints while
  experimenting.

## Related

[[TLS and HTTPS]] · [[ACME Protocol]] · [[Caddy]] ·
[[Let's Encrypt]] · [[Reverse Proxy]]

## Sources

- [[caddy-automatic-https]] · [[caddy-quickstart-https]] ·
  [[letsencrypt-getting-started]] · [[certbot-using]]
