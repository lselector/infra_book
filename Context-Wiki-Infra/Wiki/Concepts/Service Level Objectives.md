---
type: Concept
title: "Service Level Objectives"
description: "A target for reliability you actually intend to meet, and the error budget it implies."
tags: [ops-and-security, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Service Level Objectives

An SLO is a stated target — say 99.5% of requests
succeeding over 30 days. The gap between that and 100% is
your error budget.

## Why the number matters

It converts an argument into arithmetic. 99.9% permits
about 43 minutes of downtime a month; 99.99% permits four.
The second costs an order of magnitude more to deliver and
usually requires abandoning [[One-Box Deployment]]
entirely.

## Why it matters here

- Most small projects should explicitly *not* target four
  nines. Saying so out loud stops well-meaning
  over-engineering.
- It gives [[Monitoring and Alerting]] a threshold to
  alert against that means something.
- Availability commitments appear in enterprise contracts
  and in the availability criterion of
  [[Trust Services Criteria]] — better to choose the
  number than inherit it.

## Related

[[Monitoring and Alerting]] · [[Incident Response]] ·
[[SOC 2]] · [[Cost Control]]

## Sources

- [[sre-book-slos]] · [[sre-book-monitoring]] ·
  [[aws-well-architected-reliability]]
