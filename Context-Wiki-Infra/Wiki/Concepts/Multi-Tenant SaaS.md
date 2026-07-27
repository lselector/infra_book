---
type: Concept
title: "Multi-Tenant SaaS"
description: "Serving many customers from one system - shared database, database per tenant, and the isolation trade-off."
tags: [architectures, saas]
timestamp: "2026-07-27T00:00:00Z"
---

# Multi-Tenant SaaS

One deployment serves many customers. The design question
is how far their data is separated.

## The three models

| Model | Isolation | Cost per tenant | Fits |
|---|---|---|---|
| Shared schema, `tenant_id` column | weakest | lowest | self-serve, many small tenants |
| Schema per tenant | middling | middling | tens to hundreds of tenants |
| Database per tenant | strongest | highest | few large or regulated tenants |

## Why it matters here

- Start with a `tenant_id` column and enforce it in one
  place — a query layer or row-level security — never by
  remembering to add a `WHERE` clause.
- The isolation model is the first thing an enterprise
  security questionnaire asks about, and it feeds directly
  into [[SOC 2]] confidentiality claims.
- Per-tenant databases make onboarding, migration and
  backup restore N times more work. Do not choose it for
  three customers.

## The failure mode to design against

A missing tenant filter that leaks one customer's data to
another. This is the single worst bug class in SaaS. Test
for it explicitly, and prefer a mechanism that fails
closed.

## Related

[[Relational Databases]] · [[Authorization]] ·
[[SOC 2]] · [[Database Sharding]]

## Sources

- [[azure-multitenant-overview]] ·
  [[azure-multitenant-tenancy-models]] ·
  [[azure-multitenant-storage-data]]
