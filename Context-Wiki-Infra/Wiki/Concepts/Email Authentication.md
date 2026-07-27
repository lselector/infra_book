---
type: Concept
title: "Email Authentication"
description: "SPF, DKIM and DMARC - the three DNS records that let receivers verify your mail is really yours."
tags: [product-patterns, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Email Authentication

Three DNS records that together let a receiving server
decide whether a message claiming to be from your domain
actually is.

## The three

- **SPF** — a `TXT` record listing who may send for the
  domain. Checks the envelope sender.
- **DKIM** — the sender signs the message; the public key
  is a `TXT` record. Survives forwarding.
- **DMARC** — a `TXT` record at `_dmarc.yourdomain` that
  tells receivers what to do when SPF and DKIM fail
  (`none`, `quarantine`, `reject`) and where to send
  reports.

DMARC additionally requires **alignment**: the
authenticated domain must match the visible `From:`
domain. This is why [[Amazon SES]] pushes you toward a
custom MAIL FROM subdomain — it aligns SPF with your
domain rather than `amazonses.com`.

## The rollout that does not break mail

1. Publish DKIM and SPF.
2. Publish DMARC at `p=none` and read the reports for a
   few weeks — they will reveal senders you forgot.
3. Move to `p=quarantine`, then `p=reject`.

## Watch out for

- **Two SPF records break both.** There must be exactly
  one; merge them.
- The SPF 10-DNS-lookup limit, easily exceeded when
  several services send for the domain.

## Related

[[Email Deliverability]] · [[Amazon SES]] ·
[[DNS Record Types]] · [[Transactional Email]]

## Sources

- [[aws-ses-dkim]] · [[aws-ses-spf]] · [[aws-ses-dmarc]] ·
  [[aws-ses-custom-mail-from]] ·
  [[cloudflare-dns-email-records]]
