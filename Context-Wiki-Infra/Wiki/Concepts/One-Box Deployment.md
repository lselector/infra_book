---
type: Concept
title: "One-Box Deployment"
description: "Everything on a single small VPS - the cheapest way to run real server-side code, and where ops burden begins."
wikipedia: "https://en.wikipedia.org/wiki/Virtual_private_server"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# One-Box Deployment

App, reverse proxy and database on one virtual machine.
Rung 5 of [[The Ladder]], and the point at which you
acquire a computer to look after.

## What it looks like

- A $5-12/month VPS from [[Hetzner Cloud]] or
  [[DigitalOcean]].
- [[Caddy]] terminating TLS and proxying to the app.
- The app under [[systemd]] so it restarts on boot and on
  crash.
- [[SQLite]] or [[PostgreSQL]] on the same disk.
- Nightly backups off the box.

## Getting code onto it

`git pull` and a `systemctl restart` is the honest
starting point. When you want zero-downtime deploys and
rollback, [[Kamal]] adds them over SSH with no daemon on
the box; [[Coolify]] adds a whole dashboard instead. The
cost case for choosing this over AWS at all is
[[VPS Instead of Hyperscaler]].

## Why it matters here

It is astonishingly capable. A single modern 2-vCPU
instance behind a [[Content Delivery Network]] serves more
traffic than most projects will ever see. Reaching for
Kubernetes at this stage is the definitive
[[Anti-Patterns]] example.

## What you have signed up for

- OS patching — automate it, see [[Unattended Upgrades]].
- [[Linux Server Hardening]]: SSH keys, firewall,
  no root login.
- [[Database Backups]] with a tested restore.
- Being the only thing between a disk failure and data
  loss.

## Related

[[Linux Server Hardening]] · [[Reverse Proxy]] ·
[[Database Backups]] · [[Monolithic Web App]] ·
[[Managed PaaS]] · [[VPS Instead of Hyperscaler]] ·
[[Self-Hosted PaaS]] · [[Kamal]] · [[Coolify]]

## Sources

- [[hetzner-create-a-server]] ·
  [[digitalocean-droplet-quickstart]] ·
  [[ubuntu-server-openssh]] · [[systemd-service-unit]]
