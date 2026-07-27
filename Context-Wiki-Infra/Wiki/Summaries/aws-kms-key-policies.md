---
type: Summary
title: "AWS KMS — key policies and access control"
description: "A key policy is a resource policy for an AWS KMS key."
resource: "https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html"
source_file: "Raw/05_ops_cicd_security/aws-kms-key-policies.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS KMS — key policies and access control

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-kms-key-policies.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>

## Opening

> A key policy is a resource policy for an AWS KMS key. Key policies are the primary way to control access to KMS keys. Every KMS key must have exactly one key policy. The statements in the key policy determine who has permission to use the KMS key and how they can use it. You can also use [IAM ...
> No AWS principal, including the account root user or key creator, has any permissions to a KMS key unless they are explicitly allowed, and never denied, in a key policy, IAM policy, or grant.
> Unless the key policy explicitly allows it, you cannot use IAM policies to *allow* access to a KMS key. Without permission from the key policy, IAM policies that allow permissions have no effect. (You can use an IAM policy to *deny* a permission to a KMS key without permission from a key policy.) ...
> Unlike IAM policies, which are global, key policies are Regional. A key policy controls access only to a KMS key in the same Region. It has no effect on KMS keys in other Regions.

## Contents of the source document

- Key policies in AWS KMS

## Related pages

[[AWS KMS]]
