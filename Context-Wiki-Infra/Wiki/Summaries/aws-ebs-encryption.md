---
type: Summary
title: "Amazon EBS encryption — encrypting volumes at rest"
description: "Use Amazon EBS encryption as a straight-forward encryption solution for your Amazon EBS resources associated with your Amazon EC2 instances."
resource: "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html"
source_file: "Raw/05_ops_cicd_security/aws-ebs-encryption.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon EBS encryption — encrypting volumes at rest

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-ebs-encryption.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html>

## Opening

> Use Amazon EBS encryption as a straight-forward encryption solution for your Amazon EBS resources associated with your Amazon EC2 instances. With Amazon EBS encryption, you aren't required to build, maintain, and secure your own key management infrastructure. Amazon EBS encryption uses AWS KMS keys ...
> Encryption operations occur on the servers that host EC2 instances, ensuring the security of both data-at-rest and data-in-transit between an instance and its attached EBS storage.
> You can attach both encrypted and unencrypted volumes to an instance simultaneously. All Amazon EC2 instance types support Amazon EBS encryption.
> + [How Amazon EBS encryption works](how-ebs-encryption-works.md)

## Contents of the source document

- Amazon EBS encryption
  - Encrypt EBS resources
    - Encrypt an empty volume on creation
    - Encrypt unencrypted resources

## Related pages

[[AWS KMS]] · [[Amazon EC2]]
