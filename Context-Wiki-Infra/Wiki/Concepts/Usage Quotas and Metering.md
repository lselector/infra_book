---
type: Concept
title: "Usage Quotas and Metering"
description: "Counting tokens per tenant, capping them per plan, and billing for what is left - the difference between a feature and a liability."
wikipedia: "https://en.wikipedia.org/wiki/Software_metering"
tags: [ai-in-saas, product-patterns, scaling]
timestamp: "2026-07-28T00:00:00Z"
---

# Usage Quotas and Metering

[[Rate Limiting]] protects the system from a burst.
**Quotas protect the business from a month.** A tenant
politely making one request every ten seconds, all day,
every day, breaks no rate limit and can still cost more
than they pay you.

An AI feature is the first part of most SaaS products
with a genuinely variable unit cost. Meter it from day
one — retrofitting usage accounting onto a year of
un-instrumented traffic is miserable.

## Meter tokens, not requests

Every provider response reports what it actually cost:
input tokens, output tokens, and cached tokens billed at
a fraction of the input rate. Record all of them.

One row per call, written after the response completes:

| Column | Why |
|---|---|
| tenant, user | who to charge and who to talk to |
| feature | which part of the product is expensive |
| model | the cheap/expensive routing split |
| input, output, cached tokens | the actual billed units |
| cost estimate | so the number is readable without a rate table |
| created | for windows and invoices |

Aggregate that table nightly into per-tenant totals. Keep
the raw rows long enough to answer a billing dispute.

## Choose the unit the customer sees

Tokens are the truth but a terrible customer-facing unit
— nobody can predict them. Most products expose
something coarser:

- **Messages or actions** per month. Simple, predictable,
  and mispriced for anyone pasting whole documents.
- **Credits**, with different actions costing different
  amounts. Flexible, needs explaining.
- **Seats with fair-use caps.** The default: bundle the
  AI feature into the plan, cap it, and only meter the
  outliers.

Whatever you show, keep tokens underneath it. The
customer-visible unit will change; the accounting should
not have to.

## Hard caps, soft caps, and overage

- **Soft cap** — warn at 80%, keep serving. Right for
  paying customers you do not want to interrupt.
- **Hard cap** — refuse past the limit, with a clear
  message and an upgrade path. Mandatory on free tiers,
  where the alternative is funding someone else's
  side project.
- **Overage** — keep serving and bill the excess. Only
  with an explicit agreement, and a ceiling on top of it.

Enforce at two points: a **pre-check** before calling the
provider (cheap, approximate, prevents the spend) and a
**post-record** after the response (exact, updates the
running total). Pre-check only is unenforceable; post-
record only means the horse has already bolted.

## Billing for it

If usage is billed rather than bundled, use the billing
platform's metering primitives instead of computing
invoices yourself: report meter events as usage happens,
attach the meter to a price on the subscription, and let
the platform aggregate and invoice. [[Stripe]] does this
with billing meters — you send `{customer, value}` events
and the plan's price does the arithmetic.

Two properties matter more than the API details:
**events are aggregated asynchronously**, so your running
total in the UI should come from your own records rather
than the billing platform; and **event ingestion should
be idempotent**, or a retried report double-bills a
customer ([[Idempotency]], [[Duplicate Processing]]).

## Lowering the number

In rough order of leverage:

1. **Route to a cheaper model per feature.** Tier prices
   differ by an order of magnitude; most in-product
   features do not need the top tier.
2. **Cache the stable prefix.** System prompt, tool
   definitions and retrieved documents re-read at a
   fraction of the input price ([[Caching]]).
3. **Send less context.** Trim thread history, retrieve
   three chunks instead of thirty.
4. **Batch anything nobody is waiting for** at roughly
   half price.
5. **Cap output length.** `max_tokens` is a spend
   control, and output tokens cost several times input.

## Watch out for

- **Cancelled streams still bill** for what was
  generated. Record them.
- **Retries bill twice.** Meter every attempt, not every
  logical request, or your records will not reconcile
  with the provider invoice.
- **Free tiers are an attack surface.** Signup abuse
  turns into inference bills — see [[Bot Protection]].
- **No per-tenant view.** Without one you cannot tell a
  pricing problem from an abuse problem, and both look
  like "the AI bill went up".
- **Alert on the derivative, not the total.** A budget
  alarm at the provider fires after the money is gone;
  an alert on tokens-per-hour fires while you can still
  act ([[Monitoring and Alerting]], [[Cost Control]]).

## Related

[[Rate Limiting]] · [[Cost Control]] ·
[[LLM API Integration]] · [[AI Assistant Panel]] ·
[[Bot Protection]] · [[Stripe]] · [[Caching]] ·
[[Multi-Tenant SaaS]] · [[Idempotency]] ·
[[Monitoring and Alerting]]

## Sources

- [[stripe-usage-based-billing]] · [[stripe-usage-meters]]
  · [[stripe-recording-usage]] · [[anthropic-pricing]] ·
  [[anthropic-prompt-caching]] ·
  [[anthropic-batch-processing]] ·
  [[aws-budgets-managing-costs]] · [[gcp-billing-budgets]]
