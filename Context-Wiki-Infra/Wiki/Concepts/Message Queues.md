---
type: Concept
title: "Message Queues"
description: "Handing slow work to a background worker so the request can return immediately."
wikipedia: "https://en.wikipedia.org/wiki/Message_queue"
tags: [storage-and-databases, architecture]
timestamp: "2026-07-27T00:00:00Z"
---

# Message Queues

The web process enqueues a job and responds; a separate
worker performs it.

## What belongs on a queue

- Sending email — see [[Transactional Email]]. Never make
  a user wait on an SMTP round trip.
- Image and video processing.
- Report generation, exports, third-party API calls.
- Anything with a retry requirement.

## Why it matters here

It is what keeps a $6 box responsive: slow work moves off
the request path. It also gives you retries and a dead
letter destination for free, which is real reliability.

## Start simple

- A database table as a queue is entirely legitimate at
  low volume, and you already have the database.
- [[Redis]] with a small worker library is the usual next
  step.
- [[RabbitMQ]] when you need routing, fan-out and
  guaranteed delivery semantics.

## Watch out for

Jobs that are not idempotent. Any queue will eventually
deliver a message twice; the worker must tolerate it.

## Related

[[Caching]] · [[Redis]] · [[RabbitMQ]] ·
[[Transactional Email]] · [[Monitoring and Alerting]]

## Sources

- [[rabbitmq-tutorial-work-queues]] ·
  [[redis-data-store-get-started]]
