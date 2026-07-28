---
type: Service
title: "AWS Secrets Manager"
description: "Managed secret storage with built-in rotation - and a per-secret monthly fee."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Web_Services"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Secrets Manager

Stores secrets encrypted with [[AWS KMS]], controls access
through IAM, logs every retrieval to
[[AWS CloudTrail]], and can rotate supported secrets
automatically.

## What distinguishes it

**Automatic rotation.** For [[Amazon RDS]] credentials it
will generate a new password, update the database and
update the secret, on a schedule, with no downtime. That
is the feature you are paying for.

## Cost

About $0.40 per secret per month plus API charges. With
many secrets this adds up, which is why
[[AWS Systems Manager Parameter Store]] is the common
alternative — it stores encrypted values at no per-secret
charge, without the rotation machinery.

## The rule of thumb

- Needs rotation, or is a database credential → Secrets
  Manager.
- Static configuration and API keys → Parameter Store.

## Related

[[Secrets Management]] ·
[[AWS Systems Manager Parameter Store]] · [[AWS KMS]] ·
[[Key Rotation]] · [[Least Privilege]]

## Sources

- [[aws-secrets-manager-intro]] · [[aws-parameter-store]]
