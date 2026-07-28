---
type: Concept
title: "Secrets Management"
description: "Where credentials live, how they get to the app, and what to do when one leaks."
wikipedia: "https://en.wikipedia.org/wiki/Key_management"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Secrets Management

API keys, database passwords and signing keys must reach
the application without ever entering the repository.

## The progression

| Stage | Mechanism | Adequate for |
|---|---|---|
| 1 | env vars from a `.env` outside Git | one box, one developer |
| 2 | platform secret store ([[GitHub Actions]], PaaS) | CI and managed hosting |
| 3 | [[AWS Secrets Manager]] / [[Google Secret Manager]] / [[HashiCorp Vault]] | rotation, audit trail, teams |
| 4 | short-lived credentials from an IAM role | no long-lived secret at all |

Stage 4 is the destination: the best-managed secret is one
that does not exist, because the workload's identity
grants access directly.

## The rules

- `.env` in `.gitignore`, file mode `600`, never
  committed.
- One secret per environment — see
  [[Deployment Environments]].
- Rotate on staff departure and on any suspicion.
- A leaked secret is leaked forever. Removing the commit
  does not help; **rotate it**.

## Detection

[[Gitleaks]] scans history, and GitHub push protection
blocks the commit before it lands. Turn both on before you
need them.

## Related

[[Envelope Encryption]] · [[Least Privilege]] ·
[[Key Rotation]] · [[Gitleaks]] · [[Twelve-Factor App]] ·
[[Bitwarden]] · [[Development Setup]]

## Sources

- [[owasp-secrets-management-cheatsheet]] ·
  [[aws-secrets-manager-intro]] · [[aws-parameter-store]] ·
  [[gcp-secret-manager-overview]] ·
  [[vault-what-is-vault]] · [[github-secret-scanning]] ·
  [[gitleaks-readme]] · [[sops-readme]]
