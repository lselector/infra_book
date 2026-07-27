---
type: Concept
title: "Envelope Encryption"
description: "Encrypt data with a data key, encrypt the data key with a KMS key - the pattern behind every cloud KMS."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Envelope Encryption

Two layers of key. The data is encrypted with a fast
symmetric **data key**; the data key is itself encrypted
by a **key encryption key** that never leaves the KMS.

## The flow

1. Ask the KMS to generate a data key. It returns the key
   in plaintext *and* encrypted under your KMS key.
2. Encrypt your data locally with the plaintext data key.
3. Store the ciphertext **and** the encrypted data key
   together. Discard the plaintext data key from memory.
4. To decrypt: send the encrypted data key to the KMS, get
   the plaintext back, decrypt locally.

## Why it is built this way

- Large payloads never travel to the KMS — only a 32-byte
  key does.
- The master key material never leaves the service, and on
  [[AWS KMS]] never leaves a
  [[Hardware Security Module]].
- Every use of the master key is an authorised, logged API
  call, which is what makes [[Audit Logging]] of key use
  possible.
- Rotating the master key does not require re-encrypting
  your data — see [[Key Rotation]].

## Watch out for

Losing the encrypted data key. It is not recoverable from
the ciphertext; store the two together, always.

## Related

[[AWS KMS]] · [[Google Cloud KMS]] · [[Key Rotation]] ·
[[Hardware Security Module]] · [[Encryption at Rest]]

## Sources

- [[aws-kms-concepts]] · [[gcp-kms-envelope-encryption]] ·
  [[owasp-cryptographic-storage-cheatsheet]]
