---
type: Summary
title: "AWS KMS — developer guide overview"
description: "AWS Key Management Service (AWS KMS) is an AWS managed service that makes it easy for you to create and control the keys used to encrypt and sign your data."
resource: "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"
source_file: "Raw/05_ops_cicd_security/aws-kms-overview.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS KMS — developer guide overview

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-kms-overview.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/kms/latest/developerguide/overview.html>

## Opening

> AWS Key Management Service (AWS KMS) is an AWS managed service that makes it easy for you to create and control the keys used to encrypt and sign your data. The AWS KMS keys that you create in AWS KMS are protected by [FIPS 140-3 Security Level 3 validated hardware security modules ...
> When you encrypt data, you need to protect your encryption key. If you encrypt your key, you need to protect its encryption key. Eventually, you must protect the highest level encryption key (known as a *root key*) in the hierarchy that protects your data. That's where AWS KMS comes in.
> ![Root key protect the data keys that protect your data](http://docs.aws.amazon.com/kms/latest/developerguide/images/key-hierarchy-root.png)
> AWS KMS protects your root keys. KMS keys are created, managed, used, and deleted entirely within AWS KMS. They never leave the service unencrypted. To use or manage your KMS keys, you call AWS KMS.

## Contents of the source document

- AWS Key Management Service
  - Why use AWS KMS?
  - AWS KMS in AWS Regions
  - AWS KMS pricing
  - AWS KMS service level agreement

## Related pages

[[AWS KMS]] · [[HTTP]]
