---
type: Tool
title: "SQLite"
description: "A whole database in one file, with no server - the right default for a very simple app."
wikipedia: "https://en.wikipedia.org/wiki/SQLite"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# SQLite

An embedded SQL database. The entire database is one file;
there is no process to run, no port, no user management,
no backups infrastructure beyond copying a file.

## When it is the right answer

- One application process — a [[Monolithic Web App]] on
  [[One-Box Deployment]].
- Read-heavy workloads, which is most web applications.
- Internal tools, prototypes, and anything where the ops
  cost of PostgreSQL is not yet justified.

The project's own guidance is that it suits most
applications below very high write concurrency, and it is
not being modest.

## Make it behave in production

- **Enable WAL mode.** It permits concurrent readers with
  a writer and is essential for a web app.
- Set a `busy_timeout` so a brief lock retries instead of
  erroring.
- Turn on foreign keys — they are off by default.

## The real limit

**Concurrent writers.** One writer at a time. If your
workload writes constantly from multiple processes, this
is your signal to move to [[PostgreSQL]].

## Migrating later

Keep the database URL in config from day one and use
portable SQL. The move is then a schema translation and a
data copy, not a rewrite. See [[Relational Databases]].

## Related

[[PostgreSQL]] · [[Relational Databases]] ·
[[Database Backups]] · [[One-Box Deployment]] ·
[[The Ladder]]

## Sources

- [[sqlite-when-to-use]] · [[sqlite-wal]] ·
  [[sqlite-backup]] · [[sqlite-quirks]] · [[sqlite-about]]
