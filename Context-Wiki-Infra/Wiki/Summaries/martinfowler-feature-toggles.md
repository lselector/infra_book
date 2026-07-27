---
type: Summary
title: "Feature toggles (feature flags) — Martin Fowler"
description: "Feature Toggles (often also refered to as Feature Flags) are a powerful technique, allowing teams to modify system behavior without changing code."
resource: "https://martinfowler.com/articles/feature-toggles.html"
source_file: "Raw/08_scaling_maturity/martinfowler-feature-toggles.md"
tags: [scaling, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Feature toggles (feature flags) — Martin Fowler

Extractive digest of the immutable capture in
`Raw/08_scaling_maturity/martinfowler-feature-toggles.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://martinfowler.com/articles/feature-toggles.html>

## Opening

> _Feature Toggles (often also refered to as Feature Flags) are a powerful technique, allowing teams to modify system behavior without changing code. They fall into various usage categories, and it's important to take that categorization into account when implementing and managing toggles. Toggles ...
> 09 October 2017
> [](https://thepete.net)
> [Pete Hodgson](https://thepete.net)

## Contents of the source document

- Feature Toggles (aka Feature Flags)
  - Contents
  - A Toggling Tale
    - The birth of a Feature Flag
    - Making a flag dynamic
    - Getting ready to release
    - Canary releasing
    - A/B testing
  - Categories of toggles
    - Release Toggles
    - Experiment Toggles
    - Ops Toggles
    - Permissioning Toggles
    - Managing different categories of toggles
  - Implementation Techniques
    - De-coupling decision points from decision logic
    - Inversion of Decision
    - Avoiding conditionals

## Related pages

[[HTTP]] · [[Infrastructure as Code]] · [[Render]]
