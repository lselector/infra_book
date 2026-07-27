---
type: Summary
title: "OWASP — authorization cheat sheet (least privilege, access reviews)"
description: "Authorization may be defined as 'the process of verifying that a requested action or service is approved for a specific entity' (NIST)."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-authorization-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — authorization cheat sheet (least privilege, access reviews)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-authorization-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>

## Opening

> Authorization may be defined as "the process of verifying that a requested action or service is approved for a specific entity" ([NIST](https://csrc.nist.gov/glossary/term/authorization)). Authorization is distinct from authentication which is the process of verifying an entity's identity. When ...
> The objective of this cheat sheet is to assist developers in implementing authorization logic that is robust, appropriate to the app's business context, maintainable, and scalable. The guidance provided in this cheat sheet should be applicable to all phases of the development lifecycle and flexible ...
> Flaws related to authorization logic are a notable concern for web apps. Broken Access Control was ranked as the most concerning web security vulnerability in [OWASP's 2021 Top 10](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) and asserted to have a "High" likelihood of exploit by ...
> The potential impact resulting from exploitation of authorization flaws is highly variable, both in form and severity. Attackers may be able to read, create, modify, or delete resources that were meant to be protected (thus jeopardizing their confidentiality, integrity, and/or availability); ...

## Contents of the source document

- Authorization Cheat Sheet¶
  - Introduction¶
  - Recommendations¶
    - Enforce Least Privileges¶
    - Deny by Default¶
    - Validate the Permissions on Every Request¶
    - Prefer Attribute and Relationship Based Access Control over RBAC¶
    - Ensure Lookup IDs are Not Accessible Even When Guessed or Cannot Be Tampered With¶
    - Enforce Authorization Checks on Static Resources¶
    - Verify that Authorization Checks are Performed in the Right Location¶
    - Exit Safely when Authorization Checks Fail¶
    - Implement Appropriate Logging¶
    - Create Unit and Integration Test Cases for Authorization Logic¶
  - References¶
    - ABAC¶
    - General¶
    - Least Privilege¶
    - RBAC¶

## Related pages

[[Amazon S3]] · [[Authentication]] · [[Authorization]] · [[Django]] · [[HTTP]] · [[Incident Response]] · [[JSON Web Token]] · [[Least Privilege]] · [[OWASP]] · [[Security Testing]]
