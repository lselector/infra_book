---
type: Concept
title: "Database Sharding"
description: "Splitting data across databases by key - powerful, irreversible in practice, and rarely needed."
wikipedia: "https://en.wikipedia.org/wiki/Shard_(database_architecture)"
tags: [storage-and-databases, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Database Sharding

Partitioning rows across multiple independent databases,
usually by customer or by a hash of some key.

## Why it matters here

Mostly as a thing to avoid for as long as possible. A
single [[PostgreSQL]] instance on decent hardware handles
volumes far beyond what most SaaS products reach. Sharding
costs you cross-shard joins, distributed transactions,
rebalancing, and a much harder backup story.

## The cheaper steps first

1. Indexes and query fixes.
2. [[Caching]] the expensive reads.
3. [[Read Replicas]] for read load.
4. Table partitioning within one database — same engine,
   far less operational change.
5. Only then, separate databases.

## When it is genuinely right

When [[Multi-Tenant SaaS]] isolation requirements already
push you to a database per tenant. Then sharding is a
side effect of a decision you made for other reasons,
which is the easiest way to arrive at it.

## Related

[[Read Replicas]] · [[Multi-Tenant SaaS]] · [[Caching]] ·
[[Relational Databases]]

## Sources

- [[postgresql-partitioning]] ·
  [[azure-multitenant-storage-data]]
