---
type: Service
title: "Amazon VPC"
description: "Your private network in AWS - subnets, routing and security groups."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud"
tags: [storage-and-databases, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon VPC

An isolated virtual network in which your AWS resources
live, with your own address range, subnets and routing.

## The minimum useful model

- **Public subnet** for anything with a public IP.
- **Private subnet** for databases and internal workers.
- **Security groups** as stateful, instance-level
  firewalls, referencing each other by group rather than
  by IP.
- **Network ACLs** as a coarse subnet-level backstop.

## Why it matters here

It is the AWS expression of the same idea as binding to
`127.0.0.1` and running [[UFW]] on a single box. The
principle — nothing is reachable unless deliberately
opened — is identical; only the machinery is larger.

## Watch out for

- NAT gateways bill hourly plus per GB and surprise people
  regularly.
- `0.0.0.0/0` on a database port. This is the recurring
  cause of exposed databases.

## Related

[[VPC and Security Groups]] · [[Amazon EC2]] · [[UFW]] ·
[[Least Privilege]] · [[Cost Control]]

## Sources

- [[aws-what-is-vpc]] · [[aws-vpc-security-groups]] ·
  [[aws-vpc-subnets]]
