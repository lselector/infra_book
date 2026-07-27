---
type: Concept
title: "DNS Record Types"
description: "A, AAAA, CNAME, MX, TXT and the handful of records a small site actually needs."
tags: [foundations, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# DNS Record Types

The small set of record types that covers almost every
web and SaaS need.

## The records you will actually use

| Type | Points to | Used for |
|---|---|---|
| `A` | IPv4 address | apex domain to a server |
| `AAAA` | IPv6 address | same, over IPv6 |
| `CNAME` | another name | `www` to the apex, or to a PaaS host |
| `MX` | a mail host | receiving email, and SES bounce paths |
| `TXT` | arbitrary text | SPF, DKIM, DMARC, domain verification |
| `NS` | nameservers | delegating the zone |
| `CAA` | a certificate authority | restricting who may issue certs |

## Why it matters here

- A static site on [[Cloudflare Pages]] needs a `CNAME`
  and nothing else.
- A one-box app needs an `A` record to the VPS, and that
  is what [[Automatic HTTPS]] validates against.
- [[Amazon SES]] setup is almost entirely `TXT` and `MX`
  records — DKIM keys, an SPF policy, and a DMARC policy.

## Watch out for

- You cannot put a `CNAME` on the apex in classic DNS.
  Cloudflare's CNAME flattening papers over this; other
  providers may not.
- A second SPF `TXT` record does not add to the first —
  it breaks both. Merge into one.

## Related

[[Domain Names and DNS]] · [[Email Authentication]] ·
[[TLS and HTTPS]]

## Sources

- [[cloudflare-dns-records]] ·
  [[cloudflare-dns-records-manage]] ·
  [[cloudflare-dns-email-records]]
