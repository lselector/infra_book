---
type: Summary
title: "Architectural approaches for storage and data in multitenant solutions"
description: "Read in English Edit Note Access to this page requires authorization."
resource: "https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data"
source_file: "Raw/02_architectures/azure-multitenant-storage-data.md"
tags: [architectures, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Architectural approaches for storage and data in multitenant solutions

Extractive digest of the immutable capture in
`Raw/02_architectures/azure-multitenant-storage-data.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data>

## Opening

> [ Read in English ](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data) [ Edit ](https://github.com/microsoftdocs/architecture-center/blob/main/docs/guide/multitenant/approaches/storage-data.md)
> Note
> Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data) or changing directories.
> Access to this page requires authorization. You can try changing directories.

## Contents of the source document

- Architectural approaches for storage and data in multitenant solutions
  - Key considerations and requirements
    - Scale
    - Performance predictability
    - Data isolation
    - Complexity of implementation
    - Complexity of management and operations
    - Cost
  - Approaches and patterns to consider
    - Deployment Stamps pattern
    - Shared multitenant databases and file stores
    - Sharding pattern
    - Multitenant app with dedicated databases for each tenant
    - Geode pattern
  - Antipatterns to avoid
  - Databases
  - File and blob storage
  - Cost allocation

## Related pages

[[Authentication]] · [[Authorization]] · [[PostgreSQL]] · [[Rate Limiting]] · [[Relational Databases]]
