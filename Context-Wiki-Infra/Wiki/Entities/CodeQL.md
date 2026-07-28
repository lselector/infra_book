---
type: Tool
title: "CodeQL"
description: "GitHub's static analysis - queries your code as if it were a database."
wikipedia: "https://en.wikipedia.org/wiki/Semmle"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# CodeQL

Static analysis that compiles code into a queryable
database and runs security queries against it, surfacing
results as code scanning alerts.

## What it finds

Data-flow problems that pattern matching misses: untrusted
input reaching a query or a command, path traversal,
unsafe deserialisation. It traces the path from source to
sink and shows it.

## Using it well

- Enable default setup on the repository; it is free for
  public repositories and included in GitHub Advanced
  Security for private ones.
- Run on pull requests so findings arrive with the change
  that caused them.
- Triage properly. Static analysis produces false
  positives; dismissing with a recorded reason is fine,
  ignoring the whole feature is not.

## Where it sits

Static analysis (SAST) complements the dynamic scanning of
[[OWASP ZAP]] (DAST) and the dependency work of
[[Dependabot]]. Different tools, different blind spots —
all three are part of [[Security Testing]].

## Related

[[Security Testing]] · [[Dependabot]] · [[OWASP ZAP]] ·
[[GitHub Actions]] · [[OWASP Top 10]]

## Sources

- [[github-code-scanning]] · [[owasp-top-ten]]
