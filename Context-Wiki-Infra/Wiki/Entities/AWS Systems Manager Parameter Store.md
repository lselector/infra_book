---
type: Service
title: "AWS Systems Manager Parameter Store"
description: "Free encrypted parameter storage - the cheap default for configuration and API keys on AWS."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Systems Manager Parameter Store

Hierarchical storage for configuration values and secrets.
`SecureString` parameters are encrypted with [[AWS KMS]]
and access is governed by IAM.

## Why it is often the better choice

Standard parameters cost nothing per secret. For a small
application with a dozen API keys and connection strings,
that is the entire difference from
[[AWS Secrets Manager]] — which charges per secret and
adds rotation you may not need.

## Useful properties

- Hierarchical paths — `/myapp/prod/db-url` — so IAM
  policies can grant access to a whole environment's
  parameters at once.
- Versioning, so you can see and revert changes.
- Retrieval is logged to [[AWS CloudTrail]], which is
  [[Audit Logging]] evidence.

## Watch out for

Throughput limits on the standard tier under heavy
polling. Fetch parameters at startup and cache them rather
than reading per request.

## Related

[[Secrets Management]] · [[AWS Secrets Manager]] ·
[[AWS KMS]] · [[Audit Logging]]

## Sources

- [[aws-parameter-store]] · [[aws-secrets-manager-intro]]
