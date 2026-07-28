---
type: Vendor
title: "Resend"
description: "Developer-first transactional email - modern SDKs, React email templates."
website: "https://resend.com/"
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Resend

A transactional email API aimed at developers, with
first-class SDKs and the ability to author templates as
React components.

## What distinguishes it

- A small, clean API surface — sending an email is a few
  lines.
- React Email for templates, which removes the usual pain
  of hand-writing table-based HTML.
- Domain verification and DKIM setup guided in the
  dashboard.

## The trade

Same as [[Postmark]]: roughly ten times the SES price for
a fraction of the setup. Fine at low volume, a real cost
at high volume.

## The rule that still applies

Whichever service you use, you must publish SPF, DKIM and
DMARC for your domain, and handle bounces. The service
sends the mail; **you** own the domain's reputation. See
[[Email Authentication]] and [[Email Deliverability]].

## Related

[[Transactional Email]] · [[Amazon SES]] · [[Postmark]] ·
[[Email Authentication]]

## Sources

- [[resend-introduction]] · [[postmark-developer-docs]]
