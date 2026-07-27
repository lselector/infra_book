---
type: Summary
title: "Google Cloud KMS — key management service overview"
description: "Cloud Key Management Service (Cloud KMS) lets you create and manage cryptographic keys for use in compatible Google Cloud services and in your own applications."
resource: "https://cloud.google.com/kms/docs/key-management-service"
source_file: "Raw/05_ops_cicd_security/gcp-kms-overview.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud KMS — key management service overview

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-kms-overview.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/kms/docs/key-management-service>

## Opening

> Cloud Key Management Service (Cloud KMS) lets you create and manage cryptographic keys for use in compatible Google Cloud services and in your own applications. Using Cloud KMS, you can do the following:
> You can use the following table to identify which type of encryption meets your needs for each use case. The best solution for your needs might include a mix of encryption approaches. For example, you might use software keys for your least sensitive data and hardware or external keys for your most ...
> Encryption type | Cost | Compatible services | Features
> [ Google-owned and Google-managed encryption keys (Google Cloud default encryption)](https://cloud.google.com/docs/security/encryption/default-encryption#googles_default_encryption) | Included | All Google Cloud services that store customer data  |

## Contents of the source document

  - Choose the right encryption for your needs
  - Protecting data in Google Cloud
    - Google-owned and Google-managed encryption keys (Google Cloud default encryption)
    - Customer-managed encryption keys (CMEKs)
    - Cloud KMS keys
    - Multi-tenant Cloud HSM for Google Workspace
    - Customer-supplied encryption keys (CSEKs)
    - Confidential Computing

## Related pages

[[Authentication]] · [[Envelope Encryption]] · [[Google Cloud KMS]] · [[Key Rotation]]
