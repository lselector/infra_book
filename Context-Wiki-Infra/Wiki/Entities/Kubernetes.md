---
type: Tool
title: "Kubernetes"
description: "Container orchestration at cluster scale - and a clear-eyed account of when you do not need it."
wikipedia: "https://en.wikipedia.org/wiki/Kubernetes"
tags: [deployments, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Kubernetes

Schedules containers across a fleet of machines, handling
placement, restarts, rolling updates, service discovery
and horizontal scaling.

## What it genuinely solves

Running many services across many machines, with
self-healing and declarative desired state, in an
organisation large enough to have people who operate it.

## Why it is usually wrong here

The cost is not the control plane fee; it is the concept
count. Pods, deployments, services, ingresses,
configmaps, secrets, persistent volume claims, RBAC —
every one is something to learn, debug and get wrong,
before you have shipped a feature.

A [[Monolithic Web App]] on [[One-Box Deployment]] behind
a [[Content Delivery Network]] serves an enormous amount
of traffic. When it stops being enough, [[Managed PaaS]]
or [[AWS Fargate]] cover most of the remaining ground.

## The honest signals that you need it

- Many services, many teams, needing independent
  deployment.
- Genuine bin-packing economics across a large fleet.
- An organisational standard you cannot opt out of.

"We might scale" is not on the list. See
[[Anti-Patterns]].

## Related

[[Containers in Production]] · [[Docker]] ·
[[AWS Fargate]] · [[Anti-Patterns]] · [[Managed PaaS]]

## Sources

- [[kubernetes-overview]] · [[aws-ecs-fargate]] ·
  [[martinfowler-microservice-premium]]
