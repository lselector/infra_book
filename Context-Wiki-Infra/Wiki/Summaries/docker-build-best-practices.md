---
type: Summary
title: "Docker — building best practices for images"
description: "Multi-stage builds let you reduce the size of your final image, by creating a cleaner separation between the building of your image and the final output."
resource: "https://docs.docker.com/build/building/best-practices/"
source_file: "Raw/03_deployments/docker-build-best-practices.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Docker — building best practices for images

Extractive digest of the immutable capture in
`Raw/03_deployments/docker-build-best-practices.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.docker.com/build/building/best-practices/>

## Opening

> Multi-stage builds let you reduce the size of your final image, by creating a
> cleaner separation between the building of your image and the final output.
> Split your Dockerfile instructions into distinct stages to make sure that the
> resulting output only contains the files that are needed to run the application.

## Contents of the source document

- Building best practices
  - Use multi-stage builds
    - Create reusable stages
  - Choose the right base image
  - Rebuild your images often
    - Use --pull to get fresh base images
- syntax=docker/dockerfile:1
    - Use --no-cache for clean builds
  - Exclude with .dockerignore
  - Create ephemeral containers
  - Don't install unnecessary packages
  - Decouple applications
  - Sort multi-line arguments
  - Leverage build cache
  - Pin base image versions
- syntax=docker/dockerfile:1
- syntax=docker/dockerfile:1
  - Build and test your images in CI

## Related pages

[[Cache Busting]] · [[Docker]] · [[GitHub Actions]] · [[Nginx]] · [[Visual Studio Code]]
