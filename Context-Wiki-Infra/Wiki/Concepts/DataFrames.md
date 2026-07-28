---
type: Concept
title: "DataFrames"
description: "Tables in memory, on one machine - where every data problem should start, and how far it now goes."
tags: [data, foundations, python]
timestamp: "2026-07-28T00:00:00Z"
---

# DataFrames

A DataFrame is a table held in memory with named,
typed columns: read a file, filter, group, join, write.
It is the interface almost all data work happens
through, and — this is the part people get wrong — it
runs perfectly well on one machine for datasets far
larger than most projects will ever have.

## The three you will meet

| | Use it when |
|---|---|
| [[pandas]] | The ecosystem answer. Everything integrates with it; every tutorial assumes it |
| [[Polars]] | The same job, multi-threaded and lazy, on data that made pandas swap |
| [[DuckDB]] | You would rather write SQL over files, with joins and aggregates that spill to disk |

All three read and write the same [[Apache Arrow]]
memory layout, so moving between them is cheap and does
not mean rewriting the pipeline.

## The sizing rule that saves the most money

A modern VM takes 64–256 GB of RAM for a few hundred
dollars a month. Columnar formats (Parquet) plus
predicate pushdown mean you rarely load all of it.

So: **one machine handles tens of gigabytes
comfortably, and hundreds with care.** Reach for
[[Distributed Data Processing]] when a single machine
genuinely cannot finish the job — not when the dataset
sounds big. A [[Polars]] query on one box regularly
beats a small [[Apache Spark]] cluster on the same data,
because there is no shuffle and no cluster to start.

## Habits worth having

- **Parquet, not CSV**, for anything you store. Typed,
  columnar, compressed, ~10x smaller and faster to scan.
- **Lazy over eager.** `scan_parquet` + filter lets the
  engine skip data it never reads; `read_parquet` does
  not.
- **Pin your versions** in `pyproject.toml` and let
  [[uv]] lock them — data pipelines break silently on
  minor upgrades.
- **Keep transformations in a script, not a notebook.**
  Notebooks are for looking; [[Static Build Pipeline]]
  is the model for anything that must run twice.

## Related

[[pandas]] · [[Polars]] · [[DuckDB]] ·
[[Apache Arrow]] · [[Distributed Data Processing]] ·
[[Apache Spark]] · [[Object Storage]] · [[uv]] ·
[[Anti-Patterns]]

## Sources

- Upstream documentation: pandas, Polars, DuckDB and
  Apache Arrow user guides. Not part of the downloaded
  `Raw/` corpus — no capture to cite yet.
