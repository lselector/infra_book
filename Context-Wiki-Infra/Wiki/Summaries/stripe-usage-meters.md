---
type: Summary
title: "Configure a billing meter (Stripe)"
description: "Before you can record customer usage, you must create a meter, then configure it."
resource: "https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure"
source_file: "Raw/12_ai_in_saas/stripe-usage-meters.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Configure a billing meter (Stripe)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/stripe-usage-meters.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure>

## Opening

> Before you can [record customer usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage), you must create a meter, then configure it. After you configure the meter, you can’t make any changes aside from the display name.
> Meters specify how to aggregate meter events over a billing period. Meter events represent all actions that customers take in your system (for example, API requests). Meters attach to prices and form the basis of what’s billed.
> For the Hypernian example, meter events are the number of tokens a customer uses in a query. The meter is the sum of tokens over a month.
> You can use the Stripe Dashboard or API to configure a meter. To use the API with the Stripe CLI to create a meter, [get started with the Stripe CLI](https://docs.stripe.com/stripe-cli).

## Contents of the source document

- Create and configure a meter
  - Create and configure a meter for usage-based billing.
  - Create a meter
  - Meter configuration attributes
  - Fix incorrect usage data

## Related pages

[[Node.js]] · [[Stripe]]
