---
type: Tool
title: "Polars"
description: "A multi-threaded, lazy DataFrame library in Rust - most of what people start a Spark cluster for, on one machine."
wikipedia: "https://en.wikipedia.org/wiki/Polars_(software)"
tags: [data, python, rust, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Polars

A DataFrame library written in [[Rust]], with Python,
Rust, R and NodeJS bindings. Columnar
([[Apache Arrow]]), multi-threaded by default, and lazy
when you ask it to be.

```python
import polars as pl

top = (pl.scan_parquet("s3://bucket/events/*.parquet")
       .filter(pl.col("event") == "purchase")
       .group_by("country")
       .agg(pl.col("amount").sum())
       .sort("amount", descending=True)
       .head(10)
       .collect())          # nothing ran until here
```

## Why it matters for infrastructure

`scan_parquet` + `collect()` is a **lazy** query: Polars
sees the whole pipeline before executing, so it pushes
the filter down into the file scan, reads only the
columns named, and uses every core. The practical effect
is that datasets which pushed teams onto a cluster now
finish on one VM — which is a rung of [[Stacks]] you do
not have to climb.

## Where it fits against the others

- **vs [[pandas]]** — faster and stricter, with a
  narrower ecosystem. Nulls, types and joins behave
  predictably; there is no index.
- **vs [[DuckDB]]** — much the same performance class.
  Choose by taste: method chains or SQL. They interoperate
  through Arrow at no copy cost.
- **vs [[Apache Spark]]** — no cluster, no shuffle, no
  start-up. Until the data does not fit, this wins.

## Watch out for

- **The API is not pandas.** Expressions, not indexing;
  `pl.col(...)` everywhere. Budget an afternoon.
- **Eager mode gives up the point.** `read_parquet` reads
  everything; `scan_parquet` is where the win lives.
- **Still moving fast.** Pin the version and let [[uv]]
  lock it.
- **Memory is still finite.** Lazy streaming helps, but
  a 500 GB join on a 16 GB box will still fail.

## Related

[[DataFrames]] · [[pandas]] · [[DuckDB]] ·
[[Apache Arrow]] · [[Rust]] · [[Apache Spark]] ·
[[Distributed Data Processing]] · [[uv]]

## Sources

- Upstream documentation: <https://docs.pola.rs>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
