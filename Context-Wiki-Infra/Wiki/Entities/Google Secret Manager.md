---
type: Service
title: "Google Secret Manager"
description: "Google Cloud's secret store - versioned, IAM-controlled, audit-logged."
wikipedia: "https://en.wikipedia.org/wiki/Google_Cloud_Platform"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Secret Manager

Stores secrets as versioned resources, encrypted at rest,
with IAM access control and access logging to
[[Google Cloud Audit Logs]].

## The model

A *secret* is a container; a *version* is a value. Code
references either a specific version or `latest`.
Rotation is adding a new version and disabling the old,
which gives a clean rollback path.

## Practical notes

- Grant `secretAccessor` on individual secrets rather than
  project-wide — [[Least Privilege]].
- Bind the role to the workload's service account so no
  credential is stored anywhere.
- CMEK is supported if you need key custody via
  [[Google Cloud KMS]].

## Watch out for

Pinning to `latest` means a bad new version breaks
production instantly with no deploy. Pin to a version in
production and promote deliberately.

## Related

[[Secrets Management]] · [[Google Cloud KMS]] ·
[[AWS Secrets Manager]] · [[Least Privilege]]

## Sources

- [[gcp-secret-manager-overview]] · [[gcp-cmek]]
