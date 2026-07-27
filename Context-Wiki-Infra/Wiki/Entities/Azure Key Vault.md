---
type: Service
title: "Azure Key Vault"
description: "Microsoft's combined store for keys, secrets and certificates."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Azure Key Vault

One service covering three things: cryptographic keys
(like a KMS), secrets (like a secret store), and TLS
certificates with managed renewal.

## Why it is here

Completeness — if your stack is on Azure, this is the
equivalent of [[AWS KMS]] plus
[[AWS Secrets Manager]]. The certificate management is a
genuine convenience the others do not bundle.

## Notes

- Standard and Premium tiers; Premium provides
  HSM-backed keys — see [[Hardware Security Module]].
- Access via Azure RBAC or vault access policies; RBAC is
  the current recommendation.
- Soft delete and purge protection guard against
  accidental and malicious deletion — enable both.

## Related

[[Secrets Management]] · [[AWS KMS]] ·
[[Google Cloud KMS]] · [[Hardware Security Module]]

## Sources

- [[azure-key-vault-overview]]
