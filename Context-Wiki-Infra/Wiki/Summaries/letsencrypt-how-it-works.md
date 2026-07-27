---
type: Summary
title: "Let's Encrypt — how it works (ACME)"
description: "Last updated: August 2, 2025 The objective of Let’s Encrypt and the ACME protocol is to make it possible to set up an HTTPS server and have it automatically obtain browser-trusted certificat"
resource: "https://letsencrypt.org/how-it-works/"
source_file: "Raw/03_deployments/letsencrypt-how-it-works.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Let's Encrypt — how it works (ACME)

Extractive digest of the immutable capture in
`Raw/03_deployments/letsencrypt-how-it-works.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://letsencrypt.org/how-it-works/>

## Opening

> Last updated: August 2, 2025
> The objective of Let’s Encrypt and the [ACME protocol](https://tools.ietf.org/html/rfc8555) is to make it possible to set up an HTTPS server and have it automatically obtain browser-trusted certificates without any human intervention. This is accomplished by running an ACME client on a web server.
> To understand how the technology works, let’s walk through the process of setting up `https://example.com/` with an ACME client.
> There are two steps to this process. First, the ACME client proves to the [Certificate Authority](https://wikipedia.org/wiki/Certificate_authority) (CA) that the web server controls a domain. After that the client can request or revoke certificates for that domain.

## Contents of the source document

- How It Works
  - Domain Validation
  - Certificate Issuance and Revocation
    - Issuance
    - Revocation

## Related pages

[[ACME Protocol]] · [[HTTP]] · [[Let's Encrypt]]
