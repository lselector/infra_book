---
type: Service
title: "AWS Backup"
description: "Policy-driven backups across AWS services, with vaults you cannot casually delete."
tags: [storage-and-databases, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Backup

Centralises backup policy across EBS, RDS, DynamoDB, EFS
and others: one plan defines schedule, retention and
lifecycle, applied by resource tag.

## What it adds over per-service snapshots

- One place to state and evidence the policy — which is
  what [[SOC 2]] availability evidence looks like.
- **Vault Lock**, a write-once retention control that even
  an account administrator cannot override. That is the
  meaningful defence against ransomware and against a
  compromised admin.
- Cross-region and cross-account copies.

## What it does not remove

The obligation to **test restores**. A backup plan with a
green status and an untested restore path is the same
false comfort as any other. See [[Database Backups]].

## Related

[[Database Backups]] · [[SOC 2]] ·
[[Trust Services Criteria]] · [[Incident Response]] ·
[[Encryption at Rest]]

## Sources

- [[aws-backup-what-is]] · [[aws-rds-encryption]]
