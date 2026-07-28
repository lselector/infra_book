---
type: Tool
title: "Apache Arrow"
description: "The columnar memory format every modern data tool shares - why moving between them is free."
wikipedia: "https://en.wikipedia.org/wiki/Apache_Arrow"
tags: [data, foundations, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Apache Arrow

A language-independent specification for how columnar
data sits in memory, plus implementations in a dozen
languages. It is infrastructure for data tools rather
than a tool you run.

## Why you should care

Before Arrow, handing a table from Python to a database
driver to a query engine meant serialising and copying
at each boundary — often the largest cost in the
pipeline. Tools that speak Arrow share the same memory
layout, so the handoff is a pointer.

That is why [[Polars]], [[DuckDB]], [[pandas]] (with
`dtype_backend="pyarrow"`), [[Apache Spark]] and every
modern warehouse client interoperate at no copy cost —
and why "switch from pandas to Polars" is an incremental
change rather than a rewrite.

## What you actually touch

- **Parquet** — the on-disk companion format. Typed,
  columnar, compressed; roughly a tenth the size of CSV
  and far faster to scan. Store data this way.
- **pyarrow** — the Python package underneath most of
  the above; you will see it in your lockfile whether or
  not you import it.
- **Arrow Flight** — a wire protocol for moving Arrow
  batches between processes, when a network hop is
  unavoidable.

## The practical rule

Store Parquet in [[Object Storage]], query it with
whichever Arrow-native engine suits the job, and stop
converting between formats. Most "we need a data
platform" conversations end here.

## Related

[[DataFrames]] · [[Polars]] · [[DuckDB]] · [[pandas]] ·
[[Apache Spark]] · [[Object Storage]] ·
[[Distributed Data Processing]]

## Sources

- Upstream documentation: <https://arrow.apache.org/docs/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
