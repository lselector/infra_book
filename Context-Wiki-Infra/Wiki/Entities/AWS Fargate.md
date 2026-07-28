---
type: Service
title: "AWS Fargate"
description: "Containers on AWS without managing servers - the middle ground between a VPS and a cluster."
wikipedia: "https://en.wikipedia.org/wiki/Amazon_Web_Services"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Fargate

Runs containers on ECS or EKS without you provisioning or
patching the underlying instances. You supply an image and
a task definition.

## Where it fits

Between [[Managed PaaS]] and [[Kubernetes]]. You get
container orchestration, IAM integration and VPC placement
without a node fleet to maintain — which removes the
largest operational burden of running Kubernetes yourself.

## Practical notes

- Task roles give the container AWS credentials with no
  stored secret, which is the [[Least Privilege]] ideal.
- Scales to zero on scheduled tasks; long-running services
  bill continuously.
- Logs go to CloudWatch by default.

## Watch out for

Per-vCPU-second pricing makes steady-state workloads more
expensive than an equivalent [[Amazon EC2]] instance. It
is a convenience premium — worth it for spiky or
low-maintenance workloads, less so for a service that runs
flat out all month.

## Related

[[Containers in Production]] · [[Kubernetes]] ·
[[Docker]] · [[Cost Control]]

## Sources

- [[aws-ecs-fargate]] · [[kubernetes-overview]]
