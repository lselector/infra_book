---
type: Summary
title: "Google Cloud — customer-managed encryption keys (CMEK)"
description: "This document provides an overview of using Cloud Key Management Service (Cloud KMS) for customer-managed encryption keys (CMEK)."
resource: "https://cloud.google.com/kms/docs/cmek"
source_file: "Raw/05_ops_cicd_security/gcp-cmek.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud — customer-managed encryption keys (CMEK)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-cmek.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/kms/docs/cmek>

## Opening

> This document provides an overview of using Cloud Key Management Service (Cloud KMS) for customer-managed encryption keys (CMEK). Using Cloud KMS CMEK gives you ownership and control of the keys that protect your data at rest in Google Cloud.
> The Cloud KMS keys that you create are customer-managed keys. Google Cloud services that use your keys are said to have a _CMEK integration_. You can manage these CMEKs directly, or through [Cloud KMS Autokey](https://cloud.google.com/kms/docs/autokey-overview). The following factors differentiate ...
> Type of key | Cloud KMS Autokey | Cloud KMS customer-managed (manual) | Google-owned and Google-managed encryption key (Google default encryption)
> Can view key metadata | Yes | Yes | No

## Contents of the source document

  - Comparison of CMEK and Google-owned and Google-managed encryption keys
    - Default encryption with Google-owned and Google-managed encryption keys
    - Customer-managed encryption keys (CMEK)
    - Customer-managed encryption keys (CMEK) with Cloud KMS Autokey
  - When to use customer-managed encryption keys
  - What a CMEK-integrated service provides
    - CMEK-integrated services track keys and resources
    - CMEK-integrated services handle resource access
  - Using Autokey for CMEK
  - Manually creating CMEKs
    - CMEK compliance
  - Key usage tracking
  - CMEK organization policies
  - What's next

## Related pages

[[Encryption at Rest]] · [[Envelope Encryption]] · [[Key Rotation]]
