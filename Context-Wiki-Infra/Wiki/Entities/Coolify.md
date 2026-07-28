---
type: Tool
title: "Coolify"
description: "An open-source Heroku you install on your own VPS - dashboard, push-to-deploy, one-click databases and automatic TLS."
website: "https://coolify.io/"
tags: [deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# Coolify

A self-hostable deployment platform: install it on a
server you rent, connect a Git repository, and get
push-to-deploy applications, databases and services with
certificates, backups and logs behind a web dashboard.
Open source, with no features held back behind a paywall.

The canonical example of a [[Self-Hosted PaaS]].

## Why it appears here

It is the shortest route from [[One-Box Deployment]] to
something that *feels* like [[Managed PaaS]], at VPS
prices. For a solo developer running several small apps
on one box, it removes most of the per-app deploy
plumbing — see [[VPS Instead of Hyperscaler]].

## What you get

- Deploys from GitHub, GitLab, Bitbucket or Gitea, plus
  any Docker-compatible service and a catalogue of
  one-click ones.
- Free certificates via [[Let's Encrypt]], renewed
  automatically — [[Automatic HTTPS]] without touching a
  config file.
- Databases as managed-feeling containers, with scheduled
  backups to S3-compatible [[Object Storage]].
- Per-pull-request preview deploys, which is
  [[Deployment Environments]] for free.
- Server monitoring, a browser terminal, webhooks and a
  REST API for [[Continuous Integration and Delivery]].
- Multi-server and Docker Swarm setups from one panel.

## Installing it

One script on a fresh box:

    curl -fsSL https://cdn.coollabs.io/coolify/install.sh | sudo bash

It installs Docker and its dependencies, generates an SSH
key, writes everything under `/data/coolify`, and serves
the dashboard on port 8000. Read the script before you
run it — piping a URL into a root shell deserves that
much; [[Linux Server Hardening]] applies here too.

Requirements are modest but not nothing: 2 CPU cores and
2 GB of RAM minimum for the control plane, on a
Debian/Ubuntu, RHEL, SUSE or Arch host. The Ubuntu
auto-installer supports LTS releases only.

## Watch out for

- **The panel needs root SSH** and non-root users are not
  yet fully supported. Treat the box as one trust
  boundary.
- **The dashboard can deploy code and read every secret
  you store.** Strong credentials and MFA are not
  optional — see [[Multi-Factor Authentication]] and
  [[Least Privilege]].
- **It consumes the resources it asks for.** On a 2 GB
  box, Coolify plus a database leaves little for the app.
  Size up, or use [[Kamal]] instead.
- **Upgrades are yours.** A self-hosted platform is
  software you operate; the hosted **Coolify Cloud**
  (from about $5/month, connecting to *your* servers) is
  the trade if you would rather not.
- **Docker installed via snap is not supported** — a
  common cause of a failed install on Ubuntu.

## Related

[[Self-Hosted PaaS]] · [[VPS Instead of Hyperscaler]] ·
[[Kamal]] · [[Managed PaaS]] · [[One-Box Deployment]] ·
[[Docker]] · [[Docker Compose]] ·
[[Containers in Production]] · [[Git-Driven Deployment]] ·
[[Hetzner Cloud]] · [[DigitalOcean]] · [[Cost Control]]

## Sources

- [[coolify-introduction]] · [[coolify-installation]] ·
  [[coolify-home]] · [[coolify-readme]]
