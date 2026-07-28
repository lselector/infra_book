---
type: Concept
title: "Replication Lag"
description: "The replica is behind the primary - the bug where a user saves a change and the next page says it never happened."
wikipedia: "https://en.wikipedia.org/wiki/Replication_(computing)"
tags: [storage-and-databases, reliability, scaling]
timestamp: "2026-07-28T00:00:00Z"
---

# Replication Lag

A replica applies the primary's changes some time after
they are committed. During that window, reads from the
replica return older data. Failure mode 6 of
[[Failure Modes]].

Normally the lag is milliseconds. It becomes an outage
when it grows to minutes and nobody notices.

## The bug users actually report

> "I updated my profile and it reverted."

The write went to the primary; the redirect read from a
replica that had not caught up yet. This is
**read-your-own-writes** violation, and it is the single
most common consequence of adding [[Read Replicas]].

The fix is not more replicas. It is routing: **after a
user writes, read that user from the primary** for a
short window (a session flag, a cookie, or a timestamp
comparison). Everyone else can keep reading the replica.

## What makes lag grow

- **A bulk write** — a migration, a backfill, a mass
  delete. The primary applies it in parallel; a replica
  replaying single-threaded cannot keep up.
- **A long-running query on the replica** blocking
  replay.
- **A slow or saturated network link**, especially
  cross-region.
- **The replica being under-provisioned** relative to the
  primary. Replicas need comparable hardware; they are
  doing the same writes.

## What to do about it

- **Monitor lag as a first-class metric**, with an alert
  ([[Monitoring and Alerting]]). Seconds of lag, not
  bytes.
- **Route deliberately.** Analytics, reports, exports and
  search: replica. Anything the user just changed:
  primary. Anything a decision depends on — balances,
  entitlements, stock levels: primary.
- **Throttle bulk operations** into batches with pauses,
  and watch lag while they run.
- **Fail closed on lag.** If lag exceeds a threshold,
  send reads back to the primary rather than serving
  visibly wrong data.

## The failover connection

Lag is also data loss. With asynchronous replication, if
the primary dies, everything not yet replicated is gone —
that is the recovery point objective (RPO) you actually
have, whatever the plan says. Synchronous replication
removes the loss and adds latency to every write; it is a
deliberate trade, not a default. Promoting a lagging
replica while the old primary is merely unreachable is
how you get [[Split Brain]].

## Related

[[Failure Modes]] · [[Read Replicas]] ·
[[Split Brain]] · [[Database Backups]] ·
[[PostgreSQL]] · [[Connection Pooling]] ·
[[Monitoring and Alerting]] · [[Database Sharding]]

## Sources

- [[postgresql-warm-standby]] · [[aws-rds-what-is]] ·
  [[aws-well-architected-reliability]] ·
  [[postgresql-runtime-config-connection]]
