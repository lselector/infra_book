---
type: Tool
title: "DuckDB"
description: "SQLite for analytics - an in-process column store that queries Parquet on disk or in object storage."
wikipedia: "https://en.wikipedia.org/wiki/DuckDB"
tags: [data, storage-and-databases, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# DuckDB

An embedded, column-oriented database. No server, no
daemon, one dependency — the same deployment story as
[[SQLite]], aimed at analytical queries rather than
transactional ones.

```sql
-- straight over files, nothing loaded first
SELECT country, sum(amount)
FROM 's3://bucket/events/*.parquet'
WHERE event = 'purchase'
GROUP BY country ORDER BY 2 DESC LIMIT 10;
```

It reads Parquet, CSV, JSON, [[pandas]] and [[Polars]]
frames in place via [[Apache Arrow]], spills to disk
when a join exceeds RAM, and uses every core.

## Where it earns its place here

- **Analytics on the app server.** Nightly reports over
  Parquet exports, with nothing new to operate.
- **The step before a warehouse.** Tens of gigabytes
  answered in seconds, for the price of the disk.
- **A build-time query engine.** In a
  [[Static Build Pipeline]], generating pages or JSON
  from a dataset without standing anything up.
- **Reading [[Object Storage]] directly** with the
  `httpfs` extension — no copy, no ETL.

## SQLite or DuckDB?

Same shape, opposite workloads. [[SQLite]] is row-based
and belongs in the request path: many small reads and
writes, one row at a time. DuckDB is column-based and
belongs in the analysis path: few queries, each touching
millions of rows. Using either for the other's job is
slow in a way no amount of indexing fixes.

## Watch out for

- **Not a concurrent multi-writer server.** One process
  writes. It is an *embedded* database.
- **Not for OLTP.** No row-level concurrency story.
- **Version-pin the file format** if you persist a
  `.duckdb` file — the format has changed between
  releases.

## Related

[[DataFrames]] · [[Polars]] · [[pandas]] · [[SQLite]] ·
[[Apache Arrow]] · [[Object Storage]] ·
[[Distributed Data Processing]] · [[Static Build Pipeline]]

## Sources

- Upstream documentation: <https://duckdb.org/docs/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
