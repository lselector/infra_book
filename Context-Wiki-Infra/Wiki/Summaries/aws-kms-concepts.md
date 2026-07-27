---
type: Summary
title: "AWS KMS — concepts: KMS keys, data keys, envelope encryption"
description: "The KMS keys that you create and manage for use in your own cryptographic applications are of a type known as customer managed keys."
resource: "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html"
source_file: "Raw/05_ops_cicd_security/aws-kms-concepts.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS KMS — concepts: KMS keys, data keys, envelope encryption

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-kms-concepts.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>

## Opening

> The KMS keys that you create and manage for use in your own cryptographic applications are of a type known as *customer managed keys*. Customer managed keys can also be used in conjunction with AWS services that use KMS keys to encrypt the data the service stores on your behalf. Customer managed ...
> There are cases where a customer might want an AWS service to encrypt their data, but they don’t want the overhead of managing keys and don’t want to pay for a key. An *AWS managed key* is a KMS key that exists in your account, but can only be used under certain circumstances. Specifically, it can ...
> AWS managed keys are a legacy key type that is no longer being created for new AWS services as of 2021. Instead, new (and legacy) AWS services are using what’s known as an *AWS owned key* to encrypt customer data by default. An AWS owned key is a KMS key that is in an account managed by the AWS ...
> The KMS keys that you create are [customer managed keys](#customer-mgn-key). AWS services that use KMS keys to encrypt your service resources often create keys for you. KMS keys that AWS services create in your AWS account are [AWS managed keys](#aws-managed-key). KMS keys that AWS services create ...

## Contents of the source document

- AWS KMS keys
  - Customer managed keys
  - AWS managed keys
  - AWS owned keys
  - AWS KMS key hierarchy
  - Key identifiers (KeyId)

## Related pages

[[AWS CloudTrail]] · [[AWS KMS]] · [[Amazon S3]] · [[Encryption at Rest]] · [[Envelope Encryption]] · [[HTTP]] · [[Key Rotation]]
