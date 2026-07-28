---
type: Concept
title: "Failure Modes"
description: "The ten ways systems actually break in production - each with the signal that shows it and the fix that ends it."
wikipedia: "https://en.wikipedia.org/wiki/Fault_tolerance"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Failure Modes

Outages are not infinitely varied. Nearly all of them are
one of a small number of shapes, repeated across
different components. Learning the shapes is worth more
than learning any one component, because the shape tells
you where to look while the site is down.

## The ten

| # | Failure | One-line signature |
|---|---|---|
| 1 | [[Single Point of Failure]] | One thing dies, everything dies |
| 2 | [[Cascading Failure]] | One thing dies, the survivors die of the load |
| 3 | [[Retry Storm]] | The clients finish off what the outage started |
| 4 | [[Cache Stampede]] | One key expires, every request hits the origin |
| 5 | [[Hot Partition]] | One shard, one key, one tenant does all the work |
| 6 | [[Replication Lag]] | The read replica answers with yesterday |
| 7 | [[Duplicate Processing]] | The same job runs twice, the customer is charged twice |
| 8 | [[Queue Backlog]] | Producers outpace consumers, latency grows without bound |
| 9 | [[Poison Message]] | One bad item stops the whole queue, forever |
| 10 | [[Split Brain]] | Two nodes both believe they are the primary |

## Why they repeat

Each is a normal, correct behaviour that stops being
correct under a condition nobody tested:

- **Retries** are right when failures are independent and
  catastrophic when they are correlated.
- **Caches** are right until the moment they are empty.
- **Replicas** are right until someone reads their own
  write.
- **Queues** are right until the consumer is slower than
  the producer for longer than the queue is deep.

The component behaves exactly as documented. The system
does not.

## Which of these you can actually have

At rungs 1–4 of [[Stacks]] — static hosting, a build
script, a form endpoint — most of this list is
unreachable. There is no replica to lag, no queue to
back up, no partition to get hot. That is the strongest
argument in [[The Ladder]] for staying low: each rung
you climb adds failure modes as surely as it adds
capability.

The first three arrive with the first server (rung 5):
single point of failure, retry storm, and — once there
is a cache — stampede. Replication lag and split brain
need a second copy of the data. Duplicate processing,
backlog and poison messages arrive with the first queue.

## The four fixes that cover most of it

1. **Timeouts everywhere, always.** An unbounded wait
   converts a slow dependency into an outage. This one
   fix touches items 2, 3 and 8.
2. **Retries with exponential backoff and jitter, and a
   budget** — never a bare retry loop (items 2, 3).
3. **Idempotency keys** on anything that costs money or
   sends mail ([[Idempotency]], items 7 and 9).
4. **A limit on everything unbounded** — queue depth,
   in-flight requests, connection pool size, payload
   size, retry count.

## Finding out before your users do

Watch saturation and queue depth, not just error rate —
a system in trouble is usually still returning 200s while
its queues grow ([[Monitoring and Alerting]]). Define what
"working" means in numbers ([[Service Level Objectives]]),
and rehearse the failures deliberately rather than
waiting for them ([[Chaos Engineering]]). When one
happens anyway, [[Incident Response]] is the part you
practise in advance.

## Related

[[Single Point of Failure]] · [[Cascading Failure]] ·
[[Retry Storm]] · [[Cache Stampede]] ·
[[Hot Partition]] · [[Replication Lag]] ·
[[Duplicate Processing]] · [[Queue Backlog]] ·
[[Poison Message]] · [[Split Brain]] ·
[[Idempotency]] · [[Chaos Engineering]] ·
[[Monitoring and Alerting]] ·
[[Service Level Objectives]] · [[Incident Response]] ·
[[Anti-Patterns]] · [[The Ladder]]

## Sources

- [[aws-well-architected-reliability]] ·
  [[aws-well-architected-framework]] ·
  [[sre-book-index]] · [[sre-book-monitoring]] ·
  [[sre-book-slos]]
