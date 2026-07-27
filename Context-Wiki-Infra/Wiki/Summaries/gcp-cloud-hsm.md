---
type: Summary
title: "Google Cloud HSM — FIPS 140-2 Level 3 hardware-backed keys"
description: "This document provides an overview of Cloud HSM and shows you how to create and use HSM-protected encryption keys in Cloud Key Management Service."
resource: "https://cloud.google.com/kms/docs/hsm"
source_file: "Raw/05_ops_cicd_security/gcp-cloud-hsm.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Google Cloud HSM — FIPS 140-2 Level 3 hardware-backed keys

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/gcp-cloud-hsm.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cloud.google.com/kms/docs/hsm>

## Opening

> This document provides an overview of Cloud HSM and shows you how to create and use HSM-protected encryption keys in Cloud Key Management Service.
> Cloud HSM is a cloud-hosted Hardware Security Module (HSM) service that lets you host encryption keys and perform cryptographic operations in a cluster of [FIPS 140-2 Level 3](https://csrc.nist.gov/publications/detail/fips/140/2/final) certified HSMs. Google manages the HSM cluster for you, so you ...
> When you create a key, you add it to a key ring in a given Google Cloud location. You can create a new key ring or use an existing one. In this topic, you create a new key ring and add a new key to it.
> Create a key ring in a Google Cloud [location](https://cloud.google.com/kms/docs/locations) that supports Cloud HSM.

## Contents of the source document

  - What is Cloud HSM?
  - Create a key ring
    - Console
    - gcloud
    - C#
    - Go
    - Java
    - Node.js
    - PHP
    - Python
    - Ruby
    - API
  - Create a key
    - Console
    - gcloud
    - C#
    - Go
    - Java

## Related pages

[[Authorization]] · [[Encryption at Rest]] · [[HTTP]] · [[Hardware Security Module]] · [[Key Rotation]]
