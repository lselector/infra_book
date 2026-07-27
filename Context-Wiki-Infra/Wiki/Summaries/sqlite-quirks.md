---
type: Summary
title: "SQLite — quirks, caveats and gotchas"
description: "Small. Fast. Reliable. Choose any three."
resource: "https://www.sqlite.org/quirks.html"
source_file: "Raw/04_network_storage_db/sqlite-quirks.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# SQLite — quirks, caveats and gotchas

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/sqlite-quirks.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.sqlite.org/quirks.html>

## Opening

> [ ](https://www.sqlite.org/index.html)
> Small. Fast. Reliable.
> Choose any three.
> Quirks, Caveats, and Gotchas In SQLite

## Contents of the source document

- 1\. Overview
- 2\. SQLite Is Embedded, Not Client-Server
- 3\. Flexible Typing
  - 3.1. No Separate BOOLEAN Datatype
  - 3.2. No Separate DATETIME Datatype
  - 3.3. The datatype is optional
- 4\. Foreign Key Enforcement Is Off By Default
- 5\. PRIMARY KEYs Can Sometimes Contain NULLs
- 7\. SQLite Does Not Do Full Unicode Case Folding By Default
- 8\. Double-quoted String Literals Are Accepted
- 9\. Keywords Can Often Be Used As Identifiers
- 10\. Dubious SQL Is Allowed Without Any Error Or Warning
- 11\. AUTOINCREMENT Does Not Work The Same As MySQL
- 12\. NUL Characters Are Allowed In Text Strings
- 13\. SQLite Distinguishes Between Integer And Text Literals
- 14\. SQLite Gets The Precedence Of Comma-Joins Wrong

## Related pages

[[PostgreSQL]] · [[SQLite]]
