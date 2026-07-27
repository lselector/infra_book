---
type: Summary
title: "AWS Secrets Manager — what it is and when to use it"
description: "AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles."
resource: "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"
source_file: "Raw/05_ops_cicd_security/aws-secrets-manager-intro.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Secrets Manager — what it is and when to use it

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-secrets-manager-intro.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>

## Opening

> AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles. Many AWS services store and use secrets in Secrets Manager.
> Secrets Manager helps you improve your security posture, because you no longer need hard-coded credentials in application source code. Storing the credentials in Secrets Manager helps avoid possible compromise by anyone who can inspect your application or the components. You replace hard-coded ...
> With Secrets Manager, you can configure an automatic rotation schedule for your secrets. This enables you to replace long-term secrets with short-term ones, significantly reducing the risk of compromise. Since the credentials are no longer stored with the application, rotating credentials no longer ...
> For other types of secrets you might have in your organization:

## Contents of the source document

- What is AWS Secrets Manager?
  - Get started with Secrets Manager
  - Compliance with standards
  - Pricing

## Related pages

[[AWS CloudTrail]] · [[AWS KMS]] · [[AWS Lambda]] · [[AWS Secrets Manager]] · [[Amazon EC2]] · [[Amazon S3]]
