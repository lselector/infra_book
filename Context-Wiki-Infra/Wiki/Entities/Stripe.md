---
type: Vendor
title: "Stripe"
description: "Payments and subscription billing - hosted checkout that keeps card data off your servers."
tags: [product-patterns, saas]
timestamp: "2026-07-27T00:00:00Z"
---

# Stripe

Payment processing, with hosted Checkout and a Billing
product for subscriptions.

## Why hosted Checkout is the right default

Card details never touch your server. That removes the
overwhelming majority of PCI scope, which is otherwise a
serious compliance burden for a small team — a much bigger
deal than the small loss of design control.

## Subscriptions

Billing handles the parts that are tedious and easy to get
wrong: proration, trials, upgrades and downgrades,
dunning, invoices, tax. Building this yourself is a
multi-month detour.

## The integration rules

1. **Webhooks are the source of truth**, not the redirect
   back to your site. Users close tabs; webhooks retry.
2. **Verify the webhook signature.** An unverified webhook
   endpoint is a way to grant yourself a free
   subscription.
3. **Be idempotent.** Webhooks are delivered at least
   once.
4. Separate test and live keys per environment — see
   [[Deployment Environments]] and
   [[Secrets Management]].

## Related

[[Authentication]] · [[Secrets Management]] ·
[[Deployment Environments]] · [[Transactional Email]] ·
[[SOC 2]]

## Sources

- [[stripe-how-checkout-works]] ·
  [[stripe-subscriptions-overview]]
