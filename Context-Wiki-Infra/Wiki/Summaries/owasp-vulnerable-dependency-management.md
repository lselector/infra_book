---
type: Summary
title: "OWASP — vulnerable dependency management cheat sheet"
description: "The objective of the cheat sheet is to provide a proposal of approach regarding the handling of vulnerable third-party dependencies when they are detected, and this, depending on different s"
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-vulnerable-dependency-management.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — vulnerable dependency management cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-vulnerable-dependency-management.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html>

## Opening

> The objective of the cheat sheet is to provide a proposal of approach regarding the handling of vulnerable third-party dependencies when they are detected, and this, depending on different situation.
> The cheat sheet is not tools oriented but it contains a [tools](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html#tools) section informing the reader about free and commercial solutions that can be used to detect vulnerable dependencies, depending on ...
> Proposals mentioned in this cheat sheet are not silver-bullet (recipes that work in all situations) yet can be used as a foundation and adapted to your context.
> Most of the projects use third-party dependencies to delegate handling of different kind of operations, _e.g._ generation of document in a specific format, HTTP communications, data parsing of a specific format, etc.

## Contents of the source document

- Vulnerable Dependency Management Cheat Sheet¶
  - Introduction¶
  - Context¶
  - Remark about the detection¶
    - 1\. Responsible disclosure¶
    - 2\. Full disclosure¶
  - Remark about the security issue handling decision¶
  - Cases¶
    - Case 1¶
    - Case 2¶
    - Case 3¶
    - Case 4¶
  - Tools¶

## Related pages

[[Container Images]] · [[Docker]] · [[HTTP]] · [[Kubernetes]] · [[OWASP]] · [[OWASP Top 10]] · [[Rust]] · [[Trivy]]
