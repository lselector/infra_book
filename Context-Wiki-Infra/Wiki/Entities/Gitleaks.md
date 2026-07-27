---
type: Tool
title: "Gitleaks"
description: "Scans Git history for committed credentials - run it before you need it."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Gitleaks

Scans a repository, including its full history, for
patterns that look like credentials, and reports where
they are.

## How to use it

- **Once, now**, against the whole history of every
  repository you own. The results are often surprising.
- **In [[Continuous Integration and Delivery]]**, failing
  the build on a new finding.
- **As a pre-commit hook**, which stops the mistake
  before it exists.

## What to do with a finding

**Rotate the credential.** Rewriting history to remove the
commit is secondary and often impossible — the secret may
already be cloned, cached by the host, or in a fork. Treat
any committed secret as public from the moment it was
pushed. See [[Secrets Management]].

## The complementary control

GitHub secret scanning and push protection block many
known credential formats at push time, which is better
than detecting them afterwards. Turn both on.

## Related

[[Secrets Management]] · [[SOPS]] ·
[[Continuous Integration and Delivery]] ·
[[Security Testing]]

## Sources

- [[gitleaks-readme]] · [[github-secret-scanning]] ·
  [[github-push-protection]]
