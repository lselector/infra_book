---
type: Concept
title: "Read Replicas"
description: "Copies of the database that serve reads - the first real scaling step, with a lag you must design around."
wikipedia: "https://en.wikipedia.org/wiki/Replication_(computing)"
tags: [storage-and-databases, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Read Replicas

A streaming copy of the primary database that accepts
queries but not writes.

## Why it matters here

Most applications read far more than they write. Sending
reports, dashboards and search to a replica takes load off
the primary without sharding anything. It is also a warm
standby, which improves your recovery story.

## The thing that catches everyone

**Replication lag.** A write to the primary is not
instantly visible on the replica. Read-after-write on a
replica shows the user stale data — they save a form and
see the old value. Route reads that must reflect a
just-completed write back to the primary.

## Before you reach for it

Check that the slow query is not simply missing an index,
and that a cache would not do. Replicas add operational
surface; indexes do not.

## Related

[[Relational Databases]] · [[PostgreSQL]] ·
[[Connection Pooling]] · [[Database Sharding]] ·
[[Caching]]

## Sources

- [[postgresql-warm-standby]] ·
  [[postgresql-partitioning]] ·
  [[aws-well-architected-reliability]]
