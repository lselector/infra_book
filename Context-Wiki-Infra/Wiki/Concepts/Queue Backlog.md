---
type: Concept
title: "Queue Backlog"
description: "Producers outrunning consumers - the failure that hides behind a green dashboard until the queue is hours deep."
wikipedia: "https://en.wikipedia.org/wiki/Message_queue"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Queue Backlog

Work arrives faster than it is processed, so the queue
grows. Nothing errors; everything is simply late, and
gets later. Failure mode 8 of [[Failure Modes]].

## Why it is easy to miss

Every dashboard is green. Requests return 200, the
consumer's error rate is zero, CPU looks fine. The only
symptom is that the welcome email arrives forty minutes
after signup — a customer-visible failure with no failed
request behind it.

**Queue depth and message age are the metrics.** Error
rate will not show this, and neither will latency of the
enqueue call. Alert on *oldest message age*: it is the
number the user experiences.

## The arithmetic

A queue is stable only while `consumers × rate ≥ arrival
rate`. If a consumer handles 10 messages/second and 12
arrive, the queue grows by 2/second forever — 7,200
messages an hour. There is no depth at which it
self-corrects. The backlog ends when you add capacity,
speed the consumer up, or shed work.

Draining takes longer than people expect. Clearing a
100k backlog at a surplus of 5/second takes about five
and a half hours *if nothing new arrives*.

## Causes worth checking first

- A dependency got slower (the API you call now takes
  400ms instead of 40ms), so throughput fell without
  anything failing.
- A [[Poison Message]] blocking a partition, or being
  retried in a loop and consuming all the capacity.
- Consumers scaled to zero, crash-looping, or evicted.
- A burst — a marketing send, a batch import, a retry
  wave from [[Retry Storm]].
- Serialised work: one lock, one connection, one
  partition ([[Hot Partition]]).

## Getting out of one

1. **Stop the inflow** if you can — pause the producer,
   disable the feature.
2. **Add consumers**, if the downstream can take it.
   Adding consumers against a saturated database just
   moves the failure ([[Cascading Failure]]).
3. **Triage the queue.** Not all work is equal: process
   password resets before the nightly digest. A separate
   queue per priority beats one queue with a priority
   field.
4. **Drop what is worthless.** A three-hour-old "typing…"
   notification helps nobody. Decide in advance which
   messages have a shelf life and give them a TTL.

## Designing so it cannot run away

- **Bound the queue.** An unbounded queue converts a
  throughput problem into a memory problem and then an
  outage. Reject or shed at the limit.
- **Backpressure the producer** rather than accepting
  work you cannot do.
- **Autoscale on queue depth**, not CPU — the consumer is
  usually waiting on I/O, so CPU will not trigger.
- **Keep handlers short and idempotent**
  ([[Idempotency]]) so scaling out is safe.

## Related

[[Failure Modes]] · [[Message Queues]] ·
[[Poison Message]] · [[Duplicate Processing]] ·
[[Cascading Failure]] · [[Retry Storm]] ·
[[Hot Partition]] · [[RabbitMQ]] · [[Redis]] ·
[[Event-Driven Architecture]] ·
[[Monitoring and Alerting]] ·
[[Service Level Objectives]]

## Sources

- [[rabbitmq-tutorial-work-queues]] ·
  [[sre-book-monitoring]] · [[sre-book-slos]] ·
  [[aws-well-architected-reliability]]
