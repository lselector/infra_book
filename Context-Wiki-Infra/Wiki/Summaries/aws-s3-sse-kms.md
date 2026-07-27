---
type: Summary
title: "Amazon S3 — server-side encryption with KMS keys (SSE-KMS)"
description: "Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3."
resource: "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html"
source_file: "Raw/05_ops_cicd_security/aws-s3-sse-kms.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon S3 — server-side encryption with KMS keys (SSE-KMS)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-s3-sse-kms.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html>

## Opening

> Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The ...
> Server-side encryption is the encryption of data at its destination by the application or service that receives it.
> Amazon S3 automatically enables server-side encryption with Amazon S3 managed keys (SSE-S3) for new object uploads.
> Unless you specify otherwise, buckets use SSE-S3 by default to encrypt objects. However, you can choose to configure buckets to use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) instead. For more information, see [Specifying server-side encryption with AWS KMS ...

## Contents of the source document

- Using server-side encryption with AWS KMS keys (SSE-KMS)
  - AWS KMS keys
    - Using SSE-KMS encryption for cross-account operations
    - SSE-KMS encryption workflow
    - Auditing SSE-KMS encryption
  - Amazon S3 Bucket Keys
  - Requiring server-side encryption
  - Encryption context
  - Sending requests for AWS KMS encrypted objects

## Related pages

[[AWS CloudTrail]] · [[AWS KMS]] · [[Amazon S3]] · [[Authentication]] · [[Authorization]] · [[Envelope Encryption]] · [[HTTP]] · [[Shared Responsibility Model]]
