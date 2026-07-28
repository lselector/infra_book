---
type: Service
title: "Dependabot"
description: "Automated pull requests for vulnerable and outdated dependencies."
wikipedia: "https://en.wikipedia.org/wiki/GitHub"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Dependabot

Built into GitHub. Watches your manifests and lockfiles,
alerts on known vulnerabilities, and opens pull requests
that bump the affected package.

## Why it is the highest-value security automation

It converts "we should keep dependencies updated" —
something nobody does by hand — into a pull request that
already exists, with a changelog and a passing test suite.
Turn on alerts and security updates; both are free on
public and private repositories.

## Configuring it so it helps

- Security updates: on, always.
- Version updates: weekly rather than daily, grouped, or
  the noise trains people to close them unread.
- Ensure [[Continuous Integration and Delivery]] runs on
  its pull requests — a green build is what makes merging
  it a two-second decision.

## Related

[[Dependency Auditing]] · [[GitHub Actions]] ·
[[Security Testing]] · [[OWASP Top 10]] · [[CodeQL]]

## Sources

- [[github-dependabot-alerts]] · [[npm-audit]] ·
  [[pip-audit-readme]] ·
  [[owasp-vulnerable-dependency-management]]
