---
type: Summary
title: "SQLite — write-ahead logging (WAL mode)"
description: "Small. Fast. Reliable. Choose any three."
resource: "https://www.sqlite.org/wal.html"
source_file: "Raw/04_network_storage_db/sqlite-wal.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# SQLite — write-ahead logging (WAL mode)

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/sqlite-wal.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.sqlite.org/wal.html>

## Opening

> [ ](https://www.sqlite.org/index.html)
> Small. Fast. Reliable.
> Choose any three.
> Write-Ahead Logging

## Contents of the source document

- 1\. Overview
- 2\. How WAL Works
  - 2.1. Checkpointing
  - 2.2. Concurrency
  - 2.3. Performance Considerations
- 3\. Activating And Configuring WAL Mode
  - 3.1. Automatic Checkpoint
  - 3.2. Application-Initiated Checkpoints
  - 3.3. Persistence of WAL mode
- 4\. The WAL File
- 5\. Read-Only Databases
- 6\. Avoiding Excessively Large WAL Files
- 7\. Implementation Of Shared-Memory For The WAL-Index
- 8\. Use of WAL Without Shared-Memory
- 9\. Sometimes Queries Return SQLITE_BUSY In WAL Mode
- 10\. Backwards Compatibility
- 11\. The WAL-Reset Bug
  - 11.1. Bug Details

## Related pages

[[HTTP]] · [[SQLite]]
