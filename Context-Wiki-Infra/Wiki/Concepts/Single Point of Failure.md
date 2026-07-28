---
type: Concept
title: "Single Point of Failure"
description: "The one component whose loss takes everything with it - how to find yours, and when removing it is not worth it."
wikipedia: "https://en.wikipedia.org/wiki/Single_point_of_failure"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Single Point of Failure

A component with no redundancy, whose failure stops the
whole system. Failure mode 1 of [[Failure Modes]].

## Finding yours

Walk a request from DNS to disk and ask of each hop:
*if this stops, what still works?* On a rung-5
[[One-Box Deployment]] the honest answer is a short list
because the single point of failure is the box, and
everything is on it.

Less obvious ones, in rough order of how often they bite:

- **The domain registration.** An expired domain is a
  total outage that no amount of server redundancy
  helps. Auto-renew, and put the renewal card somewhere
  it will not expire first.
- **The DNS provider** ([[Cloudflare DNS]]).
- **One database primary** — universal, and usually
  fine.
- **The deploy path.** If only one person's laptop can
  ship a fix, that laptop is in the critical path
  ([[Git-Driven Deployment]] removes this).
- **The TLS certificate.** Expiry is an outage;
  [[Automatic HTTPS]] removes the human from renewal.
- **One cloud account, one payment method.** A failed
  card can suspend everything.
- **One person who knows how it works.**

## When to leave it alone

Removing a single point of failure means running two of
something, and two of something is not twice the cost —
it is twice the cost plus a coordination problem
([[Split Brain]] is what you buy with a second primary).

For a small product, availability usually improves more
from a tested restore ([[Database Backups]]) and a
15-minute rebuild than from redundancy. "How long to
recreate it?" beats "how do I make it never fail?" until
the revenue arithmetic says otherwise. Compare the two
honestly: five nines of uptime and a database you have
never restored is a worse position than one box you can
rebuild from a script.

## When to remove it

- Revenue per hour of downtime exceeds the monthly cost
  of the redundancy.
- A customer contract names an availability number
  ([[Service Level Objectives]]).
- The failure is *likely*, not merely possible — a disk
  with no backup, a certificate renewed by hand.

Then the ladder is: [[Load Balancing]] across two app
instances (they must be stateless first), a managed
database with automatic failover ([[Amazon RDS]]),
and static assets on a [[Content Delivery Network]] so
the origin is not in every request path.

## Watch out for

**Fake redundancy.** Two app servers sharing one
database, one NFS mount, or one availability zone have
moved the single point, not removed it. And redundancy
you have never failed over to is a hypothesis, not a
control — see [[Chaos Engineering]].

## Related

[[Failure Modes]] · [[Cascading Failure]] ·
[[Split Brain]] · [[Load Balancing]] ·
[[One-Box Deployment]] · [[Database Backups]] ·
[[Service Level Objectives]] · [[Amazon RDS]] ·
[[Content Delivery Network]] · [[Cost Control]]

## Sources

- [[aws-well-architected-reliability]] ·
  [[cloudflare-what-is-load-balancing]] ·
  [[sre-book-index]]
