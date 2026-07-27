---
type: Summary
title: "OWASP — logging cheat sheet (what to log, what never to log)"
description: "This cheat sheet is focused on providing developers with concentrated guidance on building application logging mechanisms, especially related to security logging."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-logging-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — logging cheat sheet (what to log, what never to log)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-logging-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>

## Opening

> This cheat sheet is focused on providing developers with concentrated guidance on building application logging mechanisms, especially related to security logging.
> Many systems enable network device, operating system, web server, mail server and database server logging, but often custom application event logging is missing, disabled or poorly configured. It provides much greater insight than infrastructure logging alone. Web application (e.g. web site or web ...
> Application logging should be consistent within the application, consistent across an organization's application portfolio and use industry standards where relevant, so the logged event data can be consumed, correlated, analyzed and managed by a wide variety of systems.
> Application logging should always be included for security events. Application logs are invaluable data for both security and operational use cases.

## Contents of the source document

- Logging Cheat Sheet¶
  - Introduction¶
  - Purpose¶
    - Operational use cases¶
    - Security use cases¶
  - Design, implementation, and testing¶
    - Event data sources¶
    - Where to record event data¶
    - Which events to log¶
    - Event attributes¶
    - Data to exclude¶
    - Customizable logging¶
    - Event collection¶
    - Verification¶
    - Network architecture¶
  - Deployment and operation¶
    - Release¶
    - Operation¶

## Related pages

[[Authentication]] · [[Authorization]] · [[HTTP]] · [[Incident Response]] · [[OWASP]]
