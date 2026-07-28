---
type: Service
title: "AWS Artifact"
description: "Where you download AWS's own SOC 2 report to give your auditor."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Web_Services"
tags: [compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Artifact

Self-service portal for AWS's audit reports and
compliance documents — SOC 1, SOC 2, SOC 3, ISO
certificates, PCI attestations.

## Why it matters to a small team

Under the [[Shared Responsibility Model]] you **inherit**
controls from AWS: physical data centre security,
environmental controls, hardware disposal. You cannot
evidence those yourself, and you do not have to — you
provide AWS's report.

This is one of the reasons a [[SOC 2]] examination for a
cloud-hosted product is achievable at all for a small
company: a meaningful share of the control surface is
inherited and already audited.

## Practical notes

- Most reports require accepting an NDA before download.
- Reports are periodic — download the current one during
  your audit window, not a stale copy.
- Google and Cloudflare publish equivalents through their
  own trust portals.

## Related

[[Shared Responsibility Model]] · [[SOC 2]] ·
[[Trust Services Criteria]] · [[Vanta]]

## Sources

- [[aws-artifact-what-is]] · [[aws-soc-faqs]] ·
  [[gcp-soc2-compliance]] ·
  [[cloudflare-trust-hub-compliance]]
