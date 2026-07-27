---
type: Summary
title: "Google Cloud — default encryption at rest"
description: "This content was last updated in May 2024 and represents the status quo as of the time that it was written."
resource: "https://cloud.google.com/docs/security/encryption/default-encryption"
source_file: "Raw/05_ops_cicd_security/gcp-encryption-at-rest.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud — default encryption at rest

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-encryption-at-rest.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/docs/security/encryption/default-encryption>

## Opening

> _This content was last updated in May 2024 and represents the status quo as of the time that it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._
> At Google, our comprehensive security strategy includes encryption at rest, which helps to protect customer data from attackers. We encrypt all Google customer content at rest, without any action required by you, using one or more encryption mechanisms. This document describes our approach to ...
> This document is for security architects and security teams who are currently using or considering Google. This document assumes a basic understanding of [encryption](https://wikipedia.org/wiki/Encryption) and [cryptographic primitives](https://wikipedia.org/wiki/Cryptographic_primitive). For more ...
> Encryption at rest is encryption that is used to help protect data that is stored on a disk (including solid-state drives) or backup media. All data that is stored by Google is encrypted at the storage layer using the Advanced Encryption Standard (AES) algorithm, AES-256. We use a common ...

## Contents of the source document

  - Keys in Google Cloud
  - How encryption at rest helps to secure data
  - What is customer data?
  - Default encryption of data at rest
    - Layers of encryption
    - Encryption at the infrastructure layer
    - Encryption at the storage device layer
    - Encryption of backups
    - FIPS compliance for data at rest
  - Key management
    - Generating DEKs
    - Generating KEKs
    - KEK management
    - Process for accessing encrypted chunks of data
    - Encryption key hierarchy and root of trust
    - Summary of key management
    - Global availability and replication
  - Google's common cryptographic library

## Related pages

[[Authentication]] · [[Authorization]] · [[Encryption at Rest]] · [[Envelope Encryption]] · [[Key Rotation]]
