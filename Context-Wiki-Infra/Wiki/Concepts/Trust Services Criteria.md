---
type: Concept
title: "Trust Services Criteria"
description: "The five criteria a SOC 2 report can cover, and what each asks of a small infrastructure."
tags: [compliance, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Trust Services Criteria

The control criteria a SOC 2 examination is measured
against. Security is mandatory; the other four are opted
into.

## The five

| Criterion | Asks | Typical evidence here |
|---|---|---|
| **Security** (required) | is access controlled and are threats detected | IAM policy, [[Multi-Factor Authentication]], [[Audit Logging]], [[Security Testing]] |
| **Availability** | does the system meet its uptime commitments | [[Monitoring and Alerting]], [[Database Backups]], restore drills, [[Service Level Objectives]] |
| **Confidentiality** | is designated data protected | [[Encryption at Rest]], [[Encryption in Transit]], [[Least Privilege]] |
| **Processing integrity** | is processing complete and accurate | validation, reconciliation, error handling |
| **Privacy** | is personal data handled as notified | consent, retention, deletion |

Most B2B SaaS scopes Security plus Availability and
Confidentiality, and leaves the other two out. Scope
narrowly — every criterion added is more evidence forever.

## The common criteria structure

Security is expressed as nine common criteria (CC1-CC9)
covering control environment, communication, risk
assessment, monitoring, control activities, logical and
physical access, operations, change management and risk
mitigation. Change management is where your
[[Continuous Integration and Delivery]] pipeline earns
its keep.

## Related

[[SOC 2]] · [[Encryption at Rest]] · [[Audit Logging]] ·
[[Access Review]] · [[Shared Responsibility Model]]

## Sources

- [[aicpa-soc2-overview]] · [[vanta-soc2-checklist]] ·
  [[drata-soc2-compliance]] ·
  [[aws-well-architected-security-pillar]]
