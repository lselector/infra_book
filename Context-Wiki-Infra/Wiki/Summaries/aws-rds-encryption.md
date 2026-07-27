---
type: Summary
title: "Amazon RDS — encrypting database resources at rest"
description: "Amazon RDS can encrypt your Amazon RDS DB instances."
resource: "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html"
source_file: "Raw/05_ops_cicd_security/aws-rds-encryption.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon RDS — encrypting database resources at rest

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/aws-rds-encryption.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

## Opening

> Amazon RDS can encrypt your Amazon RDS DB instances. Data that is encrypted at rest includes the underlying storage for DB instances, its logs, automated backups, read replicas, and snapshots.
> Amazon RDS encrypted DB instances use the industry standard AES-256 encryption algorithm to encrypt your data on the server that hosts your Amazon RDS DB instances.
> After your data is encrypted, Amazon RDS handles authentication of access and decryption of your data transparently with a minimal impact on performance. You don't need to modify your database client applications to use encryption.
> For encrypted and unencrypted DB instances, data that is in transit between the source and the read replicas is encrypted, even when replicating across AWS Regions.

## Contents of the source document

- Encrypting Amazon RDS resources
  - Overview of encrypting Amazon RDS resources
  - Encrypting a DB instance
  - Determining whether encryption is turned on for a DB instance
    - Console
    - AWS CLI
    - RDS API
  - Availability of Amazon RDS encryption
  - Encryption in transit
  - Limitations of Amazon RDS encrypted DB instances

## Related pages

[[AWS KMS]] · [[Amazon RDS]] · [[Amazon S3]] · [[Amazon VPC]] · [[Authentication]] · [[Encryption at Rest]] · [[Encryption in Transit]] · [[Envelope Encryption]] · [[HTTP]] · [[Read Replicas]]
