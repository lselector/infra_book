---
type: Concept
title: "Docker Build Cache"
description: "Why the second build is fast and the third is not - the cache rules, and how to keep them working in CI."
wikipedia: "https://en.wikipedia.org/wiki/Docker_(software)"
tags: [deployments, tooling, performance]
timestamp: "2026-07-28T00:00:00Z"
---

# Docker Build Cache

Docker caches the result of each `Dockerfile`
instruction. On a rebuild it reuses a cached layer when
the instruction and its inputs are unchanged — and
**invalidates that layer and every layer after it** when
they are not.

That cascade is the whole subject. One badly placed line
turns a 5-second rebuild into a 4-minute one, on every
push, forever.

## The invalidation rules

| Instruction | Cache breaks when |
|---|---|
| `RUN cmd` | the command string changes |
| `COPY` / `ADD` | the copied files' contents change |
| `FROM image:tag` | the resolved base image changes |
| `ARG` used in a layer | the value changes |
| anything after an invalidated layer | always |

Note what is *not* on the list: time. `RUN apt-get
update` will happily reuse a six-month-old package index
because the string did not change.

## The one rule that matters

**Copy dependency manifests, install, then copy source.**

```dockerfile
COPY requirements.txt .          # changes rarely
RUN pip install -r requirements.txt
COPY . .                         # changes every commit
```

Reversed — `COPY . .` before the install — every commit
invalidates the install layer and reinstalls every
dependency. This is the most common Dockerfile mistake
and the most expensive.

The same shape applies everywhere: `package.json` +
`package-lock.json` before `npm ci`; `Cargo.toml` +
`Cargo.lock` before `cargo build`; `pyproject.toml` +
`uv.lock` before `uv sync` ([[uv]]).

## `.dockerignore` is part of the cache

`COPY . .` hashes the build context. If `.git`,
`node_modules` or a log file is in it, the hash changes
when they change, and the layer rebuilds for reasons
unrelated to your code. Excluding them makes the cache
*stable*, not just the image small
([[Container Images]]).

## Keeping the cache in CI

A CI runner is a fresh machine with no cache, so a naive
pipeline gets no reuse at all and every build is a cold
one ([[Continuous Integration and Delivery]]).
[[BuildKit]] exports and imports the cache to fix this:

```yaml
- uses: docker/build-push-action@v6
  with:
    push: true
    tags: ghcr.io/me/app:${{ github.sha }}
    cache-from: type=gha           # read last build's cache
    cache-to: type=gha,mode=max    # write this build's
```

`type=gha` uses GitHub's cache; `type=registry` pushes
cache layers to a registry, which works anywhere.
`mode=max` caches intermediate stages too — important
with multi-stage builds, where only the final stage is
cached otherwise.

**Cache mounts** are the other half: they persist package
manager caches *between* builds without ever entering the
image.

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

## When to bypass it

`--no-cache` for release builds if you want fresh base
packages, and `--pull` to re-resolve the base tag. A
cached `apt-get update` from months ago is a real supply
of stale, vulnerable packages — rebuild without cache
periodically and re-scan with [[Trivy]].

## Watch out for

- **Cache is per-machine unless exported.** Your laptop's
  fast build says nothing about CI.
- **Multi-architecture builds** (arm64 + amd64) keep
  separate caches; expect the first of each to be slow.
- **A cache is not a lockfile.** Reproducibility comes
  from pinned dependencies and pinned base digests, not
  from the cache happening to hold an old layer.
- **Do not cache secrets.** `--mount=type=secret` exists
  precisely so a token used during build never lands in a
  layer ([[Secrets Management]]).

## Related

[[Container Images]] · [[BuildKit]] · [[Docker]] ·
[[Docker Compose]] ·
[[Continuous Integration and Delivery]] ·
[[GitHub Actions]] · [[Caching]] · [[Cache Busting]] ·
[[Trivy]] · [[Secrets Management]] · [[uv]]

## Sources

- [[docker-build-best-practices]] ·
  [[docker-compose-overview]] ·
  [[github-actions-workflow-syntax]] ·
  [[github-actions-understanding]] · [[trivy-overview]]
