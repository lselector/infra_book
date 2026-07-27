---
type: Service
title: "GitHub Actions"
description: "CI/CD built into the repository - the default pipeline for projects in this book."
tags: [ops-and-security, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# GitHub Actions

Runs workflows on repository events: push, pull request,
schedule, or manual dispatch.

## The workflow worth having on day one

Test, lint, audit dependencies, and deploy `main` on
green. Four jobs, and it catches the class of mistake that
otherwise reaches production.

## Secrets

Repository and environment secrets are encrypted and
exposed to workflows as environment variables. They are
masked in logs — though a script that prints a secret in a
transformed form can still leak it.

Better still: OIDC federation to a cloud role, so the
workflow assumes short-lived credentials and no long-lived
secret exists at all. See [[Secrets Management]].

## Environments

Deployment environments add required reviewers and
protection rules — the mechanism behind a manual approval
gate before production, and useful evidence for change
management under [[SOC 2]].

## Watch out for

- `pull_request_target` and workflows triggered by forks:
  a classic route to secret exfiltration. Understand the
  trigger before using it.
- Pin third-party actions to a commit SHA, not a moving
  tag.

## Related

[[Continuous Integration and Delivery]] ·
[[Git-Driven Deployment]] · [[Secrets Management]] ·
[[Deployment Environments]] · [[Dependabot]]

## Sources

- [[github-actions-understanding]] ·
  [[github-actions-workflow-syntax]] ·
  [[github-actions-secrets]] · [[github-environments]] ·
  [[github-actions-deployment]]
