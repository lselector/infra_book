---
type: Concept
title: "Least Privilege"
description: "Every identity gets exactly the access it needs - the control that limits every other failure."
wikipedia: "https://en.wikipedia.org/wiki/Principle_of_least_privilege"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Least Privilege

Grant the minimum permission required, for the shortest
time, to the smallest scope.

## Where it applies on a small stack

- **Deploy credentials.** A token that can deploy one
  Pages project, not an account-wide API key.
- **Database users.** The app connects as a user that owns
  its own schema, not as superuser.
- **Cloud IAM.** Prefer roles assumed by the workload over
  long-lived access keys — this also removes the secret
  entirely, see [[Secrets Management]].
- **The server.** The app runs as its own unprivileged
  user, never root. See [[Linux Server Hardening]].

## Why it matters here

It does not prevent compromise; it bounds it. A leaked
deploy token that can only deploy one static site is an
inconvenience. The same leak with an account-wide key is
an incident.

## Making it verifiable

[[AWS IAM]] Access Analyzer reports which permissions were
actually used, so you can cut the unused ones with
evidence rather than guesswork. That report is also useful
material for an [[Access Review]].

## Related

[[Authorization]] · [[Secrets Management]] ·
[[Access Review]] · [[Shared Responsibility Model]] ·
[[SOC 2]]

## Sources

- [[aws-iam-best-practices]] · [[aws-iam-access-analyzer]]
  · [[owasp-authorization-cheatsheet]]
