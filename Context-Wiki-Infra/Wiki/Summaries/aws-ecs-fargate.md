---
type: Summary
title: "AWS Fargate for Amazon ECS"
description: "AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances."
resource: "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html"
source_file: "Raw/03_deployments/aws-ecs-fargate.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Fargate for Amazon ECS

Extractive digest of the immutable capture in
`Raw/03_deployments/aws-ecs-fargate.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html>

## Opening

> AWS Fargate is a technology that you can use with Amazon ECS to run [containers](https://aws.amazon.com/containers/) without having to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run ...
> When you run your tasks and services with Fargate, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate task has its own isolation boundary and does not share the underlying kernel, CPU ...
> Fargate offers platform versions for Amazon Linux 2 (platform version 1.3.0), Bottlerocket operating system (platform version 1.4.0), and Microsoft Windows 2019 Server Full and Core editions.Unless otherwise specified, the information applies to all Fargate platforms.
> For information about the Regions that support Linux containers on Fargate, see [Linux containers on AWS Fargate](AWS_Fargate-Regions.md#linux-regions).

## Contents of the source document

- Architect for AWS Fargate for Amazon ECS
  - Walkthroughs
  - Capacity providers
  - Task definitions
  - Platform versions
  - Service load balancing
  - Usage metrics

## Related pages

[[AWS Fargate]] · [[Amazon EC2]] · [[HTTP]] · [[Load Balancing]]
