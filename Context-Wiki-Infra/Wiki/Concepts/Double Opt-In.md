---
type: Concept
title: "Double Opt-In"
description: "Requiring a click in a confirmation email before adding someone to a list."
wikipedia: "https://en.wikipedia.org/wiki/Opt-in_email"
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Double Opt-In

After someone submits a form, the provider sends a
confirmation email. Only a click on that link adds them to
the list.

## Why accept the lost signups

- **The address is real.** Typos and fake addresses never
  enter the list, protecting your bounce rate and
  therefore your [[Email Deliverability]].
- **Consent is evidenced.** You hold a timestamped record
  of the confirmation, which is what a GDPR complaint or
  a spam report is answered with.
- **Engagement is higher.** A confirmed subscriber chose
  twice.

It costs perhaps 20-30% of raw signups, and it is
consistently worth it.

## The one thing to get right

The confirmation email must arrive and must be obvious. A
vague subject line loses people who genuinely wanted in.
Say plainly: click to confirm, here is what you will
receive.

## Related

[[Landing Page Email Capture]] ·
[[Autoresponder Sequence]] · [[Email Deliverability]] ·
[[AWeber]]

## Sources

- [[mailchimp-double-opt-in]] · [[aweber-email-automation]]
  · [[google-bulk-sender-guidelines]]
