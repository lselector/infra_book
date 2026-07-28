---
type: Concept
title: "Hardware Security Module"
description: "A tamper-resistant device that holds keys and never gives them back - and when you need a dedicated one."
wikipedia: "https://en.wikipedia.org/wiki/Hardware_security_module"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Hardware Security Module

Dedicated hardware that generates and stores keys and
performs cryptographic operations internally. Key material
cannot be exported, only used.

## What it buys

- **Non-exportability.** An attacker with full software
  access still cannot copy the key.
- **Tamper resistance**, physical and logical.
- **Validated assurance** — FIPS 140-2/140-3 levels, which
  is the language contracts and regulators use.

## The important practical point

You are almost certainly already using HSMs. [[AWS KMS]]
keys are protected by FIPS-validated HSMs by default, at
about $1 per key per month. You get the assurance without
operating anything.

A *dedicated* HSM — [[AWS CloudHSM]] or Google Cloud HSM —
costs orders of magnitude more and exists for
single-tenant custody requirements: payment processing, a
regulator demanding exclusive control, or running your own
certificate authority.

## The decision

Use the managed KMS. Move to a dedicated HSM only when a
contract or regulation names the requirement — never
because it sounds more secure.

## Related

[[AWS KMS]] · [[Google Cloud KMS]] · [[AWS CloudHSM]] ·
[[Envelope Encryption]] · [[Encryption at Rest]]

## Sources

- [[aws-cloudhsm-intro]] · [[gcp-cloud-hsm]] ·
  [[nist-cmvp-fips-140]] · [[aws-kms-overview]]
