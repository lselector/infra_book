---
type: Service
title: "Supabase Auth"
description: "Authentication attached to a Postgres database, with row-level security as the authorisation model."
tags: [ops-and-security, auth]
timestamp: "2026-07-27T00:00:00Z"
---

# Supabase Auth

Part of the Supabase platform: hosted authentication whose
users live in a table in your own [[PostgreSQL]] database.

## The distinguishing idea

Because users are rows in your database, authorisation can
be expressed as PostgreSQL row-level security policies —
the database itself enforces who may read which row. That
is an unusually robust place to put the check, and it
suits [[Multi-Tenant SaaS]] isolation well.

## When to choose it

- You are already using Supabase for the database.
- You want an open-source, self-hostable path.
- You like the RLS model for [[Authorization]].

## Watch out for

RLS is powerful and easy to get subtly wrong. Policies
must be tested deliberately, including the negative cases,
because a permissive policy silently exposes everything.

## Related

[[Authentication]] · [[Authorization]] · [[PostgreSQL]] ·
[[Firebase Authentication]] · [[Multi-Tenant SaaS]]

## Sources

- [[supabase-auth-overview]]
