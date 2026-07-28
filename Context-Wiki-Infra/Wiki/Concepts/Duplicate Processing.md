---
type: Concept
title: "Duplicate Processing"
description: "The same message handled twice - why at-least-once delivery is the norm, and why the fix is in your handler."
wikipedia: "https://en.wikipedia.org/wiki/Reliability_(computer_networking)"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Duplicate Processing

The same unit of work runs more than once: two charges,
two emails, two rows. Failure mode 7 of
[[Failure Modes]].

## Why it is normal, not exceptional

Almost every queue and API delivers **at least once**.
The reason is unavoidable: the consumer processes a
message and then acknowledges it. If it dies between
those two steps — or the ack is lost, or the ack arrives
after the visibility timeout — the broker correctly
concludes the work was not done and delivers it again.

"Exactly-once delivery" is not something you can buy at
the transport layer. What systems that advertise it
actually provide is at-least-once delivery plus
deduplication, which is what you are about to build.

## Common sources

- Broker redelivery after a consumer crash or timeout
  ([[RabbitMQ]], SQS, [[Redis]] streams).
- A [[Retry Storm]] retrying a POST that already
  succeeded but whose response was lost.
- A webhook provider retrying because your 200 was slow.
- A user double-clicking Submit.
- Two cron runs overlapping because the first took longer
  than the interval.
- A deploy that restarts workers mid-batch.

## The fix: make the handler idempotent

Not "prevent duplicates" — **absorb** them. See
[[Idempotency]] for the mechanics; the short version:

- Give every unit of work a stable ID chosen by the
  *producer*, not the consumer.
- Record processed IDs in the same transaction as the
  effect, with a unique constraint. The database, not
  your `if`, is what makes this correct under
  concurrency.
- Where an external call is involved, pass an idempotency
  key — [[Stripe]] and most payment APIs accept one, and
  a repeated key returns the original result instead of
  charging again.

```sql
INSERT INTO processed (message_id) VALUES ($1)
ON CONFLICT DO NOTHING RETURNING 1;   -- no row = already done
```

## The ordering people get wrong

Do the side effect *then* record it, and a crash between
them repeats the effect. Record it *then* do it, and a
crash loses the work entirely. Neither is safe alone,
which is why the record and the effect must share one
transaction — or, when the effect is external (an email,
a charge), why that external call must itself accept an
idempotency key.

## Watch out for

**Emails and money have no undo.** Those two handlers
deserve idempotency before anything else does.
**Non-idempotent SQL**: `balance = balance + 10` is
dangerous on redelivery; `balance = $new_total` is not.

## Related

[[Failure Modes]] · [[Idempotency]] ·
[[Poison Message]] · [[Queue Backlog]] ·
[[Message Queues]] · [[RabbitMQ]] · [[Retry Storm]] ·
[[Stripe]] · [[Transactional Email]] ·
[[Event-Driven Architecture]]

## Sources

- [[rabbitmq-tutorial-work-queues]] ·
  [[stripe-how-checkout-works]] ·
  [[aws-well-architected-reliability]]
