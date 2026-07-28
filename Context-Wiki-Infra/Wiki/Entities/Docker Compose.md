---
type: Tool
title: "Docker Compose"
description: "Several containers defined in one file - the practical way to run containers on a single box."
wikipedia: "https://en.wikipedia.org/wiki/Docker_(software)"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Docker Compose

Describes a multi-container application in one
`compose.yaml` and runs it with a single command.

## The shape on a small deployment

```yaml
services:
  app:
    build: .
    env_file: .env
    restart: unless-stopped
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
    restart: unless-stopped
volumes:
  pgdata:
```

Started by [[systemd]] on boot, fronted by [[Caddy]].

## Why it is enough

It gives reproducible builds, isolated dependencies and a
one-file description of the whole stack. What it does not
give — rescheduling onto another machine — is irrelevant
when there is one machine. See
[[Containers in Production]].

## Watch out for

- `docker compose down -v` deletes named volumes. That is
  your database.
- Compose can publish ports past [[UFW]]; verify what is
  actually listening.
- Back up the volume from the host, or better, `pg_dump`
  from inside — see [[Database Backups]].
- Compose has native `secrets` support; prefer it to
  passing credentials as environment variables.

## Related

[[Docker]] · [[Containers in Production]] ·
[[One-Box Deployment]] · [[Secrets Management]]

## Sources

- [[docker-compose-overview]] ·
  [[docker-compose-production]] ·
  [[docker-compose-services-reference]] ·
  [[docker-compose-secrets]]
