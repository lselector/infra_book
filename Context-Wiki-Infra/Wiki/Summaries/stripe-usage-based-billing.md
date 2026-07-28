---
type: Summary
title: "Usage-based billing implementation guide (Stripe)"
description: "Pay-as-you-go pricing is a flexible, scalable model that lets you charge customers in arrears for the usage they accrue."
resource: "https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide"
source_file: "Raw/12_ai_in_saas/stripe-usage-based-billing.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Usage-based billing implementation guide (Stripe)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/stripe-usage-based-billing.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide>

## Opening

> Pay-as-you-go pricing is a flexible, scalable model that lets you charge customers in arrears for the usage they accrue. AI businesses, SaaS platforms, and cloud services often use this pricing model.
> This guide covers basic usage-based billing with Billing Meters. Unless you maintain an existing Billing Meters integration, use [Metronome](https://docs.stripe.com/billing/usage-based), Stripe’s primary usage-based billing platform, instead.
> If you already use Billing Meters, you don’t need to migrate. Continue using this guide for your existing integration.
> This guide describes how to implement pay-as-you-go pricing on Stripe for a fictional company called Hypernian. Hypernian charges their customers the following rates for their LLM models:

## Contents of the source document

- Set up a pay-as-you-go pricing model
  - Charge customers based on their usage of your product or service.
  - What you’ll build
  - Create a meter
  - Create a pricing model
  - Create a customer
  - Create a subscription
  - Send a test meter event
  - Create a preview invoice
  - OptionalRetrieve usage for a custom time period
  - Next steps

## Related pages

[[Stripe]]
