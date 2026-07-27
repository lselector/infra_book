---
type: Summary
title: "AWS KMS — rotating KMS keys"
description: "To create new cryptographic material for your customer managed keys, you can create new KMS keys, and then change your applications or aliases to use the new KMS keys."
resource: "https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html"
source_file: "Raw/05_ops_cicd_security/aws-kms-rotate-keys.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS KMS — rotating KMS keys

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-kms-rotate-keys.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>

## Opening

> To create new cryptographic material for your [customer managed keys](concepts.md#customer-mgn-key), you can create new KMS keys, and then change your applications or aliases to use the new KMS keys. Or, you can rotate the key material associated with an existing KMS key by enabling automatic key ...
> By default, when you enable *automatic key rotation* for a KMS key, AWS KMS generates new cryptographic material for the KMS key every year. You can also specify a custom [rotation-period](#rotation-period) to define the number of days after you enable automatic key rotation that AWS KMS will ...
> You can [track the rotation](#monitor-key-rotation) of key material for your KMS keys in Amazon CloudWatch, AWS CloudTrail, and the AWS Key Management Service console. You can also use [GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html) ...
> Key rotation changes only the *current key material*, which is the cryptographic secret that is used in encryption operations. When you use the rotated KMS key to decrypt ciphertext, AWS KMS uses the key material that was used to encrypt it. You cannot select a particular key material for decrypt ...

## Contents of the source document

- Rotate AWS KMS keys
  - Why rotate KMS keys?
  - How key rotation works

## Related pages

[[AWS CloudTrail]] · [[AWS KMS]] · [[Encryption at Rest]] · [[HTTP]] · [[Key Rotation]]
