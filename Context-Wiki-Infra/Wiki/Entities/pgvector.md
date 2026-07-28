---
type: Tool
title: "pgvector"
description: "Vector similarity search as a PostgreSQL extension - the reason most small teams do not need a vector database."
website: "https://github.com/pgvector/pgvector"
tags: [ai-in-saas, storage-and-databases]
timestamp: "2026-07-28T00:00:00Z"
---

# pgvector

An open-source [[PostgreSQL]] extension that adds vector
column types, distance operators and approximate-nearest-
neighbour indexes. Embeddings live in an ordinary table,
beside the row they describe, queried with ordinary SQL.

For a small SaaS adding
[[Retrieval-Augmented Generation]], this is almost always
the right answer: no second datastore to run, back up,
secure and keep in sync.

## Using it

```sql
CREATE EXTENSION vector;

CREATE TABLE doc_chunks (
    id         bigserial PRIMARY KEY,
    tenant_id  bigint NOT NULL,
    source     text,
    chunk      text,
    embedding  vector(1536)
);

CREATE INDEX ON doc_chunks
  USING hnsw (embedding vector_cosine_ops);
```

Then retrieval is a `SELECT` with an `ORDER BY` on the
distance operator (`<=>` cosine, `<->` L2, `<#>` inner
product) and a `LIMIT`. Crucially, the tenant filter is
just another `WHERE` clause in the same query — the thing
a separate vector database makes awkward, and the thing
that most needs to be right ([[Multi-Tenant SaaS]]).

## Index choice

| Index | Build | Recall | Notes |
|---|---|---|---|
| none | instant | exact | fine up to tens of thousands of rows |
| IVFFlat | fast | tunable | needs data present before building |
| HNSW | slower, more memory | better | the usual default now |

Both approximate indexes trade recall for speed and have
a query-time knob to trade back. Measure on your own data
rather than trusting a benchmark.

## Watch out for

- **Dimensions are fixed per column**, and vectors from
  different embedding models are not comparable. Changing
  model means re-embedding everything — record which
  model produced each row.
- **Storage adds up.** 1536 floats is ~6 KB per row
  before the index; a million chunks is a real disk and
  memory bill ([[Cost Control]]).
- **Index build wants memory.** Watch
  `maintenance_work_mem` on a small VPS
  ([[One-Box Deployment]]).
- **It is not a search engine on its own.** Combine with
  PostgreSQL full-text search for names, codes and exact
  strings; pure vector search is bad at identifiers.
- **Managed availability varies.** Most hosted Postgres
  offerings include it now, but check before committing
  ([[Amazon RDS]], [[Managed PaaS]]).
- **Keep the source text**, not just the vector. You send
  the text to the model, and you cannot invert an
  embedding.

## Related

[[Retrieval-Augmented Generation]] · [[PostgreSQL]] ·
[[Multi-Tenant SaaS]] · [[AI Assistant Panel]] ·
[[Relational Databases]] · [[Database Backups]] ·
[[LLM API Integration]] · [[Anti-Patterns]]

## Sources

- [[pgvector-readme]] · [[postgresql-tutorial-start]] ·
  [[postgresql-partitioning]] ·
  [[azure-multitenant-storage-data]]
