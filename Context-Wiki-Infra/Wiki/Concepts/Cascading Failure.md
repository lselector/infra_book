---
type: Concept
title: "Cascading Failure"
description: "One component fails, its load moves to the others, and they fail in turn - the outage that spreads."
wikipedia: "https://en.wikipedia.org/wiki/Cascading_failure"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Cascading Failure

A failure that propagates: losing one instance shifts its
work onto the survivors, which pushes them past their own
limits, and the system unravels faster than it degrades.
Failure mode 2 of [[Failure Modes]].

## The shape

Three app servers at 70% CPU look healthy. One dies. The
remaining two now need 105% each. They slow, health
checks time out, the [[Load Balancing]] layer marks them
unhealthy and removes them — and now nothing is serving,
including the instance that would have recovered.

The distinguishing feature is that **the system cannot
recover on its own after the trigger goes away**. Restore
the failed instance and it is immediately buried by the
backlog that built up while it was gone.

## What makes it possible

- **No headroom.** Running N instances that need all N.
- **Unbounded queues and connection pools.** Work piles
  up instead of being rejected, so latency grows without
  limit — see [[Queue Backlog]].
- **No timeouts.** A thread waiting forever on a slow
  dependency is a thread not serving anyone.
- **Retries without a budget** — the amplifier that turns
  a partial failure into a total one ([[Retry Storm]]).
- **Health checks that fail under load** rather than
  measuring liveness, so overload gets misdiagnosed as
  death.

## The controls, in order of value for the money

1. **Timeouts on every outbound call**, shorter than the
   caller's own deadline. This is free and prevents more
   cascades than anything else.
2. **Load shedding.** Return 503 fast when saturated.
   A rejected request costs almost nothing; a queued one
   costs a thread and makes things worse.
3. **Circuit breakers.** After N consecutive failures,
   stop calling the dependency for a while and serve a
   degraded answer. It gives the dependency room to
   recover — which it will never get while you hammer it.
4. **Bulkheads.** Separate connection pools per
   dependency, so a slow payment API cannot consume every
   worker and take the login page down with it.
5. **Headroom.** Size for N-1 instances, not N.
6. **Graceful degradation.** Serve stale cache, hide the
   recommendations panel, disable search — decide in
   advance which features may be dropped.

## Watch out for

**Restart alone rarely fixes it.** A cascade that started
from overload restarts straight back into the same
overload. You have to shed load first — drop traffic,
pause consumers, disable the expensive feature — then
bring capacity back, then restore traffic.

**Microservices multiply the paths.** Every synchronous
call between services is a new route for a cascade, which
is a large part of the
[[Anti-Patterns|microservice premium]] a small team pays.

## Related

[[Failure Modes]] · [[Retry Storm]] · [[Queue Backlog]] ·
[[Single Point of Failure]] · [[Load Balancing]] ·
[[Sticky Sessions]] · [[Connection Pooling]] ·
[[Monitoring and Alerting]] · [[Incident Response]] ·
[[Anti-Patterns]] · [[Chaos Engineering]] ·
[[Rate Limiting]]

## Sources

- [[aws-well-architected-reliability]] ·
  [[sre-book-index]] · [[sre-book-monitoring]] ·
  [[martinfowler-microservice-premium]]
