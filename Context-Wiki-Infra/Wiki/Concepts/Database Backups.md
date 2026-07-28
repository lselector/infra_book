---
type: Concept
title: "Database Backups"
description: "A backup you have never restored is not a backup - the nightly dump, the offsite copy, and the drill."
wikipedia: "https://en.wikipedia.org/wiki/Backup"
tags: [storage-and-databases, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Database Backups

The one piece of infrastructure whose absence ends a
business rather than inconveniencing it.

## The minimum that counts

1. **Nightly dump** — `pg_dump` for [[PostgreSQL]], or a
   consistent file copy for [[SQLite]].
2. **Offsite** — pushed to [[Object Storage]], because a
   backup on the same disk protects against nothing.
3. **Retention** — daily for a fortnight, weekly for a
   quarter. Ransomware and silent corruption are found
   late.
4. **Encrypted** at rest — see [[Encryption at Rest]].
5. **A restore drill.** Restore into a scratch database
   and run the app against it. Quarterly, calendared.

## Why it matters here

Backups are the availability control in
[[Trust Services Criteria]], and the first thing an
auditor asks to see evidence of. More importantly, the
restore drill is where you discover the dump has been
silently failing for five weeks.

## Watch out for

- Backups that need the production password to restore,
  stored only in production.
- `pg_dump` from a cron job with no alert on failure —
  wire it to [[Monitoring and Alerting]].

## Related

[[PostgreSQL]] · [[SQLite]] · [[Object Storage]] ·
[[restic]] · [[Incident Response]] · [[SOC 2]]

## Sources

- [[postgresql-backup-dump]] · [[pg-dump-man]] ·
  [[sqlite-backup]] · [[restic-backup-docs]] ·
  [[aws-backup-what-is]] · [[crontab-5-man-page]]
