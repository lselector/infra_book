---
type: Concept
title: "Unattended Upgrades"
description: "Letting the machine install its own security patches, because you will not."
wikipedia: "https://en.wikipedia.org/wiki/Patch_(computing)"
tags: [deployments, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Unattended Upgrades

A package that applies security updates automatically on a
schedule.

## Why it matters here

The realistic alternative on a one-person project is not
"careful manual patching", it is *no patching*. An
unattended-upgrades configuration limited to the security
pocket is low risk and closes the window between a
vulnerability being published and your box getting it.

It is also the cheapest possible answer to the "how do you
manage vulnerabilities" question in a security
questionnaire.

## Configure deliberately

- Security updates only, by default.
- Enable automatic reboot only if you can tolerate one —
  and if so, set a window.
- Have it email or log failures somewhere you will see,
  which ties into [[Monitoring and Alerting]].

## Watch out for

Unattended reboots on a box running a database with no
replica. Either accept the brief outage window or handle
reboots by hand and let only the package installs be
automatic.

## Related

[[Linux Server Hardening]] · [[One-Box Deployment]] ·
[[Dependency Auditing]]

## Sources

- [[ubuntu-automatic-updates]]
