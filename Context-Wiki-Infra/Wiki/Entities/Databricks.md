---
type: Service
title: "Databricks"
description: "Managed Spark plus a lakehouse - the platform you buy when data processing becomes a team's job."
wikipedia: "https://en.wikipedia.org/wiki/Databricks"
tags: [data, scaling, managed]
timestamp: "2026-07-28T00:00:00Z"
---

# Databricks

The commercial platform built by the creators of
[[Apache Spark]]: managed clusters, notebooks, job
scheduling, a governed table catalog, and the storage
format that ties them together.

## What you are actually buying

| Piece | What it does |
|---|---|
| **Managed compute** | Clusters that start on demand and auto-terminate — no Spark to operate |
| **Delta Lake** | Parquet plus a transaction log: ACID commits, time travel, `MERGE`, schema enforcement |
| **Unity Catalog** | One place for table permissions and lineage across workspaces |
| **Workflows** | Scheduling and dependencies, so pipelines are not cron on someone's laptop |
| **SQL warehouse** | A BI endpoint over the same tables, no copy into a separate warehouse |
| **MLflow** | Experiment tracking and model registry, if you go that way |

The "lakehouse" claim is that files in
[[Object Storage]] plus Delta's transaction log give you
warehouse behaviour without a second copy of the data.
In practice that holds well for analytics, less so for
the sub-second, high-concurrency queries a
[[Relational Databases|relational database]] serves.

## When it is worth it

When several people need governed access to the same
large tables, when pipelines must run on a schedule with
lineage you can show an auditor, and when the cost of
operating Spark yourself exceeds the platform premium.
That is a real threshold — and it is a long way above
where most projects in this wiki live.

## Watch out for

- **Two bills.** DBUs (the platform) *and* the cloud
  VMs underneath. Estimate both.
- **Always-on clusters.** The single largest source of
  surprise invoices. Set auto-termination on everything.
- **Notebook drift.** Production logic living in a
  notebook nobody can review is the data equivalent of
  editing files on the server — keep it in git and
  scheduled ([[Git-Driven Deployment]]).
- **Gravity.** Delta, Unity Catalog and notebooks are
  pleasant and sticky. Keep the raw layer as plain
  Parquet you could read with anything.

## Related

[[Apache Spark]] · [[Distributed Data Processing]] ·
[[Object Storage]] · [[Amazon S3]] · [[Cost Control]] ·
[[DataFrames]] · [[Access Review]]

## Sources

- Upstream documentation: <https://docs.databricks.com>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
