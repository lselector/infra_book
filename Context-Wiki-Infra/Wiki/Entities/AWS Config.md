---
type: Service
title: "AWS Config"
description: "Continuous recording of resource configuration, and rules that flag drift."
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Config

Records the configuration of your AWS resources over time
and evaluates them against rules, reporting compliant and
non-compliant status.

## What it is for

- **Drift detection.** What changed, when, and from what
  to what — including changes made by hand in the console
  that your [[Infrastructure as Code]] does not know
  about.
- **Continuous compliance.** Managed rules cover common
  expectations: unencrypted volumes, public buckets, MFA
  on root, key rotation disabled.
- **Evidence.** A continuously evaluated control is
  exactly what a [[SOC 2]] Type II observation window
  needs, and it produces the record automatically.

## Watch out for

Cost scales with the number of configuration items
recorded and rule evaluations. On a large account this is
a real line; scope the recorder rather than enabling
everything everywhere.

## Related

[[Audit Logging]] · [[AWS CloudTrail]] · [[SOC 2]] ·
[[Infrastructure as Code]] · [[Cost Control]]

## Sources

- [[aws-config-what-is]] ·
  [[aws-well-architected-security-pillar]]
