---
type: Concept
title: "Connection Pooling"
description: "Reusing database connections, because opening one is expensive and Postgres has a hard ceiling."
wikipedia: "https://en.wikipedia.org/wiki/Connection_pool"
tags: [storage-and-databases, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Connection Pooling

A pool keeps a small number of database connections open
and hands them to requests as needed.

## Why it matters here

[[PostgreSQL]] allocates a process per connection. A few
hundred is a lot; the default `max_connections` is 100.
Without pooling, a modest traffic spike exhausts them and
every request starts failing with "too many connections" —
which looks like a database outage and is actually a
configuration one.

## Two levels

- **In-process pool** — your framework's pool. Sufficient
  for a [[Monolithic Web App]] on one box.
- **[[PgBouncer]]** in front of the database. Necessary
  when you have many app processes, or short-lived
  [[Serverless Architecture]] invocations that would each
  open their own connection.

## Watch out for

- Pool size per process multiplied by process count is the
  number that must stay under `max_connections`. People
  size the pool and forget the multiplication.
- Transaction-mode pooling breaks session-level features
  such as prepared statements and `SET` — know which mode
  you are in.

## Related

[[PostgreSQL]] · [[PgBouncer]] · [[Read Replicas]] ·
[[Serverless Architecture]]

## Sources

- [[pgbouncer-config]] ·
  [[postgresql-runtime-config-connection]]
