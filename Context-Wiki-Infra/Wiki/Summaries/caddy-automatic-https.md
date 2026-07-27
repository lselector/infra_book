---
type: Summary
title: "Caddy — automatic HTTPS (certificate issuance and renewal)"
description: "Automatic HTTPS provisions TLS certificates for all your sites and keeps them renewed."
resource: "https://caddyserver.com/docs/automatic-https"
source_file: "Raw/03_deployments/caddy-automatic-https.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Caddy — automatic HTTPS (certificate issuance and renewal)

Extractive digest of the immutable capture in
`Raw/03_deployments/caddy-automatic-https.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://caddyserver.com/docs/automatic-https>

## Opening

> Automatic HTTPS provisions TLS certificates for all your sites and keeps them renewed. It also redirects HTTP to HTTPS for you! Caddy uses safe and modern defaults -- no downtime, extra configuration, or separate tooling is required.
> Here's a 28-second video showing how it works:
> Caddy keeps all managed certificates renewed and redirects HTTP (default port `80`) to HTTPS (default port `443`) automatically.
> then sites will be served over HTTPS automatically. You won't have to do anything else about it. It just works!

## Contents of the source document

- Automatic HTTPS
  - Overview
  - Activation
  - Effects
  - Hostname requirements
  - Local HTTPS
    - CA Root
    - CA Intermediates
  - Testing
  - ACME challenges
    - HTTP challenge
    - TLS-ALPN challenge
    - DNS challenge
  - On-Demand TLS
    - Using On-Demand TLS
  - Errors
    - Issuer fallback
  - Storage

## Related pages

[[ACME Protocol]] · [[Automatic HTTPS]] · [[Caddy]] · [[Cloudflare]] · [[HTTP]] · [[Key Rotation]] · [[Let's Encrypt]]
