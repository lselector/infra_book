---
type: Tool
title: "Kamal"
description: "Zero-downtime container deploys onto plain Linux boxes over SSH - Capistrano for containers, from Basecamp."
website: "https://kamal-deploy.org/"
tags: [deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# Kamal

A deploy tool that takes a list of IP addresses and a
[[Docker]] image and gives you zero-downtime rolling
deploys, with nothing installed on the servers beyond
Docker itself. Built at 37signals to move their apps off
the cloud, MIT licensed.

## Why it appears here

It is the piece that makes [[VPS Instead of Hyperscaler]]
practical for containerized apps. Deploy ergonomics that
previously required [[Managed PaaS]] or [[Kubernetes]],
applied to a vanilla Ubuntu box that has seen no
preparation beyond an added SSH key.

Originally written for Rails, but it deploys anything
that builds into a container image.

## How it works

Configuration is one `config/deploy.yml`:

    service: myapp
    image: user/myapp
    servers:
      - 192.168.0.1
    registry:
      username: registry-user-name
      password:
        - KAMAL_REGISTRY_PASSWORD
    env:
      secret:
        - DATABASE_URL

Then `kamal setup` on first run, `kamal deploy`
thereafter. A deploy: builds the image, pushes it to the
registry, pulls it on each server, starts the new
container, waits for `GET /up` to return `200 OK`, tells
`kamal-proxy` to switch traffic, stops the old container,
and prunes what is no longer used.

Commands are **imperative** — SSH and Docker commands
executed in order, via SSHKit — rather than a
reconciliation loop. You can read exactly what it did.

## Worth knowing

- **`kamal-proxy` handles the cutover**, holding requests
  while the new container comes up. That is where the
  "zero downtime" comes from — see
  [[Deployment Strategies]].
- **Accessories** run supporting containers on the same
  or other hosts: [[PostgreSQL]], [[Redis]], a queue.
- **Destinations** (`kamal deploy -d staging`) merge a
  second config file over the base, which is a cheap
  route to [[Deployment Environments]].
- **Secrets** come from `.kamal/secrets`, read from the
  environment or a password manager — never committed;
  see [[Secrets Management]].
- **Asset bridging** mounts old and new assets together
  during the switch, so in-flight page loads do not 404
  on a hashed filename. Pairs with [[Cache Busting]].
- Installed as a Ruby gem (`gem install kamal`), or run
  from a container if you have no Ruby.

## Watch out for

- **You need a container registry** — Docker Hub, GHCR or
  a private one. That is the main setup cost.
- **Root SSH access** is the default for provisioning,
  because it installs Docker for you.
- **More than one server means you supply the load
  balancer.** Kamal deploys to all of them; it does not
  put anything in front of them.
- **It is not a scheduler.** No autoscaling, no
  rescheduling a dead node's work — that is
  [[Container Orchestration]], deliberately not included.
- Health checks are only as good as your `/up` endpoint.
  Make it check the database, or a broken deploy will
  sail through.

## Related

[[VPS Instead of Hyperscaler]] · [[Coolify]] ·
[[Self-Hosted PaaS]] · [[Docker]] · [[Docker Compose]] ·
[[Containers in Production]] · [[Deployment Strategies]] ·
[[One-Box Deployment]] · [[Kubernetes]] ·
[[Git-Driven Deployment]] · [[Hetzner Cloud]]

## Sources

- [[kamal-home]] · [[kamal-installation]] ·
  [[kamal-configuration]] · [[kamal-readme]]
