---
type: Tool
title: "Docker"
description: "Packaging an app with its dependencies so it runs the same everywhere."
wikipedia: "https://en.wikipedia.org/wiki/Docker_(software)"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Docker

Builds and runs containers: an application plus its
dependencies in an image that behaves identically on a
laptop and a server.

## Why it is worth the effort

- Ends "works on my machine" as a category of problem.
- Makes the runtime version explicit and pinned.
- Is the unit that [[Docker Compose]], [[AWS Fargate]] and
  [[Kubernetes]] all consume, so the work is portable.

## Building images that do not annoy you

- Order Dockerfile layers from least to most frequently
  changing; dependencies before source.
- Use a specific base tag, never `latest`.
- Multi-stage builds so build tools stay out of the
  runtime image.
- Run as a non-root user — [[Least Privilege]] applies
  inside the container too.
- Scan the image with [[Trivy]].

## Watch out for

Secrets baked into an image. They persist in the layer
history even if a later layer removes them — see
[[Secrets Management]].

## Related

[[Docker Compose]] · [[Containers in Production]] ·
[[Kubernetes]] · [[Trivy]]

## Sources

- [[docker-build-best-practices]] ·
  [[docker-compose-overview]]
