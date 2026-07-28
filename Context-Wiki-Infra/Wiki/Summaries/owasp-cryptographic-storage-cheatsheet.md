---
type: Summary
title: "OWASP — cryptographic storage cheat sheet"
description: "This article provides a simple model to follow when implementing solutions to protect data at rest."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-cryptographic-storage-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — cryptographic storage cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-cryptographic-storage-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html>

## Opening

> This article provides a simple model to follow when implementing solutions to protect data at rest.
> Passwords should not be stored using reversible encryption - secure password hashing algorithms should be used instead. The [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) contains further guidance on storing passwords.
> The first step in designing any application is to consider the overall architecture of the system, as this will have a huge impact on the technical implementation.
> This process should begin with considering the [threat model](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) of the application (i.e, who you are trying to protect that data against).

## Contents of the source document

- Cryptographic Storage Cheat Sheet¶
  - Introduction¶
  - Architectural Design¶
    - Where to Perform Encryption¶
    - Minimise the Storage of Sensitive Information¶
  - Algorithms¶
    - Custom Algorithms¶
    - Cipher Modes¶
    - Random Padding¶
    - Secure Random Number Generation¶
    - Defence in Depth¶
  - Key Management¶
    - Processes¶
    - Key Generation¶
    - Key Lifetimes and Rotation¶
  - Key Storage¶
    - Separation of Keys and Data¶
    - Encrypting Stored Keys¶

## Related pages

[[Authentication]] · [[Azure Key Vault]] · [[Envelope Encryption]] · [[HTTP]] · [[Hardware Security Module]] · [[HashiCorp Vault]] · [[Key Rotation]] · [[Node.js]] · [[OWASP]] · [[Rust]] · [[Secrets Management]]
