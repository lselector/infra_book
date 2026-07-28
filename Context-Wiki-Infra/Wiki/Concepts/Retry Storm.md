---
type: Concept
title: "Retry Storm"
description: "Every client retrying at once - how a brief blip becomes a sustained outage, and the three lines that prevent it."
wikipedia: "https://en.wikipedia.org/wiki/Exponential_backoff"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Retry Storm

A short failure causes every client to retry, the retries
arrive together and exceed the capacity that was already
insufficient, and the service never gets a quiet moment
in which to recover. Failure mode 3 of [[Failure Modes]].

## Why retries multiply

Retries stack. If the browser retries 3 times, calling an
API gateway that retries 3 times, calling a service that
retries 3 times, one user action can become 27 requests
at the backend. Every layer that retries independently
multiplies with every other layer.

Worse, the retries **synchronise**. Clients that failed
at the same instant wait the same interval and return
together, so the load arrives in spikes rather than
spread out — the same self-synchronising herd behind
[[Cache Stampede]].

## The fixes

**Exponential backoff with jitter.** Wait 1s, 2s, 4s, 8s
— each multiplied by a random factor so clients spread
out instead of marching in step. Jitter is the part
people omit and the part that does the work.

```python
delay = min(cap, base * 2 ** attempt)
time.sleep(random.uniform(0, delay))    # full jitter
```

**A retry budget.** Cap retries at a small fraction of
total requests (10% is a common figure). When the budget
is exhausted, fail fast — the system is not having a
transient blip, it is broken, and retrying is making it
worse.

**Retry at one layer only.** Pick the layer that knows
enough to be useful, usually the outermost caller, and
turn retries off everywhere else. Many SDKs retry by
default; check yours.

**Only retry what is retryable.** 503, 429 and connection
timeouts, yes. 400, 401 and 422 will fail identically
forever. Honour `Retry-After` when the server sends it.

**Only retry what is safe to repeat.** A retried POST
that charges a card is [[Duplicate Processing]]; make it
idempotent first ([[Idempotency]]).

## On the server side

You cannot fix other people's clients — mobile apps ship
their retry policy and keep it for years. So defend:
rate-limit per client, return 429 with `Retry-After`
rather than timing out, and shed load early
([[Cascading Failure]]). A fast rejection is a gift to
both sides; a slow timeout is what keeps the storm going.

## Watch out for

**Health-check retries and cron.** Every monitor,
sidecar and scheduled job that retries on failure joins
the storm. And jobs scheduled at `0 * * * *` are already
synchronised before anything goes wrong — stagger them.

## Related

[[Failure Modes]] · [[Cascading Failure]] ·
[[Cache Stampede]] · [[Duplicate Processing]] ·
[[Idempotency]] · [[Queue Backlog]] ·
[[Monitoring and Alerting]] · [[HTTP]]

## Sources

- [[aws-well-architected-reliability]] ·
  [[sre-book-index]] · [[mdn-http-overview]]
