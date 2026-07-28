---
type: Tool
title: "pandas"
description: "The default Python DataFrame library - the one everything else integrates with."
wikipedia: "https://en.wikipedia.org/wiki/Pandas_(software)"
tags: [data, python, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# pandas

The Python data analysis library: `DataFrame`, `Series`,
and twenty years of accumulated methods for reading,
reshaping, joining and summarising tables.

```python
import pandas as pd

df = pd.read_parquet("events.parquet")
top = (df[df["event"] == "purchase"]
       .groupby("country", as_index=False)["amount"]
       .sum()
       .sort_values("amount", ascending=False)
       .head(10))
```

## Why it is still the default

Not speed. Reach: every plotting library, every ML
framework, every database driver, every tutorial and
every LLM's training data speaks pandas. When you need
one library that connects to everything, this is it.

## Watch out for

- **Memory.** The rule of thumb is 5–10x the file size
  in RAM for a CSV. Read Parquet, select only the
  columns you need, and set dtypes explicitly.
- **`SettingWithCopyWarning`.** It means what it says:
  you may be writing to a view. Use `.loc` for
  assignment and stop ignoring it.
- **Silent dtype coercion.** A single null turns an int
  column into float64; a mixed column becomes `object`
  and everything slows to Python speed. PyArrow-backed
  dtypes (`dtype_backend="pyarrow"`) fix most of this.
- **Single-threaded by default.** One core, however many
  the machine has. This is where [[Polars]] wins.
- **Chained `apply`.** A Python function per row is
  hundreds of times slower than a vectorised column
  operation.

## When to reach for something else

- Data too big for RAM, or too slow: [[Polars]].
- You would rather write SQL, or need out-of-core joins:
  [[DuckDB]] — and it reads pandas DataFrames in place.
- Genuinely does not fit on one machine:
  [[Apache Spark]] (see [[Distributed Data Processing]]
  before believing that).

All of them share the [[Apache Arrow]] memory format, so
the move is incremental rather than a rewrite.

## Related

[[DataFrames]] · [[Polars]] · [[DuckDB]] ·
[[Apache Arrow]] · [[uv]] · [[Apache Spark]]

## Sources

- Upstream documentation: <https://pandas.pydata.org/docs/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
