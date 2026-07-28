---
type: Concept
title: "Container Images"
description: "What a Dockerfile actually produces - layers, multi-stage builds, and the small number of lines that matter."
wikipedia: "https://en.wikipedia.org/wiki/OS-level_virtualization"
tags: [deployments, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Container Images

An image is a stack of read-only **layers** plus a
manifest saying how to run them. Each instruction in a
`Dockerfile` that changes the filesystem creates one
layer; containers add a thin writable layer on top at
run time.

Understanding that one sentence explains image size,
build speed, cache behaviour ([[Docker Build Cache]]) and
the most common security mistake in one go.

## A Dockerfile worth copying

```dockerfile
# ---- build stage ----
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt .                 # deps first...
RUN pip install --no-cache-dir -r requirements.txt
COPY . .                                # ...source last

# ---- runtime stage ----
FROM python:3.12-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.12/site-packages \
                  /usr/local/lib/python3.12/site-packages
COPY --from=build /app /app
RUN useradd -m app
USER app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Five decisions are doing all the work:

1. **Dependencies copied before source.** Source changes
   every commit; dependencies change monthly. Ordering
   layers least-changing-first is the single biggest
   build-time win.
2. **A specific base tag**, never `latest` — otherwise
   the build is not reproducible and one day quietly
   changes major version. Pinning by digest
   (`python:3.12-slim@sha256:...`) is stronger still.
3. **Multi-stage.** Compilers, headers and build caches
   stay in the build stage; the runtime image contains
   only what runs. Often a 5–10× size difference, and a
   smaller attack surface.
4. **A non-root `USER`.** Root in a container is root on
   the kernel it shares ([[Least Privilege]]).
5. **`CMD` in exec form** (a JSON array), so the process
   is PID 1 and receives `SIGTERM` — shell form spawns a
   shell that swallows the signal and your container
   takes ten seconds to stop on every deploy.

## `.dockerignore` earns its place immediately

```text
.git
.venv
node_modules
*.env
__pycache__
```

Without it, `COPY . .` ships your git history, your
virtualenv and possibly your `.env`. It makes the build
context smaller (faster), the image smaller, and the
secret leak less likely — one file, three benefits.

## Tags and digests

A tag is a mutable pointer; `myapp:v1.2.3` can be moved
to different content tomorrow. For deployments, resolve
to the **digest** (`myapp@sha256:…`) so that what you
tested is what runs, and so a rollback names an exact
artifact ([[Deployment Strategies]]).

## Watch out for

- **Secrets in layers persist.** A `RUN` that fetches
  with a token, or a `COPY .env`, stays in the layer
  history even if a later layer deletes the file. Anyone
  who can pull the image can recover it. Use build
  secrets ([[BuildKit]]) or runtime environment
  variables — see [[Secrets Management]].
- **`apt-get update` in its own layer** goes stale
  against a cached install layer; keep update and install
  in one `RUN`.
- **Scan before shipping.** [[Trivy]] on the built image
  reports the vulnerable OS packages you inherited from
  the base ([[Dependency Auditing]]).
- **Image size affects [[Cold Starts]]** on platforms
  that pull per instance ([[Google Cloud Run]],
  [[AWS Fargate]]).

## Related

[[Docker]] · [[Docker Build Cache]] · [[BuildKit]] ·
[[Docker Compose]] · [[Containers in Production]] ·
[[Container Orchestration]] · [[Trivy]] ·
[[Secrets Management]] · [[Least Privilege]] ·
[[Deployment Strategies]] ·
[[Continuous Integration and Delivery]] ·
[[Google Cloud Run]] · [[Cold Starts]]

## Sources

- [[docker-build-best-practices]] ·
  [[docker-compose-overview]] ·
  [[docker-compose-production]] · [[trivy-overview]] ·
  [[aws-ecs-fargate]]
