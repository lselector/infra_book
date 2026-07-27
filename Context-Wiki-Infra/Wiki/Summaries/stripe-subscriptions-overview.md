---
type: Summary
title: "Stripe Billing — subscriptions overview"
description: "Subscriptions let customers make recurring payments to access a product or service."
resource: "https://docs.stripe.com/billing/subscriptions/overview"
source_file: "Raw/06_product_patterns/stripe-subscriptions-overview.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Stripe Billing — subscriptions overview

Extractive digest of the immutable capture in
`Raw/06_product_patterns/stripe-subscriptions-overview.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.stripe.com/billing/subscriptions/overview>

## Opening

> Subscriptions let customers make recurring payments to access a product or service. When you create a subscription, Stripe automatically generates invoices, attempts payment collection, and manages the subscription status throughout its lifecycle. A subscription moves through a predictable set of ...
> Unlike one-time payments, subscriptions require storing customer and payment method information for future billing cycles. Stripe handles the payment retry logic, dunning, and status transitions.
> Each of the following subscription lifecycle phases maps to a status change on the [Subscription object](https://docs.stripe.com/api/subscriptions/object). Understanding these statuses helps you know when to provision access, notify customers, and handle errors. You can use [webhook ...
> Create a new subscription in the [Dashboard](https://dashboard.stripe.com/subscriptions?status=active) or with the [Subscriptions API](https://docs.stripe.com/api/subscriptions/create). The resulting [Subscription object](https://docs.stripe.com/api/subscriptions/object) contains the subscribed ...

## Contents of the source document

- How subscriptions work
  - Manage recurring payments and subscription lifecycles.
  - Subscription lifecycle
    - Create the subscription
    - Handle the invoice
    - Confirm payment
    - Provision access to your product
    - Update the subscription
    - Handle unpaid subscriptions
    - Cancel the subscription
  - Subscription statuses
  - Payment statuses
    - Payment succeeded
    - Requires payment method
    - Requires action
  - See also

## Related pages

[[Authentication]] · [[Stripe]]
