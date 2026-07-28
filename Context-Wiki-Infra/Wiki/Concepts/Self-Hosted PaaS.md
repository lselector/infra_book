---
type: Concept
title: "Self-Hosted PaaS"
description: "A Heroku-like control panel that you run on your own VPS - push-to-deploy ergonomics at VPS prices, with the panel itself as the new thing to operate."
wikipedia: "https://en.wikipedia.org/wiki/Self-hosting_(network)"
tags: [deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# Self-Hosted PaaS

Software you install on a box you rent, which then gives
that box the interface of a platform: connect a Git repo,
push, get a running service with a certificate on it.
[[Coolify]] is the option this wiki covers; Dokku and
CapRover are the same idea.

The distinction that matters: [[Managed PaaS]] is a
company running the platform *and* the machines.
Self-hosted PaaS is you running both — you buy the
ergonomics without buying the hardware markup.

## What it typically gives you

- Push-to-deploy from GitHub or GitLab, per
  [[Git-Driven Deployment]].
- Automatic certificates via [[Let's Encrypt]], so
  [[Automatic HTTPS]] is a checkbox rather than a config
  file.
- One-click databases — [[PostgreSQL]], [[Redis]] and
  friends — as containers alongside the app.
- Preview or per-branch deploys, which otherwise means
  building [[Deployment Environments]] by hand.
- Scheduled backups to S3-compatible [[Object Storage]].
- A dashboard with logs, a terminal and basic
  [[Monitoring and Alerting]].

Underneath, almost all of it is [[Docker]] and
[[Docker Compose]] with a nicer face — which is why
nothing here is a lock-in you cannot walk away from.

## Why it belongs in this wiki

It collapses the gap between rung 5 and rung 9 of
[[The Ladder]]. A solo developer gets rollbacks, TLS and
preview environments on a $10 box, and skips a
surprising amount of the work in
[[Continuous Integration and Delivery]]. For the full
argument and the cost comparison, see
[[VPS Instead of Hyperscaler]].

## What it costs you

- **The panel is production software you now operate.**
  It has upgrades, a database of its own, and its own
  failure modes. When it breaks, your deploy path breaks.
- **It wants resources.** Budget roughly 2 vCPU and 2 GB
  of RAM for the control plane before your app gets any.
- **The dashboard is an authenticated public endpoint.**
  Put it behind strong credentials and MFA — it can
  deploy code and read your secrets. See
  [[Linux Server Hardening]] and [[Least Privilege]].
- **Installers often want root over SSH.** Read the
  script before piping it to a shell.
- **Convenience hides the database.** A one-click
  Postgres is still a database you must back up and
  restore — [[Database Backups]] does not go away.

## The alternative on the same box

[[Kamal]] does the deploy half with no control plane at
all: no daemon, no web UI, nothing running between
deploys. If what you want is zero-downtime container
deploys and rollback — rather than a dashboard and
one-click services — it is the smaller thing to own.

## Related

[[Coolify]] · [[Kamal]] · [[Managed PaaS]] ·
[[VPS Instead of Hyperscaler]] · [[One-Box Deployment]] ·
[[Containers in Production]] · [[Docker Compose]] ·
[[Git-Driven Deployment]] · [[Deployment Environments]] ·
[[Cost Control]]

## Sources

- [[coolify-introduction]] · [[coolify-installation]] ·
  [[coolify-readme]] · [[coolify-home]]
