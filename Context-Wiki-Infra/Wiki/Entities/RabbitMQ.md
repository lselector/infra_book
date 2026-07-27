---
type: Tool
title: "RabbitMQ"
description: "A real message broker - for when a database table or Redis list is no longer enough."
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# RabbitMQ

A message broker implementing AMQP, with exchanges,
routing keys, acknowledgements and dead-letter queues.

## What it gives over simpler options

- Delivery acknowledgement and redelivery on failure.
- Routing and fan-out to multiple consumers.
- Dead-letter queues for messages that keep failing.
- Backpressure and prefetch control.

## When it is justified

When work must not be lost, when several different
consumers need the same events, or when you need routing
logic. Below that, a table in [[PostgreSQL]] or a
[[Redis]] list is less to operate and entirely adequate —
see [[Message Queues]].

## Watch out for

- Another stateful service to run, monitor and back up.
- Consumers must be idempotent: at-least-once delivery
  means duplicates will happen.
- Unacknowledged messages accumulate; monitor queue
  depth via [[Monitoring and Alerting]].

## Related

[[Message Queues]] · [[Redis]] ·
[[Transactional Email]] · [[Monitoring and Alerting]]

## Sources

- [[rabbitmq-tutorial-work-queues]]
