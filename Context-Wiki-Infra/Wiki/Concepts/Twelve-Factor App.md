---
type: Concept
title: "Twelve-Factor App"
description: "A dozen conventions that make an app cheap to deploy, scale and move between hosts."
wikipedia: "https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology"
tags: [foundations, architecture]
timestamp: "2026-07-27T00:00:00Z"
---

# Twelve-Factor App

A set of conventions for applications that are meant to be
deployed to a platform rather than installed on a pet
server. Not all twelve matter equally at small scale.

## The factors that earn their keep immediately

- **Config in the environment.** Credentials and hostnames
  come from env vars, never from committed files. This is
  the foundation of [[Secrets Management]].
- **Backing services are attached resources.** The
  database is a URL, so swapping [[SQLite]] for
  [[PostgreSQL]] or local for managed is a config change.
- **Logs are event streams.** Write to stdout and let
  [[systemd]] or the platform handle collection — do not
  manage log files in the app.
- **Dev/prod parity.** Same database engine in both, or
  you will ship bugs that only exist in production.

## Why it matters here

Following these four makes the climb up [[The Ladder]]
cheap: an app that reads its config from the environment
and logs to stdout moves from a laptop to a VPS to a PaaS
without code changes.

## Watch out for

Treating all twelve as mandatory. Strict statelessness and
disposability matter when you run many instances; on one
box they can be over-engineering.

## Related

[[Secrets Management]] · [[Deployment Environments]] ·
[[Managed PaaS]] · [[Monitoring and Alerting]]

## Sources

- [[12factor-intro]] · [[12factor-config]] ·
  [[12factor-backing-services]] · [[12factor-logs]] ·
  [[12factor-dev-prod-parity]]
