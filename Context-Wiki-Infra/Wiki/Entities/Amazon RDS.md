---
type: Service
title: "Amazon RDS"
description: "Managed relational databases - you stop doing backups and patching, and start paying for it."
tags: [storage-and-databases]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon RDS

Runs PostgreSQL, MySQL and others as a managed service:
automated backups, patching, and optional multi-AZ
failover.

## What you are buying

- Automated backups and point-in-time recovery.
- Minor version patching in a maintenance window.
- Failover to a standby, if you pay for multi-AZ.
- [[Read Replicas]] as a console action.

## What it costs

Meaningfully more than the same database on the box you
already have. The smallest sensible instance plus storage
plus backup retention typically exceeds the price of the
entire VPS running your app.

## The decision

Stay on the app server while you can restore from
`pg_dump` and can tolerate a short outage. Move when you
need failover you cannot operate yourself, or when
handling backups reliably has become a real time cost —
see [[Relational Databases]].

## Watch out for

Encrypt at creation. An unencrypted instance cannot be
encrypted in place; you snapshot, copy encrypted and
restore. See [[Encryption at Rest]].

## Related

[[PostgreSQL]] · [[Relational Databases]] ·
[[Read Replicas]] · [[Encryption at Rest]] ·
[[Cost Control]]

## Sources

- [[aws-rds-what-is]] · [[aws-rds-encryption]]
