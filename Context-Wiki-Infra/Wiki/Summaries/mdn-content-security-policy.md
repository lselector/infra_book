---
type: Summary
title: "Content Security Policy (CSP) (MDN)"
description: "The primary use case for CSP is to control which resources, in particular JavaScript resources, a document is allowed to load."
resource: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP"
source_file: "Raw/05_ops_cicd_security/mdn-content-security-policy.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Content Security Policy (CSP) (MDN)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/mdn-content-security-policy.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP>

## Opening

> The primary use case for CSP is to control which resources, in particular JavaScript resources, a document is allowed to load. This is mainly used as a defense against [cross-site scripting](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) (XSS) attacks, in which an attacker ...
> A CSP can have other purposes as well, including defending against [clickjacking](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Clickjacking) and helping to ensure that a site's pages will be loaded over HTTPS.
> In this guide we'll start by describing how a CSP is delivered to a browser and what it looks like at a high level.
> Then we'll describe how it can be used to:

## Contents of the source document

- Content Security Policy (CSP)
  - CSP overview
  - Controlling resource loading
    - XSS and resource loading
    - Fetch directives
    - Strict CSP
  - Clickjacking protection
  - Upgrading insecure requests
  - Requiring trusted types
    - Injection sinks and sanitization
    - The Trusted Types API
  - Testing your policy
    - Violation reporting
  - See also
  - Help improve MDN

## Related pages

[[HTTP]] · [[OWASP]]
