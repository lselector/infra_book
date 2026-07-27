---
type: Summary
title: "OWASP — input validation cheat sheet"
description: "This article is focused on providing clear, simple, actionable guidance for providing Input Validation security functionality in your applications."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-input-validation-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — input validation cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-input-validation-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html>

## Opening

> This article is focused on providing clear, simple, actionable guidance for providing Input Validation security functionality in your applications.
> Input validation is performed to ensure only properly formed data is entering the workflow in an information system, preventing malformed data from persisting in the database and triggering malfunction of various downstream components. Input validation should happen as early as possible in the data ...
> Data from all potentially untrusted sources should be subject to input validation, including not only Internet-facing web clients but also backend feeds over extranets, from [suppliers, partners, vendors or ...
> Input Validation should not be used as the _primary_ method of preventing [XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [SQL Injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) and other ...

## Contents of the source document

- Input Validation Cheat Sheet¶
  - Introduction¶
  - Goals of Input Validation¶
  - Input Validation Strategies¶
  - Implementing Input Validation¶
    - Allowlist vs Denylist¶
    - Validating Free-form Unicode Text¶
    - Regular Expressions (Regex)¶
  - Allowlist Regular Expression Examples¶
  - Client-side vs Server-side Validation¶
  - Validating Rich User Content¶
  - Preventing XSS and Content Security Policy¶
  - File Upload Validation¶
    - Upload Verification¶
    - Upload Storage¶
    - Public Serving of Uploaded Content¶
    - Beware of Specific File Types¶
    - Image Upload Verification¶

## Related pages

[[Authentication]] · [[Django]] · [[HTTP]] · [[OWASP]] · [[OWASP Top 10]]
