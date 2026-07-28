---
type: Service
title: "Google Cloud Audit Logs"
description: "Google Cloud's record of administrative and data access activity."
wikipedia: "https://en.wikipedia.org/wiki/Google_Cloud_Platform"
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud Audit Logs

Four log streams per project: Admin Activity, Data Access,
System Event and Policy Denied.

## The important distinction

- **Admin Activity** is always on, free, and retained for
  400 days. Configuration changes land here.
- **Data Access** is off by default for most services,
  charged, and is where reads of your data are recorded.
  Enable it for the services holding sensitive data if you
  need that evidence.

## Using it

- Export to a log bucket or BigQuery for retention beyond
  the default.
- Alert on high-signal events — IAM policy changes,
  service account key creation, [[Google Cloud KMS]] key
  destruction.
- Restrict who can read the logs; they describe your
  environment in detail.

## Related

[[Audit Logging]] · [[AWS CloudTrail]] · [[SOC 2]] ·
[[Google Cloud KMS]] · [[Monitoring and Alerting]]

## Sources

- [[gcp-cloud-audit-logs]] · [[gcp-soc2-compliance]]
