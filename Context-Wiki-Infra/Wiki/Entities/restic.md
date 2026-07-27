---
type: Tool
title: "restic"
description: "Encrypted, deduplicated, incremental backups to almost any storage backend."
tags: [storage-and-databases, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# restic

A single-binary backup tool that produces encrypted,
deduplicated snapshots in a repository, which can live on
[[Amazon S3]], [[Cloudflare R2]], SFTP or a local disk.

## Why it fits this book

- **Encrypted by default**, which satisfies the
  requirement that backups be protected at rest — see
  [[Encryption at Rest]].
- Deduplication keeps a long retention chain cheap.
- One binary, no server, no agent.
- `restic check` verifies repository integrity — the thing
  that tells you the backups are real.

## The workflow

```bash
restic backup /srv/app/data
restic forget --keep-daily 14 --keep-weekly 12 --prune
restic check
```

Run nightly from cron, alert on non-zero exit.

## Watch out for

- **The repository password.** Lose it and the backups are
  permanently unreadable. Store it somewhere independent
  of the server being backed up.
- Databases need a consistent dump first — `pg_dump` into
  a file, then back that up. Do not back up a live
  Postgres data directory.

## Related

[[Database Backups]] · [[Object Storage]] ·
[[Encryption at Rest]] · [[Incident Response]]

## Sources

- [[restic-backup-docs]] · [[postgresql-backup-dump]] ·
  [[crontab-5-man-page]]
