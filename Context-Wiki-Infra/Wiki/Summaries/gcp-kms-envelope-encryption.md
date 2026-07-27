---
type: Summary
title: "Google Cloud KMS — envelope encryption explained"
description: "Storing and encrypting data at Google's scale requires using a central cryptographic key management service with multiple layers of keys for the encrypted data."
resource: "https://cloud.google.com/kms/docs/envelope-encryption"
source_file: "Raw/05_ops_cicd_security/gcp-kms-envelope-encryption.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud KMS — envelope encryption explained

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-kms-envelope-encryption.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/kms/docs/envelope-encryption>

## Opening

> Storing and encrypting data at Google's scale requires using a central cryptographic key management service with multiple layers of keys for the encrypted data. An example of multiple layer of keys is _envelope encryption_ , which is the process of encrypting a key with another key.
> You can encrypt data at both the _application layer_ , which is responsible for displaying data to users, and the _storage layer_ , which provides the physical storage of data.
> By default, at the storage layer, Google Cloud [encrypts customer content stored at rest](https://cloud.google.com/docs/security/encryption/default-encryption) using envelope encryption, with Google's internal key management service as the central keystore. If you're storing and encrypting data ...
> Cloud KMS stores keys in a _key hierarchy_ designed for ease, with access to resources in the key hierarchy governed by [Identity and Access Management](https://cloud.google.com/kms/docs/iam). The following shows the main levels of a Cloud KMS key hierarchy:

## Contents of the source document

  - Introduction
    - Data encryption keys
    - Key encryption keys
  - Balancing DEKs and KEKs
  - How to encrypt data using envelope encryption
  - How to decrypt data using envelope encryption
  - Integration with Google Cloud services
  - Other options for Google Cloud services

## Related pages

[[Envelope Encryption]] · [[Google Cloud KMS]] · [[Key Rotation]]
