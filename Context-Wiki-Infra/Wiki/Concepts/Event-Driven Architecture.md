---
type: Concept
title: "Event-Driven Architecture"
description: "Services that react to events on a queue or bus instead of calling each other - the shape distributed serverless takes."
wikipedia: "https://en.wikipedia.org/wiki/Event-driven_architecture"
tags: [architectures, scaling, serverless]
timestamp: "2026-07-28T00:00:00Z"
---

# Event-Driven Architecture

Instead of service A calling service B and waiting, A
publishes an event — `order.paid` — and whatever cares
about it reacts. The publisher does not know who is
listening, and does not wait for them.

## Why it turns up

The honest reason is rarely elegance. It is that some
work must not happen inside a web request:

- Video transcoding, PDF generation, image resizing.
- Sending the receipt, the welcome email, the webhook.
- Rebuilding a search index, recalculating a report.
- Anything that calls a third party that might be slow.

Put those on a queue and the request returns in
milliseconds. This is the single highest-value use of
the pattern, and it needs no new architecture — just
[[Message Queues]] and a worker.

## Distributed serverless

Take that further and the whole system becomes
producers, a bus, and small consumers that scale to zero:

```text
API Gateway -> Lambda (accept, validate, enqueue)
                 |
             EventBridge / SQS
             /        |        \
     resize      email       index
     worker      worker      worker
```

Each consumer scales independently, costs nothing idle,
and fails without taking the others down. On AWS that is
[[AWS Lambda]] + [[Amazon API Gateway]] + SQS or
EventBridge; on Cloudflare, Workers plus Queues.

## What you trade away

- **Traceability.** A single user action becomes six
  invocations across four services. Without correlation
  IDs and [[Monitoring and Alerting]] you are blind.
- **Ordering.** Events arrive out of order. Assume it.
- **At-least-once delivery.** Every consumer must be
  **idempotent** — processing `order.paid` twice must
  not charge twice. This is the rule people learn late
  and expensively.
- **Local development.** "Run the whole system on my
  laptop" stops being simple.
- **Debugging by reading code.** The call graph is no
  longer in the code; it is in the subscriptions.

## Doing it properly

- Start with **one queue and one worker**, in the
  monolith. That covers 90% of the benefit.
- Make every consumer idempotent, keyed on an event ID.
- Give every queue a **dead-letter queue** on day one,
  and alert on its depth — a silent DLQ is a silent
  outage.
- Version your event payloads; consumers outlive
  producers.
- Keep the request path synchronous where the user is
  waiting for an answer. Async is for work, not replies.

## Related

[[Message Queues]] · [[Serverless Architecture]] ·
[[AWS Lambda]] · [[RabbitMQ]] · [[Redis]] ·
[[Monitoring and Alerting]] · [[Sticky Sessions]] ·
[[Anti-Patterns]]

## Sources

- [[aws-lambda-welcome]] ·
  [[rabbitmq-tutorial-work-queues]]
