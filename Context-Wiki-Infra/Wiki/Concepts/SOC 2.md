---
type: Concept
title: "SOC 2"
description: "An audited report on how you protect customer data - what it is, what it costs, and when to start."
wikipedia: "https://en.wikipedia.org/wiki/System_and_organization_controls"
tags: [compliance, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# SOC 2

An examination by a licensed CPA firm of whether your
controls meet the [[Trust Services Criteria]], resulting
in a report you can give to customers.

## Type I versus Type II

- **Type I** — controls are suitably designed at a point
  in time. Faster, cheaper, and less persuasive.
- **Type II** — controls *operated effectively* across an
  observation window, typically 3-12 months. This is what
  enterprise buyers actually want.

The window is why starting early matters: you cannot
compress it. Turning on [[Audit Logging]] the week before
the audit produces a window of one week.

## What it actually costs

The audit itself is commonly $10-40k. A compliance
automation platform ([[Vanta]], [[Drata]]) adds several
thousand a year and removes much of the evidence-gathering
labour. Add internal time, which is the largest hidden
cost.

## When to start

When a deal requires it — almost always the real trigger —
or when you can see that it will. It is a sales
requirement, not a security one; the security work is
worth doing regardless and mostly precedes it.

## The good news

If you have followed this book you already have much of
it: [[Encryption in Transit]] and
[[Encryption at Rest]], [[Least Privilege]],
[[Continuous Integration and Delivery]] change
management, [[Database Backups]],
[[Monitoring and Alerting]] and
[[Incident Response]]. What is usually missing is
*evidence* and *policies*, not controls.

## Related

[[Trust Services Criteria]] · [[Audit Logging]] ·
[[Access Review]] · [[Shared Responsibility Model]] ·
[[Incident Response]]

## Sources

- [[aicpa-soc2-overview]] · [[vanta-what-is-soc2]] ·
  [[vanta-soc2-checklist]] · [[drata-soc2-compliance]] ·
  [[aws-soc-faqs]] · [[iso-27001-offering]]

> **Caveat:** the AICPA does not publish the Trust
> Services Criteria document at a fetchable URL, so the
> criterion-level detail in `Raw/` comes from vendor
> guides. Verify against the official TSC before relying
> on any specific requirement.
