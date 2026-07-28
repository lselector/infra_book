---
type: Platform
title: "Ubuntu Server"
description: "The default Linux for a cheap VPS - long-term support, and the distribution every guide assumes."
wikipedia: "https://en.wikipedia.org/wiki/Ubuntu"
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Ubuntu Server

The Linux distribution assumed throughout this book for
[[One-Box Deployment]].

## Why this one

- LTS releases get five years of security updates, so a
  box built today is supportable for the life of most
  projects.
- Every provider offers a current image.
- The documentation and the wider internet's answers
  assume it, which matters when something breaks at 11pm.

## The first hour on a new instance

1. Create a sudo user; stop using root.
2. [[SSH Key Authentication]], then disable passwords.
3. [[UFW]]: allow 22, 80, 443.
4. [[Unattended Upgrades]] for security patches.
5. A swap file on small instances.
6. Install [[Caddy]] and your runtime; run the app under
   [[systemd]].

This is [[Linux Server Hardening]] and it is genuinely
about an hour.

## Watch out for

Release upgrades. Plan them; do not discover mid-incident
that the LTS you are on went end-of-standard-support.

## Related

[[Linux Server Hardening]] · [[One-Box Deployment]] ·
[[systemd]] · [[UFW]] · [[Unattended Upgrades]]

## Sources

- [[ubuntu-server-openssh]] · [[ubuntu-server-firewall]] ·
  [[ubuntu-automatic-updates]] · [[ubuntu-community-ufw]]
