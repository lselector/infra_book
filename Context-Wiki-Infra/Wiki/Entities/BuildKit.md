---
type: Tool
title: "BuildKit"
description: "Docker's build engine - parallel stages, cache mounts, build secrets, and multi-architecture images."
wikipedia: "https://en.wikipedia.org/wiki/Docker_(software)"
tags: [deployments, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# BuildKit

The build engine behind `docker build` since Docker
23.0 — you are almost certainly using it already,
without having enabled anything. It replaced a builder
that executed a `Dockerfile` strictly top to bottom.

## What it changed

- **A dependency graph instead of a sequence.**
  Independent stages of a multi-stage build run in
  parallel, and stages whose output is never used are
  skipped entirely.
- **Cache import/export**, so a CI runner can reuse the
  previous build's layers — see [[Docker Build Cache]].
- **Cache mounts**: a directory that persists across
  builds and never becomes part of the image.
- **Build secrets**: a file available during one `RUN`
  and absent from every layer afterwards.
- **Multi-platform builds** (`--platform
  linux/amd64,linux/arm64`) from one machine, which
  matters when you develop on an Apple Silicon laptop and
  deploy to x86 servers.

## The two features worth adopting today

**Secrets that do not end up in the image** — the fix for
the most common way credentials leak from a build
([[Secrets Management]]):

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci
```

```bash
docker build --secret id=npmrc,src=$HOME/.npmrc .
```

**Cache mounts** for package managers, which cut rebuild
time without growing the image:

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

Both need the frontend declared at the top of the file
if you target older Docker:
`# syntax=docker/dockerfile:1`.

## `docker buildx`

The CLI front end to BuildKit: named builders, remote
builders, multi-platform output, and the `cache-from` /
`cache-to` flags used in CI pipelines. In
[[GitHub Actions]], `docker/build-push-action` wraps all
of it.

## Watch out for

- **`--secret` is not `ARG`.** A build argument is
  visible in `docker history`; a build secret is not.
  Never pass credentials as `ARG`.
- **Emulated cross-architecture builds are slow.**
  Building arm64 on x86 through QEMU can be 5–10×
  slower — use native runners for both where it matters.
- **Cache export needs configuring per CI provider**, and
  an unbounded cache costs storage. `mode=max` caches
  more and stores more.

## Related

[[Docker]] · [[Container Images]] ·
[[Docker Build Cache]] · [[Docker Compose]] ·
[[GitHub Actions]] ·
[[Continuous Integration and Delivery]] ·
[[Secrets Management]] · [[Trivy]] ·
[[Containers in Production]]

## Sources

- [[docker-build-best-practices]] ·
  [[docker-compose-overview]] ·
  [[github-actions-workflow-syntax]]. Upstream
  documentation (<https://docs.docker.com/build/>) is
  cited through the Docker captures above.
