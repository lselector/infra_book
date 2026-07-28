---
type: Concept
title: "Relational Databases"
description: "Tables, constraints and transactions - and the choice between SQLite, self-hosted Postgres and managed."
wikipedia: "https://en.wikipedia.org/wiki/Relational_database"
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Relational Databases

Structured data with schemas, constraints and
transactions. For almost every application in this book,
the right kind of database.

## The three deployment shapes

| Shape | Cost | Ops | Use when |
|---|---|---|---|
| [[SQLite]] on the app disk | $0 | none | one process, read-heavy |
| [[PostgreSQL]] on the same box | $0 extra | backups, tuning | concurrent writers, one server |
| Managed ([[Amazon RDS]]) | $15-100+ | patching outsourced | you need HA or replicas |

## Why it matters here

The progression above *is* rungs 6 and 10 of
[[The Ladder]]. Start left, move right on a signal, not on
a hunch.

## The rule that saves you

Keep the database URL in an environment variable from day
one — see [[Twelve-Factor App]]. Then moving between these
three shapes is a config change and a data migration, not
a rewrite.

## Watch out for

- Choosing managed first for a project with ten users. You
  are paying $20/month for backups you could get with
  `pg_dump` and a cron entry.
- Skipping constraints because the ORM validates.
  Constraints are the last line that actually holds.

## Related

[[SQLite]] · [[PostgreSQL]] · [[Database Backups]] ·
[[Connection Pooling]] · [[Read Replicas]]

## Sources

- [[postgresql-tutorial-start]] · [[sqlite-when-to-use]] ·
  [[aws-rds-what-is]] · [[mariadb-vs-mysql]]
