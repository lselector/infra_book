---
type: Tool
title: "OSS-Fuzz"
description: "Google's free continuous fuzzing service for open-source projects - your library fuzzed forever, on their machines."
website: "https://google.github.io/oss-fuzz/"
tags: [tooling, security]
timestamp: "2026-07-28T00:00:00Z"
---

# OSS-Fuzz

A Google-run service that continuously fuzzes open-source
software on Google's infrastructure, at no cost to the
project. You contribute build scripts and fuzz targets;
OSS-Fuzz runs them forever, files bugs privately, and
verifies fixes.

Since 2016 it has found tens of thousands of bugs across
projects including OpenSSL, SQLite, curl and the Linux
kernel utilities — which is the strongest available
argument that [[Fuzz Testing]] finds things review does
not.

## How a project joins

1. Write **fuzz targets** — small functions taking a byte
   buffer and feeding it to the code under test.
2. Add a `Dockerfile` and `build.sh` so OSS-Fuzz can
   build the project with instrumentation
   ([[Container Images]]).
3. Submit a project config naming maintainer contacts.
4. Fix what arrives. Reports are private for 90 days,
   then disclosed — the deadline is deliberate.

Related pieces worth knowing: **ClusterFuzzLite** runs
the same targets in your own CI on pull requests, and
**OSS-Fuzz-Gen** uses LLMs to draft new fuzz targets for
uncovered code.

## Why it matters even if you never join

**You depend on it.** The libraries under your
application — the JSON parser, the image decoder, the TLS
stack — are hardened by this service, and its findings
become the CVEs that [[Dependency Auditing]] tells you to
update for. The connection is direct: an OSS-Fuzz report
today is a `npm audit` or `pip-audit` warning in your
project next month.

## When to join

If you publish a library that parses input from anyone —
a format, a protocol, a template language — this is free,
continuous security testing that you cannot buy at a
comparable price. If you run a closed-source SaaS, the
equivalent is running [[AFL++]] or property-based tests
in your own [[Continuous Integration and Delivery]].

## Related

[[Fuzz Testing]] · [[AFL++]] · [[Dependency Auditing]] ·
[[Security Testing]] · [[Automated Testing]] ·
[[Continuous Integration and Delivery]] ·
[[Container Images]] · [[CodeQL]] · [[Trivy]] ·
[[OWASP Top 10]]

## Sources

- Upstream documentation:
  <https://google.github.io/oss-fuzz/>. Not part of the
  downloaded `Raw/` corpus — related captures:
  [[owasp-vulnerable-dependency-management]] ·
  [[github-dependabot-alerts]] · [[npm-audit]] ·
  [[pip-audit-readme]].
