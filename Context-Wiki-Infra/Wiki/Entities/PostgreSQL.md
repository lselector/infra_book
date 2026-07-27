---
type: Tool
title: "PostgreSQL"
description: "The default serious relational database - free, capable, and happy on the same box as your app."
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# PostgreSQL

A mature open-source relational database. The recommended
destination once [[SQLite]] stops fitting, and the last
database most projects will ever need.

## Installing it on the app server

1. `apt install postgresql`.
2. Create a role and a database for the app — not
   superuser.
3. **Keep `listen_addresses = 'localhost'`.** Nothing
   should reach it from outside the machine.
4. Configure `pg_hba.conf` for `scram-sha-256` on local
   connections.
5. Set up `pg_dump` nightly to [[Object Storage]] — see
   [[Database Backups]].

Steps 3 and 5 are the ones people skip and regret.

## What you get over SQLite

Concurrent writers, real types (JSONB, arrays, ranges),
full-text search, extensions such as PostGIS and
pgvector, and [[Read Replicas]] when you need them.

## Watch out for

- `max_connections` defaults to 100 and each connection is
  a process — see [[Connection Pooling]].
- Default memory settings are conservative for a
  dedicated box; tune `shared_buffers` and
  `work_mem`.
- Require SSL once the database is not on the same host —
  [[Encryption in Transit]].

## Related

[[SQLite]] · [[Relational Databases]] ·
[[Database Backups]] · [[Connection Pooling]] ·
[[PgBouncer]] · [[Read Replicas]]

## Sources

- [[postgresql-tutorial-start]] · [[postgresql-pg-hba-conf]]
  · [[postgresql-database-roles]] ·
  [[postgresql-backup-dump]] · [[postgresql-ssl-tcp]] ·
  [[postgresql-runtime-config-connection]]
