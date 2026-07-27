---
type: Summary
title: "Docker Compose — services top-level element reference"
description: "A service is an abstract definition of a computing resource within an application which can be scaled or replaced independently from other components."
resource: "https://docs.docker.com/reference/compose-file/services/"
source_file: "Raw/03_deployments/docker-compose-services-reference.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Docker Compose — services top-level element reference

Extractive digest of the immutable capture in
`Raw/03_deployments/docker-compose-services-reference.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.docker.com/reference/compose-file/services/>

## Opening

> A service is an abstract definition of a computing resource within an application which can be scaled or replaced
> independently from other components. Services are backed by a set of containers, run by the platform
> according to replication requirements and placement constraints. As services are backed by containers, they are defined
> by a Docker image and set of runtime arguments. All containers within a service are identically created with these

## Contents of the source document

- Define services in Docker Compose
  - Examples
    - Simple example
    - Advanced example
  - Attributes
    - annotations
    - attach
    - build
    - blkio_config
    - cpu_count
    - cpu_percent
    - cpu_shares
    - cpu_period
    - cpu_quota
    - cpu_rt_runtime
    - cpu_rt_period
    - cpus
    - cpuset

## Related pages

[[Docker]] · [[Docker Compose]] · [[HTTP]] · [[Load Balancing]] · [[Nginx]] · [[PostgreSQL]] · [[Redis]]
