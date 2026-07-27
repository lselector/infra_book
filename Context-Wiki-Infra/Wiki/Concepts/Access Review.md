---
type: Concept
title: "Access Review"
description: "Periodically confirming that everyone who has access still needs it."
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Access Review

A scheduled check of every account and permission against
who actually needs it, with the result written down.

## The mechanics

1. List every identity: cloud IAM users and roles, server
   logins, database users, repository collaborators, and
   SaaS accounts.
2. For each, record the owner and whether the access is
   still required.
3. Remove what is not. Record what was removed and when.
4. Repeat quarterly.

## Why it matters here

- **Offboarding is the failure mode.** Departed
  contractors with live SSH keys and cloud credentials are
  the single most common finding.
- [[AWS IAM]] Access Analyzer reports permissions actually
  used, which turns the review from opinion into evidence
  and feeds directly into [[Least Privilege]].
- It is an explicit control expectation in
  [[Trust Services Criteria]] and the artefact is exactly
  what an auditor samples.

## Making it cheap

Keep the identity count low. Per-person SSH keys, IAM
roles instead of shared keys, and SSO where available mean
the quarterly review is a short list rather than an
archaeology project.

## Related

[[Least Privilege]] · [[SSH Key Authentication]] ·
[[SOC 2]] · [[Audit Logging]] ·
[[Multi-Factor Authentication]]

## Sources

- [[aws-iam-access-analyzer]] · [[aws-iam-best-practices]]
  · [[vanta-soc2-checklist]] ·
  [[owasp-authorization-cheatsheet]]
