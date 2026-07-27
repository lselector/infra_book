---
type: Concept
title: "Encryption at Rest"
description: "Encrypting stored data - what the provider does for you, and what remains your decision."
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Encryption at Rest

Data on disk is stored encrypted, so a stolen or
improperly decommissioned volume yields nothing.

## What you get by default

- [[Amazon S3]] encrypts new objects automatically.
- Google Cloud encrypts all data at rest with no action
  required.
- EBS volumes and [[Amazon RDS]] instances can be
  encrypted at creation — a checkbox.

## The part that is still yours

- **Enabling it at creation.** An unencrypted EBS volume
  or RDS instance cannot be encrypted in place; you
  snapshot, copy with encryption, and restore.
- **Key custody.** Provider-managed keys are fine for most
  cases; customer-managed keys ([[AWS KMS]] CMK, Google
  CMEK) give you the audit trail and the ability to
  revoke.
- **Backups.** An encrypted database with plaintext dumps
  in a bucket has achieved nothing. See
  [[Database Backups]].
- **Application-level encryption** for the few genuinely
  sensitive columns, via [[Envelope Encryption]].

## Why it matters here

It is one of the first controls named in
[[Trust Services Criteria]] and in every security
questionnaire, and it is largely free — so there is no
good reason not to have it.

## Related

[[Encryption in Transit]] · [[Envelope Encryption]] ·
[[AWS KMS]] · [[Database Backups]] · [[SOC 2]]

## Sources

- [[aws-ebs-encryption]] · [[aws-rds-encryption]] ·
  [[aws-s3-sse-kms]] · [[gcp-encryption-at-rest]] ·
  [[gcp-cmek]] · [[postgresql-encryption-options]]
