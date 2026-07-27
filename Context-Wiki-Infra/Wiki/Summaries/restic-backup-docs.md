---
type: Summary
title: "restic — backup basics and repositories"
description: "You can now back up some data. The contents of a directory at a specific point in time is called a “snapshot” in restic."
resource: "https://restic.readthedocs.io/en/stable/040_backup.html"
source_file: "Raw/04_network_storage_db/restic-backup-docs.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# restic — backup basics and repositories

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/restic-backup-docs.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://restic.readthedocs.io/en/stable/040_backup.html>

## Opening

> You can now back up some data. The contents of a directory at a specific point in time is called a “snapshot” in restic. Run the following command and enter the repository password you chose above again:
> $ restic -r /srv/restic-repo --verbose backup ~/work
> open repository
> enter password for repository:

## Contents of the source document

- Backing up
  - File change detection
  - Skip creating snapshots if unchanged
  - Absolute and relative paths
  - Dry runs
  - Excluding files
  - Including files
  - Comparing snapshots
  - Backing up special items and metadata
  - Reading data from a command
  - Reading data from stdin
  - Tags for backup
  - Scheduling backups
  - Space requirements
  - Exit status codes
  - Environment variables

## Related pages

[[HTTP]] · [[restic]] · [[systemd]]
