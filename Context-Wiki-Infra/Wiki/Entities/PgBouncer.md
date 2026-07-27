---
type: Tool
title: "PgBouncer"
description: "A tiny connection pooler in front of PostgreSQL - the fix for connection exhaustion."
tags: [storage-and-databases, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# PgBouncer

A lightweight connection pooler. Applications connect to
PgBouncer; PgBouncer maintains a much smaller number of
real [[PostgreSQL]] connections.

## Why you would add it

Postgres allocates a process per connection, so a few
hundred is a lot. Many application workers, or
[[Serverless Architecture]] invocations that each open a
connection, exhaust the limit and every request begins
failing.

## The pooling modes

- **Session** — a client holds a server connection for the
  whole session. Safest, least benefit.
- **Transaction** — a server connection is held only for
  the duration of a transaction. The usual choice, and the
  one that gives the big win.
- **Statement** — most aggressive, breaks multi-statement
  transactions.

## Watch out for

Transaction mode breaks session-scoped features: prepared
statements, `SET`, advisory locks, `LISTEN`/`NOTIFY`.
Check your driver's configuration — most have a
"prepare threshold" setting for exactly this.

## Related

[[Connection Pooling]] · [[PostgreSQL]] ·
[[Serverless Architecture]] · [[Read Replicas]]

## Sources

- [[pgbouncer-config]] ·
  [[postgresql-runtime-config-connection]]
