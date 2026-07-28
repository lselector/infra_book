---
type: Concept
title: "Split Brain"
description: "Two nodes both convinced they are the primary - the failure that corrupts data rather than stopping it."
wikipedia: "https://en.wikipedia.org/wiki/Split-brain_(computing)"
tags: [storage-and-databases, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Split Brain

A network partition separates the nodes of a cluster.
Each side can still see itself but not the other, each
concludes the other has died, and both start acting as
the primary. Failure mode 10 of [[Failure Modes]].

It is the worst item on this list, because the others
stop the system while this one keeps it running and
quietly diverges the data. Both halves accept writes;
neither is wrong; the two histories cannot be merged
afterwards by any automatic rule.

## The root cause

**A node cannot distinguish "the other node is down" from
"I cannot reach the other node."** No amount of health
checking fixes this — it is a property of networks, not
of implementations. What you can do is arrange for only
one side to be *allowed* to act.

## The standard defences

- **Quorum.** Require a majority to elect a leader.
  With three nodes, the side with two proceeds and the
  side with one steps down. This is why cluster sizes are
  odd, and why two nodes is the worst possible number: a
  partition gives 1 and 1, and neither has a majority.
- **A witness / tiebreaker.** A cheap third node whose
  only job is to make the count odd.
- **Fencing (STONITH).** Before promoting a new primary,
  forcibly cut the old one off — revoke its storage
  access, take its IP, power it off. "Shoot the other
  node in the head" is a crude name for a necessary step.
- **Leases with expiry.** Leadership is a time-limited
  lease that must be renewed. If a node cannot renew, it
  demotes itself before anyone else may take over.
- **Manual promotion.** For a small system, the safest
  policy is often that a human decides. It costs minutes
  of downtime and saves a divergence you cannot repair.

## What this means for a small product

Do not build automatic failover for a single-node
[[PostgreSQL]] until you have a real availability
requirement. A primary with a warm standby that is
promoted *by a person* is a supported, well-understood
configuration. Automatic promotion needs quorum and
fencing to be safe, and getting that right is a
specialist job — one of the strongest cases in
[[Anti-Patterns]] for buying rather than building: a
managed database ([[Amazon RDS]]) has already solved it.

## Beyond databases

The same failure appears wherever two things could both
act:

- Two schedulers running the same cron job
  ([[Duplicate Processing]]).
- Two load balancers claiming one virtual IP.
- Two Kubernetes control planes on either side of a
  partition ([[Kubernetes]] uses etcd quorum for exactly
  this reason).
- Two application instances holding a lock they took from
  different [[Redis]] nodes.

## Watch out for

**A distributed lock is not a fence.** If a process pauses
long enough — a garbage collection pause, a suspended VM
— its lock can expire while it still believes it holds
it. Locks protect against contention, not against split
brain; only fencing does.

## Related

[[Failure Modes]] · [[Replication Lag]] ·
[[Single Point of Failure]] · [[Read Replicas]] ·
[[Duplicate Processing]] · [[Idempotency]] ·
[[PostgreSQL]] · [[Amazon RDS]] · [[Kubernetes]] ·
[[Container Orchestration]] · [[Anti-Patterns]]

## Sources

- [[postgresql-warm-standby]] · [[kubernetes-overview]] ·
  [[aws-rds-what-is]] ·
  [[aws-well-architected-reliability]]
