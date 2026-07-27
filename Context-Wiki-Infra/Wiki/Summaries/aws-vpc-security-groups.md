---
type: Summary
title: "Amazon VPC — security groups"
description: "A security group controls the traffic that is allowed to reach and leave the resources that it is associated with."
resource: "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"
source_file: "Raw/04_network_storage_db/aws-vpc-security-groups.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon VPC — security groups

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/aws-vpc-security-groups.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html>

## Opening

> A *security group* controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.
> When you create a VPC, it comes with a default security group. You can create additional security groups for a VPC, each with their own inbound and outbound rules. You can specify the source, port range, and protocol for each inbound rule. You can specify the destination, port range, and protocol ...
> The following diagram shows a VPC with a subnet, an internet gateway, and a security group. The subnet contains an EC2 instance. The security group is assigned to the instance. The security group acts as a virtual firewall. The only traffic that reaches the instance is the traffic allowed by the ...
> ![VPC with 2 subnets, 2 security groups, servers in subnets associated with different security groups](http://docs.aws.amazon.com/vpc/latest/userguide/images/security-group-overview.png)

## Contents of the source document

- Control traffic to your AWS resources using security groups
  - Security group basics
  - Security group example

## Related pages

[[Amazon EC2]] · [[Amazon VPC]] · [[HTTP]]
