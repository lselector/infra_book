---
type: Service
title: "AWS CloudTrail"
description: "The audit log of everything done in an AWS account."
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS CloudTrail

Records API activity across an AWS account: who called
what, from where, when, and whether it succeeded.

## Why it is non-negotiable

- It is the [[Audit Logging]] evidence a [[SOC 2]] auditor
  expects for the cloud control plane.
- It is what you read during an incident to establish what
  actually happened.
- It records every [[AWS KMS]] key use, which is what
  makes key usage auditable at all.

## Configure it properly

- A trail covering **all regions**. Attackers use the ones
  you do not watch.
- Deliver to a **separate account or a locked bucket** so
  a compromised principal cannot erase its own tracks.
- Enable **log file validation**.
- Set retention to at least a year.
- Alert on a few high-signal events — root account use,
  IAM policy changes, trail modification — via
  [[Monitoring and Alerting]].

## Watch out for

Data events (S3 object-level, Lambda invocations) are off
by default and are where the volume and cost live. Enable
them selectively.

## Related

[[Audit Logging]] · [[SOC 2]] ·
[[Trust Services Criteria]] · [[AWS Config]] ·
[[Incident Response]]

## Sources

- [[aws-cloudtrail-user-guide]] · [[aws-kms-concepts]] ·
  [[aws-iam-best-practices]]
