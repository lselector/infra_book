---
type: Concept
title: "Incident Response"
description: "A short written plan for the day it goes wrong, decided in advance rather than at 3am."
wikipedia: "https://en.wikipedia.org/wiki/Computer_security_incident_management"
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Incident Response

The documented sequence you follow when something breaks
or is breached.

## The four phases

1. **Prepare** — contacts, access, backups, a plan people
   have read.
2. **Detect and analyse** — from
   [[Monitoring and Alerting]] or from a report. Decide
   severity.
3. **Contain, eradicate, recover** — stop the bleeding,
   remove the cause, restore service from
   [[Database Backups]].
4. **Post-incident** — a blameless write-up and concrete
   follow-up actions.

## The small-team version

One page is enough, and one page that exists beats a
detailed one that does not:

- Who decides it is an incident.
- Who to call, with phone numbers, stored somewhere that
  works when your systems do not.
- How to reach the provider console if the usual path is
  compromised.
- Where the backups are and how to restore them.
- What you are obliged to tell customers, and when.

## Why it matters here

Incident response is an explicit control under
[[Trust Services Criteria]], and a required document for
[[SOC 2]]. More usefully, writing it is when you notice
that your only recovery credential lives in the system you
are trying to recover.

## Related

[[Monitoring and Alerting]] · [[Database Backups]] ·
[[SOC 2]] · [[Audit Logging]] ·
[[Service Level Objectives]] · [[Failure Modes]] ·
[[Chaos Engineering]] · [[Red Team and Blue Team]] ·
[[MITRE ATT&CK]]

## Sources

- [[nist-incident-handling-guide]] · [[cis-controls-list]]
  · [[sre-book-monitoring]]
