---
type: Service
title: "Amazon SES"
description: "AWS's email sending service - about $0.10 per thousand, with real setup work."
tags: [product-patterns, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES

Sends email at roughly $0.10 per thousand messages — an
order of magnitude cheaper than the developer-friendly
alternatives, in exchange for doing the setup yourself.

## The setup, in order

1. **Verify a sending identity** — a domain rather than
   individual addresses.
2. **Publish Easy DKIM records** in [[Cloudflare DNS]].
3. **Configure a custom MAIL FROM subdomain**, so SPF
   aligns with your domain instead of `amazonses.com` —
   this is what DMARC alignment requires. Needs an `MX`
   and a `TXT` record.
4. **Publish DMARC** at `p=none`, read the reports, then
   tighten. See [[Email Authentication]].
5. **Request production access.** New accounts are in a
   sandbox: you may only send to verified addresses, at a
   low rate. The request is a form and usually takes a day
   — do it early, not on launch day.
6. **Subscribe to bounces and complaints** via SNS and
   suppress those addresses. This is mandatory, not
   optional; ignoring it degrades your reputation until
   nothing is delivered.

## Sending

SMTP interface for existing mail libraries, or the SDK
(`boto3`) for structured sending. Either way, enqueue it —
see [[Message Queues]] — rather than blocking a request.

## When to pay more instead

Below a few thousand emails a month the cost difference is
negligible, and [[Postmark]] or [[Resend]] remove steps
1-6 almost entirely. Choose SES for volume, or when you
are already in AWS.

## Related

[[Transactional Email]] · [[Email Authentication]] ·
[[Email Deliverability]] · [[Postmark]] · [[Resend]] ·
[[Cloudflare DNS]]

## Sources

- [[aws-ses-welcome]] · [[aws-ses-verify-identities]] ·
  [[aws-ses-dkim]] · [[aws-ses-spf]] ·
  [[aws-ses-custom-mail-from]] · [[aws-ses-dmarc]] ·
  [[aws-ses-production-access]] ·
  [[aws-ses-sending-quotas]] · [[aws-ses-smtp]] ·
  [[aws-ses-send-email-sdk]] ·
  [[aws-ses-event-publishing]] ·
  [[aws-ses-bounce-complaint-handling]] ·
  [[aws-ses-pricing]]
