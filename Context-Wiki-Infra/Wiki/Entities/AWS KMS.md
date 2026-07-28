---
type: Service
title: "AWS KMS"
description: "Managed key management backed by FIPS-validated HSMs - about $1 per key per month."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Web_Services"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS KMS

Creates and controls encryption keys. Key material is
generated in and never leaves FIPS 140-3 validated
[[Hardware Security Module]]s, and every use is an
authorised, logged API call.

## What you actually do with it

- **Encrypt other AWS services' data** — S3 objects, EBS
  volumes, RDS instances — with a customer-managed key
  rather than an AWS-managed one, which gives you the
  audit trail and the ability to revoke.
- **[[Envelope Encryption]] in your own application** for
  the few genuinely sensitive fields:
  `GenerateDataKey`, encrypt locally, store the ciphertext
  and the encrypted data key together.

## Access control

A **key policy** is attached to the key and is the primary
control — no principal, including the account root, has
access unless the key policy allows it. IAM policies can
grant further, but cannot grant what the key policy has
not enabled. This catches people out.

## Rotation

Automatic annual rotation of the backing key, with the key
ID unchanged and old ciphertexts still decryptable. One
checkbox, no re-encryption. See [[Key Rotation]].

## Cost

About $1 per key per month plus per-request charges — a
rounding error compared to [[AWS CloudHSM]].

## Related

[[Envelope Encryption]] · [[Hardware Security Module]] ·
[[Key Rotation]] · [[Google Cloud KMS]] ·
[[Encryption at Rest]] · [[AWS CloudTrail]]

## Sources

- [[aws-kms-product-page]] · [[aws-kms-overview]] ·
  [[aws-kms-concepts]] · [[aws-kms-key-policies]] ·
  [[aws-kms-rotate-keys]] · [[aws-s3-sse-kms]]
