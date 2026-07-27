---
type: Concept
title: "Git-Driven Deployment"
description: "From SSH-and-git-pull to a pipeline - the progression, and why the first step is legitimate."
tags: [ops-and-security, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Git-Driven Deployment

The repository is the source of truth for what is running.
Deployment is the act of making the server match a commit.

## The honest progression

1. **`git pull && systemctl restart`** over SSH. Real,
   auditable, and entirely adequate for one developer.
2. **A deploy script** on the server that pulls, migrates,
   restarts and health-checks — so the sequence cannot be
   half-remembered at 11pm.
3. **[[Continuous Integration and Delivery]]** that runs tests then performs
   step 2 on green.
4. **Preview environments** per pull request — see
   [[Deployment Environments]].

## Why it matters here

Step 1 is not shameful. What matters is that the commit
running in production is identifiable, and that going back
is one command. Everything above that is about removing
humans from repetitive steps and adding gates.

## The line worth drawing early

Never edit files on the server. The moment production
diverges from the repository, rollback stops working and
nobody can say what is deployed.

## Related

[[Continuous Integration and Delivery]] · [[Deployment Environments]] ·
[[Static Build Pipeline]] · [[Infrastructure as Code]]

## Sources

- [[github-actions-deployment]] ·
  [[github-actions-understanding]] ·
  [[gitlab-ci-quick-start]]
