---
type: Concept
title: "Infrastructure as Code"
description: "Declaring infrastructure in files - valuable when there is enough of it to forget."
wikipedia: "https://en.wikipedia.org/wiki/Infrastructure_as_code"
tags: [scaling, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Infrastructure as Code

Servers, DNS records, buckets and policies described in
version-controlled files and applied by a tool.

## Why it matters here

- **Reproducibility.** Rebuilding after a disaster becomes
  `terraform apply` rather than archaeology.
- **Review.** Infrastructure changes go through the same
  pull request as code.
- **Drift detection.** The tool tells you what someone
  changed by hand in the console.

## When to introduce it

Not at rung 5. One VPS and five DNS records are faster to
click than to codify, and the state file is another thing
to look after.

The signal is usually: a second environment, or the third
time you rebuild something and get it subtly different.

## The options here

[[Terraform]] — largest provider ecosystem, its own
configuration language, the default choice.
[[Pulumi]] — the same model expressed in a general-purpose
programming language.

## Watch out for

- The state file. It contains secrets and is the single
  point of truth; store it remotely with locking, never in
  Git.
- Codifying half your infrastructure. Partial IaC gives
  you the costs without the reproducibility.

## Related

[[Terraform]] · [[Pulumi]] · [[Deployment Environments]] ·
[[Continuous Integration and Delivery]] ·
[[Anti-Patterns]]

## Sources

- [[terraform-intro]] · [[terraform-language]] ·
  [[terraform-iac-tutorial]] · [[pulumi-iac-concepts]]
