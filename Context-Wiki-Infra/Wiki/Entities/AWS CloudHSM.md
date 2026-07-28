---
type: Service
title: "AWS CloudHSM"
description: "A dedicated, single-tenant HSM cluster - expensive, and required only when a contract says so."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Web_Services"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS CloudHSM

Dedicated FIPS 140-2 Level 3 hardware security modules in
your VPC, which you administer and to which AWS has no
access to your keys.

## What it gives over AWS KMS

- **Single tenancy** — the hardware is yours alone.
- **Exclusive control** — AWS cannot use or recover your
  keys, which is the point for some regulators.
- Standard interfaces (PKCS#11, JCE, OpenSSL engine) for
  applications that expect an HSM.

## What it costs you

Hundreds to thousands of dollars a month, plus real
operational responsibility: you manage users, quorum
policies and cluster backups. **If you lose the keys,
nobody can recover them.**

## The decision

Use [[AWS KMS]], whose keys are already HSM-protected at
about $1/key/month. Move to CloudHSM only when a specific
regulation or contract names dedicated, single-tenant
custody — payment processing, or running your own
certificate authority. Never because it sounds stronger.

## Related

[[Hardware Security Module]] · [[AWS KMS]] ·
[[Google Cloud KMS]] · [[Encryption at Rest]] ·
[[Cost Control]]

## Sources

- [[aws-cloudhsm-intro]] · [[nist-cmvp-fips-140]] ·
  [[gcp-cloud-hsm]]
