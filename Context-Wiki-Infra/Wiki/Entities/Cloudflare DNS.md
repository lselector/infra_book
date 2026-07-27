---
type: Service
title: "Cloudflare DNS"
description: "Authoritative DNS with a fast API, free at any volume."
tags: [deployments, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloudflare DNS

Hosts the authoritative records for your zone. Works
whether or not the domain is registered with Cloudflare —
point the registrar's nameservers at Cloudflare and the
zone moves.

## What it is used for here

- `CNAME` to [[Cloudflare Pages]] for the site.
- `A` record to the VPS for a [[One-Box Deployment]].
- `TXT` and `MX` records for [[Email Authentication]] —
  the DKIM, SPF and DMARC entries [[Amazon SES]] requires.
- DNS-01 [[ACME Protocol]] challenges via API token, for
  wildcard certificates.

## Useful specifics

- **CNAME flattening** at the apex, which classic DNS
  forbids.
- **Proxy toggle** per record: proxied records hide the
  origin and get CDN and DDoS protection; unproxied
  records are plain DNS.
- Changes propagate in seconds, not hours.

## Watch out for

Proxying a record used for mail or SSH. The proxy handles
HTTP(S) only — those records must stay unproxied.

## Related

[[Cloudflare]] · [[Domain Names and DNS]] ·
[[DNS Record Types]] · [[Email Authentication]]

## Sources

- [[cloudflare-dns-full-setup]] ·
  [[cloudflare-dns-records-manage]] ·
  [[cloudflare-dns-email-records]]
