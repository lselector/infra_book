---
type: Concept
title: "Transactional Email"
description: "Email your application sends because a user did something - receipts, resets, notifications."
wikipedia: "https://en.wikipedia.org/wiki/Email"
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Transactional Email

One message, triggered by one user action, expected
immediately: a password reset, a receipt, an order
confirmation, an alert.

## Why you cannot just use SMTP from the box

A VPS IP has no sending reputation, is frequently on a
shared block already flagged by mailbox providers, and
port 25 is usually blocked outbound. Mail sent this way
lands in spam or nowhere. Use a sending service.

## The options

| Service | Per 1,000 | Setup effort |
|---|---|---|
| [[Amazon SES]] | ~$0.10 | highest — sandbox, verification, bounce handling |
| [[Postmark]] | ~$1.00-1.50 | low |
| [[Resend]] | ~$1.00 | low |

Below a few thousand messages a month the price
difference is negligible; choose on setup time. Above
that, SES is dramatically cheaper and the setup is a
one-off.

## Non-negotiables

- **Send asynchronously.** Enqueue it — see
  [[Message Queues]] — never block a request on SMTP.
- **Publish SPF, DKIM and DMARC** — see
  [[Email Authentication]].
- **Process bounces and complaints**, or your reputation
  degrades until nothing arrives.
- **Keep it separate from marketing mail**, which is
  [[Autoresponder Sequence]] territory.

## Related

[[Amazon SES]] · [[Email Authentication]] ·
[[Email Deliverability]] · [[Message Queues]] ·
[[Autoresponder Sequence]]

## Sources

- [[aws-ses-welcome]] · [[aws-ses-send-email-sdk]] ·
  [[aws-ses-smtp]] · [[postmark-developer-docs]] ·
  [[resend-introduction]]
