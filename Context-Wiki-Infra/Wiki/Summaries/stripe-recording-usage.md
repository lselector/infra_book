---
type: Summary
title: "Record usage with the API (Stripe)"
description: "You must record usage in Stripe to make sure you bill your customers the correct amounts each billing period."
resource: "https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api"
source_file: "Raw/12_ai_in_saas/stripe-recording-usage.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Record usage with the API (Stripe)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/stripe-recording-usage.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api>

## Opening

> You must record usage in Stripe to make sure you bill your customers the correct amounts each billing period. To record usage, first [configure your meter](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure), and then send meter events that include the event name configured ...
> You can decide how often you record usage in Stripe, for example as it occurs or in batches. Stripe processes meter events asynchronously, so aggregated usage in meter event summaries and on upcoming invoices might not immediately reflect recently received meter events.
> Create a [Meter Event](https://docs.stripe.com/api/billing/meter-event/create) using the API.
> Command Line

## Contents of the source document

- Record usage for billing with the API
  - Learn how to record usage using the Stripe API.
  - Create meter events
    - Idempotency
    - Event timestamps
    - Usage values
    - Dimension cardinality limits
    - Rate limits
    - High-throughput ingestion with higher rate limits API v2
  - Handle meter event errors
    - Example payloads
    - Error codes
    - Listen to events

## Related pages

[[Authentication]] · [[Idempotency]] · [[Node.js]] · [[Resend]] · [[Stripe]]
