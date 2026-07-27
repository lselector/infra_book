---
type: Summary
title: "OWASP — secrets management cheat sheet"
description: "Secrets are being used everywhere nowadays, especially with the popularity of the DevOps movement."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-secrets-management-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — secrets management cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-secrets-management-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>

## Opening

> Secrets are being used everywhere nowadays, especially with the popularity of the DevOps movement. Application Programming Interface (API) keys, database credentials, Identity and Access Management (IAM) permissions, Secure Shell (SSH) keys, certificates, etc. Many organizations have them hardcoded ...
> There is a growing need for organizations to centralize the storage, provisioning, auditing, rotation and management of secrets to control access to secrets and prevent them from leaking and compromising the organization. Often, services share the same secrets, which makes identifying the source of ...
> This cheat sheet offers best practices and guidelines to help properly implement secrets management.
> The following sections address the main concepts relating to secrets management.

## Contents of the source document

- Secrets Management Cheat Sheet¶
  - 1 Introduction¶
  - 2 General Secrets Management¶
    - 2.1 High Availability¶
    - 2.2 Centralize and Standardize¶
    - 2.3 Access Control¶
    - 2.4 Automate Secrets Management¶
    - 2.5 Handling Secrets in Memory¶
    - 2.6 Auditing¶
    - 2.7 Secret Lifecycle¶
    - 2.8 Transport Layer Security (TLS) Everywhere¶
    - 2.9 Downtime, Break-glass, Backup and Restore¶
    - 2.10 Policies¶
    - 2.11 Metadata: prepare to move the secret¶
    - 2.12 Passwordless Authentication and Token Security¶
  - 3 Continuous Integration (CI) and Continuous Deployment (CD)¶
    - 3.1 Hardening your CI/CD pipeline¶
    - 3.2 Where should a secret be?¶

## Related pages

[[AWS Secrets Manager]] · [[Azure Key Vault]] · [[Encryption at Rest]] · [[Encryption in Transit]] · [[Envelope Encryption]] · [[Google Secret Manager]] · [[HashiCorp Vault]] · [[Incident Response]] · [[Least Privilege]] · [[Multi-Factor Authentication]] · [[OAuth 2.0 and OpenID Connect]] · [[Secrets Management]]
