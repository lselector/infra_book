---
type: Concept
title: "Continuous Integration and Delivery"
description: "Automated test, build and deploy on push - the minimum worth having, and the pipeline it grows into."
wikipedia: "https://en.wikipedia.org/wiki/CI%2FCD"
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

## The anatomy of a grown-up pipeline

Each stage exists to fail earlier and cheaper than the
one after it:

```text
push
 │
 ├─ lint + type check          seconds     fail fastest
 ├─ unit tests                 seconds     Automated Testing
 ├─ dependency + secret scan   seconds     pip-audit, Gitleaks
 ├─ build artifact             minutes     one image, one digest
 ├─ integration tests          minutes     against a real Postgres
 ├─ deploy to staging          automatic   Deployment Environments
 ├─ smoke test + ZAP baseline  seconds     Security Testing
 └─ deploy to production       on approval Deployment Strategies
```

Two properties matter more than the stage list:

**Build once, deploy many.** The artifact built in the
build stage — an image digest ([[Container Images]]), a
Pages deployment, a tarball — is the *same* artifact
promoted to staging and then production. Rebuilding per
environment means production runs something no test ever
saw.

**Fast feedback first.** Order stages by (probability of
failure ÷ time to run). A linter that fails in 8 seconds
is worth more than the same failure found 12 minutes
later.

## Making it fast

A pipeline nobody waits for is a pipeline that gets
bypassed. The usual wins, in order:

- **Cache dependencies** — `~/.cache/uv`, `~/.npm`,
  `~/.cargo`. One `cache` step, minutes saved per run.
- **Cache Docker layers** across runs
  ([[Docker Build Cache]] — `cache-from: type=gha`
  through [[BuildKit]]).
- **Run independent jobs in parallel**; use a matrix for
  multiple versions.
- **Only run what changed** — path filters, so a README
  edit does not run the full suite.
- **Move slow suites to nightly** and keep push-time
  under a few minutes ([[Automated Testing]]).

Have the workflow call the same commands you run locally
— `just test`, `just build` ([[just]], or [[Invoke]] /
[[GNU Make]]) — so the pipeline and the laptop cannot
drift apart.

## Credentials, without long-lived keys

The old way is a static cloud key in repository secrets,
which never expires and is only as safe as the last
person who had access. The modern way is **OIDC**: the CI
provider issues a short-lived token, the cloud trusts
that provider for a specific repository and branch, and
no secret is stored at all. [[GitHub Actions]] supports
this for AWS, GCP and Azure; use it in preference to
`AWS_SECRET_ACCESS_KEY` in a secret store.

When a static secret is unavoidable, scope it to one
environment with required reviewers, and give it only the
permissions the deploy needs ([[Least Privilege]],
[[Secrets Management]]).

## Watch out for

- Secrets in workflow files. Use the platform's encrypted
  secret store — see [[Secrets Management]].
- Deploy credentials with far more permission than the
  deploy needs, contra [[Least Privilege]].
- A pipeline nobody watches: a red build that stays red
  teaches the team to ignore it.
- **Third-party actions pinned to a tag.** A tag can be
  moved; pin to a commit SHA, because an action runs with
  access to your secrets.
- **A pipeline that only exists on one branch**, so the
  first release from a hotfix branch is untested.
- **No path back.** A pipeline that can only roll forward
  turns a bad deploy into an outage
  ([[Deployment Strategies]]).

## Related

[[Git-Driven Deployment]] · [[GitHub Actions]] ·
[[GitLab CI]] · [[Deployment Strategies]] ·
[[Deployment Environments]] · [[Automated Testing]] ·
[[Fuzz Testing]] · [[Security Testing]] ·
[[Dependency Auditing]] · [[Container Images]] ·
[[Docker Build Cache]] · [[BuildKit]] ·
[[Secrets Management]] · [[Least Privilege]] ·
[[Infrastructure as Code]] · [[SOC 2]] · [[just]] ·
[[GNU Make]] · [[Invoke]]

## Sources

- [[github-actions-understanding]] ·
  [[github-actions-workflow-syntax]] ·
  [[github-actions-secrets]] ·
  [[github-actions-deployment]] · [[github-environments]]
  · [[gitlab-ci-quick-start]] · [[github-code-scanning]]
