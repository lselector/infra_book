---
type: Summary
title: "AWS IAM — security best practices (least privilege)"
description: "To help secure your AWS resources, follow these best practices for AWS Identity and Access Management (IAM)."
resource: "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
source_file: "Raw/05_ops_cicd_security/aws-iam-best-practices.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS IAM — security best practices (least privilege)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-iam-best-practices.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>

## Opening

> To help secure your AWS resources, follow these best practices for AWS Identity and Access Management (IAM).
> + [Require human users to use federation with an identity provider to access AWS using temporary credentials](#bp-users-federation-idp)
> + [Require workloads to use temporary credentials with IAM roles to access AWS](#bp-workloads-use-roles)
> + [Require multi-factor authentication (MFA)](#enable-mfa-for-privileged-users)

## Contents of the source document

- Security best practices in IAM
  - Require workloads to use temporary credentials with IAM roles to access AWS
  - Require multi-factor authentication (MFA)
  - Update access keys when needed for use cases that require long-term credentials
  - Follow best practices to protect your root user credentials
  - Apply least-privilege permissions
  - Get started with AWS managed policies and move toward least-privilege permissions
  - Use IAM Access Analyzer to generate least-privilege policies based on access activity
  - Regularly review and remove unused users, roles, permissions, policies, and credentials
  - Use conditions in IAM policies to further restrict access
  - Verify public and cross-account access to resources with IAM Access Analyzer
  - Establish permissions guardrails across multiple accounts
  - Use permissions boundaries to delegate permissions management within an account

## Related pages

[[AWS CloudTrail]] · [[AWS IAM]] · [[Amazon EC2]] · [[Amazon S3]] · [[Authentication]] · [[JSON Web Token]] · [[Kubernetes]] · [[Least Privilege]] · [[Multi-Factor Authentication]]
