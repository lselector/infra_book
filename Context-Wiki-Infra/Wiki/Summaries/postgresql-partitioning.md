---
type: Summary
title: "PostgreSQL — table partitioning"
description: "July 16, 2026: PostgreSQL 19 Beta 2 Released!"
resource: "https://www.postgresql.org/docs/current/ddl-partitioning.html"
source_file: "Raw/08_scaling_maturity/postgresql-partitioning.md"
tags: [scaling, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# PostgreSQL — table partitioning

Extractive digest of the immutable capture in
`Raw/08_scaling_maturity/postgresql-partitioning.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.postgresql.org/docs/current/ddl-partitioning.html>

## Opening

> July 16, 2026: [PostgreSQL 19 Beta 2 Released!](https://www.postgresql.org/about/news/postgresql-19-beta-2-released-3350/)
> [Documentation](https://www.postgresql.org/docs/ "Documentation") → [PostgreSQL 18](https://www.postgresql.org/docs/18/index.html)
> Supported Versions: [Current](https://www.postgresql.org/docs/current/ddl-partitioning.html "PostgreSQL 18 - 5.12. Table Partitioning") ([18](https://www.postgresql.org/docs/18/ddl-partitioning.html "PostgreSQL 18 - 5.12. Table Partitioning")) / ...
> Development Versions: [19](https://www.postgresql.org/docs/19/ddl-partitioning.html "PostgreSQL 19 - 5.12. Table Partitioning") / [devel](https://www.postgresql.org/docs/devel/ddl-partitioning.html "PostgreSQL devel - 5.12. Table Partitioning")

## Contents of the source document

  - 5.12. Table Partitioning #
    - 5.12.1. Overview #
    - 5.12.2. Declarative Partitioning #
    - 5.12.3. Partitioning Using Inheritance #
    - Note
    - 5.12.4. Partition Pruning #
    - 5.12.5. Partitioning and Constraint Exclusion #
    - 5.12.6. Best Practices for Declarative Partitioning #
  - Submit correction

## Related pages

[[PostgreSQL]]
