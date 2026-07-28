---
type: Concept
title: "Audit Logging"
description: "An immutable record of who did what and when - required for compliance, invaluable during an incident."
wikipedia: "https://en.wikipedia.org/wiki/Audit_trail"
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Audit Logging

A tamper-resistant trail of administrative and
security-relevant actions, distinct from application logs.

## What must be in it

- Authentication events: success, failure, logout.
- Authorisation failures.
- Changes to permissions, roles and users.
- Changes to infrastructure and configuration.
- Access to sensitive data, where feasible.
- Key usage — [[AWS KMS]] logs every operation to
  CloudTrail.

## What must never be in it

Passwords, tokens, keys, full card numbers or personal
data beyond what is needed. A log that leaks is a breach,
and logs are widely readable.

## Where it comes from

- [[AWS CloudTrail]] and [[Google Cloud Audit Logs]] for
  the cloud control plane — turn on and retain.
- [[AWS Config]] for configuration drift.
- Your application, for domain events.

## The properties that matter

**Immutability** (write to a separate account or bucket
the app cannot delete from), **retention** (a year is a
common expectation), and **review** — logs nobody looks at
satisfy an auditor but do not detect anything. Wire the
important ones into [[Monitoring and Alerting]].

## Related

[[Monitoring and Alerting]] · [[SOC 2]] ·
[[Trust Services Criteria]] · [[Incident Response]] ·
[[Access Review]] ·
[[Tool Calling]]

## Sources

- [[aws-cloudtrail-user-guide]] · [[gcp-cloud-audit-logs]]
  · [[aws-config-what-is]] · [[owasp-logging-cheatsheet]]
