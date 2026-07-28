---
type: Service
title: "Google Cloud KMS"
description: "Google's key management service - the same envelope-encryption model, with CMEK across GCP."
wikipedia: "https://en.wikipedia.org/wiki/Google_Cloud_Platform"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud KMS

Key management for Google Cloud: key rings, keys, and key
versions, with software, HSM and external protection
levels.

## The structure to know

- **Key ring** — a regional container for keys.
- **Key** — the logical key you reference.
- **Key version** — the actual material. Rotation creates
  a new version; older versions stay available to decrypt
  existing ciphertext.

That versioning model is why [[Key Rotation]] does not
require re-encrypting anything.

## CMEK

Customer-managed encryption keys let you supply the key
protecting data in other Google Cloud services. Google
encrypts everything at rest by default with its own keys;
CMEK is what you use when you need control, revocation and
an audit trail of key use.

## HSM protection level

Selecting `HSM` places key material in FIPS 140-2 Level 3
hardware for a modest premium over the software level —
considerably cheaper than a dedicated Cloud HSM cluster.
See [[Hardware Security Module]].

## Related

[[AWS KMS]] · [[Envelope Encryption]] · [[Key Rotation]] ·
[[Encryption at Rest]] · [[Hardware Security Module]]

## Sources

- [[gcp-kms-overview]] · [[gcp-kms-envelope-encryption]] ·
  [[gcp-kms-key-rotation]] · [[gcp-cmek]] ·
  [[gcp-cloud-hsm]] · [[gcp-encryption-at-rest]]
