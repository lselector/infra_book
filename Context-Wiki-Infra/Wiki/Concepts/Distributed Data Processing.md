---
type: Concept
title: "Distributed Data Processing"
description: "Splitting a dataset across a cluster - what Spark does, what it costs, and the single machine you should try first."
wikipedia: "https://en.wikipedia.org/wiki/Distributed_computing"
tags: [data, scaling, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Distributed Data Processing

When one machine cannot hold or chew through the data,
you split it across many. The data is partitioned, each
worker processes its own partitions, and results are
combined. [[Apache Spark]] is the engine most people
mean by this; [[Databricks]] is the managed platform
built around it.

## The mental model

```text
read  -> partitions spread over workers   (parallel, cheap)
map   -> filter, project, derive columns  (parallel, cheap)
shuffle -> rows move between workers      (network, EXPENSIVE)
reduce -> group, join, aggregate          (after the shuffle)
write -> one file per partition           (parallel)
```

Everything you need to know about performance lives in
that middle line. **Narrow** operations (filter, select)
happen where the data already is. **Wide** operations
(`groupBy`, `join`, `distinct`, `orderBy`) force a
*shuffle* — every worker sends rows across the network
to every other. Fast queries are the ones that shuffle
little, late, and on already-reduced data.

## What it buys, and what it charges

**Buys:** datasets larger than any single machine;
horizontal throughput; fault tolerance mid-job.

**Charges:**

- **A cluster.** Start-up latency, idle cost, version
  drift, a scheduler to run jobs on it.
- **Debugging by stack trace across executors**, which
  is not debugging as you know it.
- **A floor on latency.** Sub-second answers are not
  what this is for.
- **A skill.** Skew, partition counts, broadcast joins,
  caching — real expertise, learned on real bills.

## Try one machine first. Seriously.

This is the same argument as the rest of this wiki, in a
different costume. A 128 GB VM plus [[Polars]] or
[[DuckDB]] over Parquet on [[Object Storage]] handles
tens to hundreds of gigabytes, finishes in seconds, and
costs a few hundred dollars a month with nothing to
operate. Most "big data" is not.

**Climb when:** the data genuinely does not fit or
finish on the biggest single machine you can rent, or
several teams need governed access to the same tables.

## If you do climb

- Store **Parquet** on object storage, partitioned by
  the column you filter on most (usually a date).
- Keep the cluster **ephemeral** — spin up per job,
  terminate after. Idle clusters are how data budgets
  die ([[Cost Control]]).
- Push filters as early as possible; broadcast the small
  side of a join.
- Keep transformation code in version control and
  scheduled, not in a notebook someone runs by hand.

## Related

[[Apache Spark]] · [[Databricks]] · [[DataFrames]] ·
[[Polars]] · [[DuckDB]] · [[Object Storage]] ·
[[Database Sharding]] · [[Cost Control]] ·
[[Anti-Patterns]]

## Sources

- Upstream documentation: the Apache Spark programming
  guide and the Databricks lakehouse documentation. Not
  part of the downloaded `Raw/` corpus — no capture to
  cite yet.
