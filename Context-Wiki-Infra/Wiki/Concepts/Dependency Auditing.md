---
type: Concept
title: "Dependency Auditing"
description: "Knowing when a library you depend on turns out to be vulnerable, and having a route to updating it."
wikipedia: "https://en.wikipedia.org/wiki/Software_composition_analysis"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Dependency Auditing

Checking your dependency tree against databases of known
vulnerabilities, continuously rather than annually.

## The tools

- `npm audit` for JavaScript.
- `pip-audit` for Python.
- [[Dependabot]] on GitHub — opens pull requests for
  vulnerable and outdated dependencies automatically.
- [[Trivy]] for container images and IaC files.

## Making it work rather than nag

- Run the audit in
  [[Continuous Integration and Delivery]] and fail on high
  severity, not on everything — a build that fails on
  cosmetic advisories gets ignored or bypassed.
- Keep transitive dependencies patchable by committing a
  lockfile.
- Distinguish "vulnerable" from "exploitable in our usage".
  A vulnerability in a code path you never call is real
  but not urgent; record the reasoning rather than
  silently ignoring it.

## Why it matters here

Vulnerable components are a permanent fixture of the
[[OWASP Top 10]], and it is the failure mode that requires
no attacker skill at all — just a scanner and a version
number.

## Related

[[Security Testing]] · [[OWASP Top 10]] ·
[[Continuous Integration and Delivery]] ·
[[Unattended Upgrades]] · [[Dependabot]]

## Sources

- [[npm-audit]] · [[pip-audit-readme]] ·
  [[github-dependabot-alerts]] · [[trivy-overview]] ·
  [[owasp-vulnerable-dependency-management]]
