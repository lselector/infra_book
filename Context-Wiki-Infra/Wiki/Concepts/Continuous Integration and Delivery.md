---
type: Concept
title: "Continuous Integration and Delivery"
description: "Automated test, build and deploy on push - and the minimum worth having on a small project."
tags: [ops-and-security, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Continuous Integration and Delivery

Continuous integration runs checks on every push.
Continuous deployment ships what passes.

## The minimum that earns its keep

```yaml
on: [push]
jobs:
  check:
    - run tests
    - run a linter
    - audit dependencies      # see Dependency Auditing
  deploy:
    if: branch == main
    - build
    - deploy                  # wrangler, ssh, or platform
```

Four steps. It catches the broken import you did not run
locally and the vulnerable dependency you did not know
about.

## Why it matters here

- It makes deployment boring and repeatable, which is the
  point.
- It is the natural place to hang [[Security Testing]]: a
  ZAP baseline scan and `pip-audit` cost seconds.
- It is the evidence an auditor wants for change
  management under [[SOC 2]] — every change tested,
  reviewed and traceable to a commit.

## Watch out for

- Secrets in workflow files. Use the platform's encrypted
  secret store — see [[Secrets Management]].
- Deploy credentials with far more permission than the
  deploy needs, contra [[Least Privilege]].
- A pipeline nobody watches: a red build that stays red
  teaches the team to ignore it.

## Related

[[Git-Driven Deployment]] · [[GitHub Actions]] ·
[[Secrets Management]] · [[Security Testing]] ·
[[Deployment Environments]]

## Sources

- [[github-actions-understanding]] ·
  [[github-actions-workflow-syntax]] ·
  [[github-actions-secrets]] · [[gitlab-ci-quick-start]]
