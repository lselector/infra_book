---
type: Tool
title: "SOPS"
description: "Encrypted secrets files that live in Git, decrypted by a KMS key."
website: "https://getsops.io/"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# SOPS

Encrypts the *values* in a YAML, JSON, ENV or INI file
while leaving the keys readable, using [[AWS KMS]],
[[Google Cloud KMS]], Azure Key Vault, age or PGP.

## Why the design is clever

Because only values are encrypted, the file still diffs
sensibly in Git: you can see that `DATABASE_URL` changed
without seeing either value. That makes committed secrets
reviewable, which is normally the objection to them.

Access control is delegated to the KMS: whoever can use
the key can decrypt, so revocation is an IAM change rather
than a re-encryption.

## When it fits

- GitOps workflows where configuration must live in the
  repository.
- Small teams who want versioned secrets without running
  [[HashiCorp Vault]].

## Watch out for

The ciphertext is in Git forever. If the KMS key is ever
compromised, history is readable — so rotate the
underlying secrets, not just the key. See
[[Secrets Management]].

## Related

[[Secrets Management]] · [[AWS KMS]] ·
[[Google Cloud KMS]] · [[Gitleaks]]

## Sources

- [[sops-readme]] ·
  [[owasp-secrets-management-cheatsheet]]
