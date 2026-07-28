---
type: Service
title: "Amazon EC2"
description: "AWS virtual machines - the IaaS baseline, worth it mainly when you are already in AWS."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon EC2

Virtual servers in AWS, in every size from burstable
micro instances upward.

## When it is the right call

- You already use [[Amazon S3]], [[AWS KMS]] or
  [[Amazon SES]] and want everything under one IAM model.
- You need a specific region or compliance posture.
- You want instance roles so the app gets credentials
  without a stored secret — a real
  [[Secrets Management]] advantage.

## When it is not

Purely as a cheap box. A comparable [[Hetzner Cloud]] or
[[DigitalOcean]] instance costs less and involves far less
surrounding configuration.

## Watch out for

- Egress charges, which do not exist in the same way at
  the VPS providers.
- Attached EBS volumes and Elastic IPs continue to bill
  after the instance is stopped.
- Encrypt the EBS volume at creation — see
  [[Encryption at Rest]]; it cannot be done in place
  later.

## Related

[[One-Box Deployment]] · [[VPC and Security Groups]] ·
[[Cost Control]] · [[Cloud Service Models]]

## Sources

- [[aws-ec2-get-started]] · [[aws-ebs-encryption]] ·
  [[aws-what-is-vpc]]
