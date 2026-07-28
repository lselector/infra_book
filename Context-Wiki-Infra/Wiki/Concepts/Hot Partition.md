---
type: Concept
title: "Hot Partition"
description: "One shard, key or tenant taking most of the traffic - why adding machines does not help, and how to spread the load."
wikipedia: "https://en.wikipedia.org/wiki/Partition_(database)"
tags: [storage-and-databases, reliability, scaling]
timestamp: "2026-07-28T00:00:00Z"
---

# Hot Partition

Work is split across partitions, but the split is uneven:
one partition receives a large share of the reads or
writes, saturates, and becomes the limit for the whole
system while the others idle. Failure mode 5 of
[[Failure Modes]].

## How the key choice creates it

The partition key decides everything:

| Key | What goes wrong |
|---|---|
| Timestamp or auto-increment ID | Every new write lands on the newest partition; that one is always hot |
| Country, when 80% of users are in one | Permanently skewed |
| Tenant ID in a [[Multi-Tenant SaaS]] | One large customer outweighs the other 500 |
| Status flag (`pending`/`done`) | Two values, so effectively two partitions |
| A single celebrity row | Everyone reads the same product, post or account |

The pattern: **any key with few distinct values, or with
a heavy head, produces a hot partition.**

## Fixes

- **Choose a high-cardinality, evenly-distributed key.**
  A hash of the ID rather than the ID itself; a random
  suffix rather than a timestamp prefix.
- **Salt the hot key.** Split `product:42` into
  `product:42:0..9`, write to a random one, read all ten
  and merge. Ugly, effective, and reversible.
- **Cache the head.** A handful of hot rows served from
  [[Redis]] or a [[Content Delivery Network]] removes
  the skew from the database entirely — mind
  [[Cache Stampede]] on exactly those keys.
- **Isolate the outlier.** In multi-tenant systems, give
  the one enormous customer its own database. This is
  usually cheaper than re-architecting for everybody.

## Where it shows up without any sharding

You do not need [[Database Sharding]] to have this.
Skew appears in ordinary systems as:

- One [[PostgreSQL]] table partition
  (`postgresql-partitioning`) taking all inserts.
- One key in [[Redis]] holding a million-element list.
- One [[Apache Spark]] task running for an hour while 199
  finish in seconds — data skew is the same failure.
- One object-storage prefix, which throttles per prefix.
- One row locked by every transaction (a counter, a
  sequence, an inventory total).

## The signal

Per-partition or per-key metrics, not averages. An
average CPU of 30% across ten nodes is consistent with
one node at 100% — and that node is your ceiling. If your
dashboard cannot show the distribution, it cannot show
this failure.

## Related

[[Failure Modes]] · [[Database Sharding]] ·
[[Read Replicas]] · [[Cache Stampede]] ·
[[Multi-Tenant SaaS]] · [[PostgreSQL]] · [[Redis]] ·
[[Apache Spark]] · [[Distributed Data Processing]] ·
[[Monitoring and Alerting]]

## Sources

- [[postgresql-partitioning]] ·
  [[azure-multitenant-storage-data]] ·
  [[azure-multitenant-tenancy-models]] ·
  [[aws-well-architected-reliability]]
