---
type: Summary
title: "Google Cloud Audit Logs — who did what, where, and when"
description: "This document provides a conceptual overview of Cloud Audit Logs."
resource: "https://cloud.google.com/logging/docs/audit"
source_file: "Raw/05_ops_cicd_security/gcp-cloud-audit-logs.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud Audit Logs — who did what, where, and when

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-cloud-audit-logs.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/logging/docs/audit>

## Opening

> This document provides a conceptual overview of Cloud Audit Logs.
> Google Cloud services write audit logs that record administrative activities and accesses within your Google Cloud resources. Audit logs help you answer "who did what, where, and when?" within your Google Cloud resources with the same level of transparency as in on-premises environments. Enabling ...
> For a list of Google Cloud services that provide audit logs, see [Google Cloud services with audit logs](https://cloud.google.com/logging/docs/audit/services). All Google Cloud services will eventually provide audit logs.
> Google Cloud MCP servers write Data Access audit logs. Data Access audit logs written by Google Cloud MCP servers API calls are service-specific and use the format `SERVICE_NAME.googleapis.com/mcp`. You can enable these Data Access logs by turning on audit logging for `mcp.googleapis.com` in the ...

## Contents of the source document

  - Google Cloud services producing audit logs
  - Required roles
  - Types of audit logs
    - Admin Activity audit logs
    - Data Access audit logs
    - System Event audit logs
    - Policy Denied audit logs
  - Audit log entry structure
    - Log name
  - Caller identities in audit logs
  - IP address of the caller in audit logs
  - Viewing audit logs
    - Console
    - gcloud
    - REST
  - Storing and routing audit logs
  - Audit log retention
  - Access control

## Related pages

[[Audit Logging]] · [[Authentication]] · [[Firebase Authentication]] · [[Google Cloud Audit Logs]] · [[JSON Web Token]] · [[Kubernetes]]
