---
type: Summary
title: "PostgreSQL — log-shipping standby servers and replication"
description: "July 16, 2026: PostgreSQL 19 Beta 2 Released!"
resource: "https://www.postgresql.org/docs/current/warm-standby.html"
source_file: "Raw/04_network_storage_db/postgresql-warm-standby.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# PostgreSQL — log-shipping standby servers and replication

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/postgresql-warm-standby.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.postgresql.org/docs/current/warm-standby.html>

## Opening

> July 16, 2026: [PostgreSQL 19 Beta 2 Released!](https://www.postgresql.org/about/news/postgresql-19-beta-2-released-3350/)
> [Documentation](https://www.postgresql.org/docs/ "Documentation") → [PostgreSQL 18](https://www.postgresql.org/docs/18/index.html)
> Supported Versions: [Current](https://www.postgresql.org/docs/current/warm-standby.html "PostgreSQL 18 - 26.2. Log-Shipping Standby Servers") ([18](https://www.postgresql.org/docs/18/warm-standby.html "PostgreSQL 18 - 26.2. Log-Shipping Standby Servers")) / ...
> Development Versions: [19](https://www.postgresql.org/docs/19/warm-standby.html "PostgreSQL 19 - 26.2. Log-Shipping Standby Servers") / [devel](https://www.postgresql.org/docs/devel/warm-standby.html "PostgreSQL devel - 26.2. Log-Shipping Standby Servers")

## Contents of the source document

  - 26.2. Log-Shipping Standby Servers #
    - 26.2.1. Planning #
    - 26.2.2. Standby Server Operation #
    - 26.2.3. Preparing the Primary for Standby Servers #
    - 26.2.4. Setting Up a Standby Server #
    - Note
    - 26.2.5. Streaming Replication #
    - 26.2.6. Replication Slots #
    - Caution
    - 26.2.7. Cascading Replication #
    - 26.2.8. Synchronous Replication #
    - 26.2.9. Continuous Archiving in Standby #
  - Submit correction

## Related pages

[[Authentication]] · [[Load Balancing]] · [[PostgreSQL]]
