---
type: Concept
title: "Autoresponder Sequence"
description: "A pre-written series of emails sent on a schedule after signup - marketing email, not transactional."
wikipedia: "https://en.wikipedia.org/wiki/Autoresponder"
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Autoresponder Sequence

A drip: messages written once and delivered on a relative
schedule after someone joins a list.

## A workable shape

| Day | Message |
|---|---|
| 0 | welcome, deliver what was promised |
| 2 | the single most useful thing you know |
| 5 | a concrete example or case study |
| 9 | address the common objection |
| 14 | the offer |

Then move subscribers to the regular broadcast list.

## Why it matters here

It is rung 4 of [[The Ladder]] — real automated behaviour
with no backend at all. [[AWeber]], Mailchimp or Kit run
it entirely; your site stays static.

## Marketing versus transactional

This is **marketing** email: bulk, scheduled, and it
requires consent and an unsubscribe link.
[[Transactional Email]] — receipts, password resets — is
triggered by a user action and goes through a different
system, usually [[Amazon SES]]. Keep them separate: mixing
them damages the deliverability of both, and a password
reset must never be delayed behind a marketing queue.

## Related

[[Landing Page Email Capture]] · [[Double Opt-In]] ·
[[Transactional Email]] · [[Email Deliverability]] ·
[[AWeber]]

## Sources

- [[aweber-email-automation]] · [[aweber-home]] ·
  [[aweber-pricing]] · [[mailchimp-landing-pages]]
