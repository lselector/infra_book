---
type: Tool
title: "Apache Spark"
description: "The distributed processing engine - what you move to when one machine genuinely cannot finish the job."
wikipedia: "https://en.wikipedia.org/wiki/Apache_Spark"
tags: [data, scaling, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Apache Spark

An open-source engine for processing data across a
cluster. You write what looks like ordinary DataFrame or
SQL code; Spark builds a plan, splits the data into
partitions, and runs the work on many machines.

## The parts you interact with

- **DataFrame / Dataset API** — the everyday interface,
  in Python (PySpark), Scala, Java or R.
- **Spark SQL** — the same engine, queried as SQL.
- **Structured Streaming** — the same code over an
  unbounded input.
- **Catalyst / Tungsten** — the query optimiser and
  execution layer that make declarative code fast.

```python
df = spark.read.parquet("s3://bucket/events/")
(df.filter(df.event == "purchase")      # narrow, cheap
   .groupBy("country")                   # wide - shuffle
   .sum("amount")
   .write.parquet("s3://bucket/out/"))
```

## Where it runs

Databricks, EMR, Dataproc, Kubernetes, or a standalone
cluster you operate. Managed is worth the premium here
more than almost anywhere else in this wiki — a
self-run Spark cluster is a job, not a task
([[Databricks]] exists precisely because of this).

## Watch out for

- **Shuffles.** `groupBy`, `join`, `distinct` and
  `orderBy` move rows between machines; everything about
  performance follows from how much you shuffle and how
  late. Broadcast the small side of a join.
- **Data skew.** One key with 80% of the rows means one
  worker doing 80% of the work while the cluster idles.
- **Idle clusters.** The most common Spark invoice is
  for a cluster that ran nothing. Make them ephemeral
  and auto-terminating ([[Cost Control]]).
- **Small files.** Thousands of tiny Parquet files cost
  more in listing than in reading. Compact them.
- **Using it at all.** For tens of gigabytes,
  [[Polars]] or [[DuckDB]] on one box will be simpler
  and often faster — see [[DataFrames]].

## Related

[[Distributed Data Processing]] · [[Databricks]] ·
[[Apache Arrow]] · [[Polars]] · [[DuckDB]] ·
[[Object Storage]] · [[Amazon S3]] · [[Kubernetes]] ·
[[Cost Control]]

## Sources

- Upstream documentation: <https://spark.apache.org/docs/latest/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
