---
type: Vendor
title: "AWeber"
description: "Long-established email marketing service - lists, sign-up forms and autoresponder campaigns."
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# AWeber

Email marketing: hosted sign-up forms, list management,
broadcast sending and automated campaigns.

## Where it sits in this book

It is the [[Autoresponder Sequence]] at rung 4 of
[[The Ladder]]. The site stays static; AWeber hosts the
form endpoint, the confirmation email, the list and the
drip.

## What you use

- A hosted form, or a plain HTML form posting to their
  endpoint.
- **Confirmed (double) opt-in** — see [[Double Opt-In]].
- **Campaigns**: a welcome sequence triggered on
  subscription, then the regular broadcast list.
- Unsubscribe handling and compliance footers, which are
  provided rather than built.

## Choosing between it and the alternatives

Mailchimp, Kit and MailerLite occupy the same space and
any of them works. Choose on the free-tier limit at your
list size and on which editor you can stand. The
architecture in this book does not change.

## The important boundary

This is **marketing** email. Password resets and receipts
are [[Transactional Email]] and belong in
[[Amazon SES]] — separate system, separate reputation.

## Related

[[Autoresponder Sequence]] · [[Double Opt-In]] ·
[[Landing Page Email Capture]] · [[Mailchimp]] ·
[[Transactional Email]]

## Sources

- [[aweber-home]] · [[aweber-email-automation]] ·
  [[aweber-pricing]]

> The AWeber knowledge base blocks automated retrieval, so
> mechanics such as double opt-in are sourced here from
> Mailchimp's equivalent documentation. See "Known gaps"
> in `Raw/sources.md`.
