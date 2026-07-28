---
type: Concept
title: "Containers in Production"
description: "Docker Compose on one box - most of the benefit of containers, almost none of the orchestration cost."
wikipedia: "https://en.wikipedia.org/wiki/OS-level_virtualization"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Containers in Production

Containers package the app with its dependencies so it
runs the same everywhere. That is worth having. A cluster
to schedule them usually is not.

## The pragmatic middle

[[Docker Compose]] on a single VPS: one `compose.yaml`
describing the app, the database and the proxy, started
with one command and restarted by [[systemd]] on boot.
You get reproducible builds and clean dependency isolation
without a control plane.

## Why it matters here

- Solves "works on my laptop" honestly.
- Makes [[Deployment Environments]] cheap — the same
  compose file with a different env file.
- Keeps the door open to [[AWS Fargate]] or [[Kubernetes]]
  later without a rewrite.

## Watch out for

- Compose is not a scheduler. It will not reschedule onto
  another machine, because there is no other machine.
- Persist databases on named volumes and back them up from
  the host — a `docker compose down -v` is a data-loss
  event.
- Image size and build caching; a naive Dockerfile
  rebuilds everything on every deploy.

## Related

[[Docker]] · [[Docker Compose]] · [[Kubernetes]] ·
[[One-Box Deployment]] · [[Deployment Environments]] ·
[[Container Images]] · [[Docker Build Cache]] ·
[[BuildKit]] · [[Deployment Strategies]] · [[Micro-VMs]]

## Sources

- [[docker-compose-overview]] ·
  [[docker-compose-production]] ·
  [[docker-build-best-practices]] ·
  [[docker-compose-services-reference]]
