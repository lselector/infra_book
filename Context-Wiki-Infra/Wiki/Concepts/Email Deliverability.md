---
type: Concept
title: "Email Deliverability"
description: "Whether your mail reaches the inbox - a reputation you build slowly and lose quickly."
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Email Deliverability

Getting accepted, and getting into the inbox rather than
the spam folder. Distinct from "the API returned 200".

## What receivers judge you on

- **[[Email Authentication]]** — SPF, DKIM, DMARC all
  passing and aligned. This is now a hard requirement for
  bulk senders at Gmail and Yahoo, not a nicety.
- **Complaint rate** — Google's threshold is 0.3%, and
  they mean it.
- **Bounce rate** — repeatedly mailing dead addresses is
  a strong negative signal.
- **Engagement** — opens and replies help; sustained
  silence hurts.
- **One-click unsubscribe** for bulk mail, and it must
  actually work.

## The operational duties

1. **Process bounces and complaints.** [[Amazon SES]]
   publishes them to SNS; consume the notifications and
   suppress those addresses permanently.
2. **Warm up** a new domain or dedicated IP gradually.
3. **Separate streams.** Send [[Transactional Email]] and
   marketing from different subdomains, so a bad campaign
   cannot stop password resets arriving.
4. **Never buy a list.** It is the fastest possible route
   to a blocked domain.

## Related

[[Email Authentication]] · [[Transactional Email]] ·
[[Amazon SES]] · [[Double Opt-In]] ·
[[Autoresponder Sequence]]

## Sources

- [[google-bulk-sender-guidelines]] ·
  [[aws-ses-bounce-complaint-handling]] ·
  [[aws-ses-event-publishing]] ·
  [[aws-ses-sending-quotas]]
