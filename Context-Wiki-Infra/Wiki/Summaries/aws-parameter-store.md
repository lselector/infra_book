---
type: Summary
title: "AWS Systems Manager Parameter Store — cheap config and secret storage"
description: "• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026."
resource: "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html"
source_file: "Raw/05_ops_cicd_security/aws-parameter-store.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Systems Manager Parameter Store — cheap config and secret storage

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-parameter-store.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html>

## Opening

> • The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard ...
> Parameter Store is a centralized configuration data store for named values called parameters. A *parameter* is any piece of data stored in Parameter Store, such as a block of text, a list of names, an AMI ID, a license key, and so on. With Parameter Store, you can securely store, organize, and ...
> Parameter Store simplifies configuration management across environments. You can standardize how applications access critical data at runtime without hardcoding values or relying on fragmented storage solutions. In this way, you maintain consistency, enforce governance, and build more secure and ...
> Parameter Store supports the following parameter types:

## Contents of the source document

- AWS Systems Manager Parameter Store
  - Where should I store my application data?
  - Parameter Store features
  - Parameter tiers in Parameter Store

## Related pages

[[AWS Fargate]] · [[AWS KMS]] · [[AWS Secrets Manager]] · [[AWS Systems Manager Parameter Store]] · [[Amazon EC2]] · [[Encryption at Rest]] · [[HTTP]]
