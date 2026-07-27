---
type: Concept
title: "Key Rotation"
description: "Replacing key material on a schedule, and why it does not mean re-encrypting everything."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Key Rotation

Periodically retiring key material and issuing new, so
that a compromised key has a bounded blast radius.

## How managed KMS rotation actually works

[[AWS KMS]] and [[Google Cloud KMS]] rotate the *backing
key* while the key identifier stays the same. New
encryptions use the new material; old ciphertexts remain
decryptable with the retained old material. Nothing needs
re-encrypting, and your application does not change.

With [[Envelope Encryption]], rotating the master key is
therefore near-free — only data keys reference it.

## What still requires work

- **Application secrets** — an API key or database
  password must be replaced on both sides, which needs a
  window where both old and new are valid.
- **Signing keys** for [[JSON Web Token]] — publish the
  new public key before signing with the new private key.

## Why it matters here

Annual rotation is a common control expectation under
[[SOC 2]], and for managed KMS keys it is one checkbox.
Turn it on; it costs nothing.

## Related

[[Envelope Encryption]] · [[AWS KMS]] ·
[[Google Cloud KMS]] · [[Secrets Management]] · [[SOC 2]]

## Sources

- [[aws-kms-rotate-keys]] · [[gcp-kms-key-rotation]] ·
  [[owasp-key-management-cheatsheet]]
