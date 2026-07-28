---
type: Tool
title: "HashiCorp Vault"
description: "Self-hostable secret management with dynamic, short-lived credentials."
wikipedia: "https://en.wikipedia.org/wiki/HashiCorp"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# HashiCorp Vault

A secrets platform that stores static secrets and, more
interestingly, **generates dynamic ones**.

## The idea worth knowing

Vault can issue a database credential that exists for one
hour and is then revoked automatically. There is no
long-lived password to leak, and revocation is
instantaneous — the stage-4 destination described in
[[Secrets Management]].

It also does encryption-as-a-service (transit), so an
application can encrypt data without handling key
material, similar to [[Envelope Encryption]].

## The cost

Vault is a stateful, highly-available service that you
must operate: unsealing, storage backend, upgrades,
backups. That is real work.

## The recommendation here

For a small project on a single cloud, use the managed
option — [[AWS Secrets Manager]],
[[AWS Systems Manager Parameter Store]] or
[[Google Secret Manager]]. Vault earns its keep when you
are multi-cloud, need dynamic credentials, or must
self-host for policy reasons.

## Related

[[Secrets Management]] · [[Key Rotation]] ·
[[Least Privilege]] · [[Envelope Encryption]]

## Sources

- [[vault-what-is-vault]]
