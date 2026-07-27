---
type: Service
title: "GitLab CI"
description: "GitLab's built-in pipelines - the equivalent when your code lives there."
tags: [ops-and-security, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# GitLab CI

Pipelines defined in `.gitlab-ci.yml`, running on shared
or self-hosted runners.

## What it does well

- Stages and jobs are explicit and easy to read.
- Built-in container registry and package registry.
- Self-hosted runners are straightforward, which matters
  if builds must run inside your own network.
- Environments and manual approval gates.

## Choosing between this and Actions

Follow the code. If the repository is on GitLab, use
GitLab CI; if on GitHub, use [[GitHub Actions]]. The
concepts transfer almost completely and neither is worth
migrating hosting for.

## Watch out for

The same rules apply as anywhere: secrets in masked
variables rather than in the file, minimal deploy
credentials, and a pipeline that someone actually watches.
See [[Continuous Integration and Delivery]].

## Related

[[Continuous Integration and Delivery]] ·
[[GitHub Actions]] · [[Secrets Management]]

## Sources

- [[gitlab-ci-quick-start]]
