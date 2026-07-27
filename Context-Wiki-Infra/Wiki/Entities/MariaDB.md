---
type: Tool
title: "MariaDB"
description: "The MySQL-compatible fork - relevant mainly when something you inherited speaks MySQL."
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# MariaDB

A community fork of MySQL, largely drop-in compatible, and
the default MySQL-family package on most Linux
distributions.

## When it is relevant here

- An existing application or CMS that expects MySQL.
- A hosting environment that offers it and not PostgreSQL.
- A team that already knows it well.

## The recommendation

For a new project in this book, [[PostgreSQL]] is the
default: richer types, stricter defaults, and a stronger
extension ecosystem. MariaDB is a fine database; it is
simply not the one the rest of this material is written
against.

## Compatibility notes

Divergence from Oracle MySQL has grown over time —
notably around JSON, system-versioned tables and some
authentication plugins. "MySQL-compatible" is true for
ordinary application SQL and less true at the edges.

## Related

[[Relational Databases]] · [[PostgreSQL]] ·
[[Amazon RDS]]

## Sources

- [[mariadb-vs-mysql]] · [[aws-rds-what-is]]
