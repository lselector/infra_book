---
type: Concept
title: "Linux Server Hardening"
description: "The short list that takes a fresh VPS from exposed to reasonable in under an hour."
wikipedia: "https://en.wikipedia.org/wiki/Hardening_(computing)"
tags: [deployments, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Linux Server Hardening

The default image is not safe to leave on the internet.
This is the minimum, and it is genuinely short.

## The checklist

1. **A non-root sudo user.** Do daily work as that user.
2. **[[SSH Key Authentication]] only** — set
   `PasswordAuthentication no` and `PermitRootLogin no`.
3. **A firewall.** Allow 22, 80, 443 and nothing else;
   [[UFW]] makes this three commands.
4. **[[Unattended Upgrades]]** for security patches.
5. **[[Fail2Ban]]** to blunt SSH brute-forcing (largely
   redundant once passwords are off, but cheap).
6. **Bind services to localhost** — especially
   [[PostgreSQL]]. Nothing should listen publicly except
   the [[Reverse Proxy]].
7. **A swap file** on small instances, so a memory spike
   degrades instead of killing the process.

## Why it matters here

Steps 1-4 remove the overwhelming majority of automated
attacks. This is not a compliance exercise; it is the
price of admission for rung 5 of [[The Ladder]].

## Verify, do not assume

Run [[Lynis]] afterwards. It audits the running system and
tells you what you actually left open.

## Related

[[One-Box Deployment]] · [[SSH Key Authentication]] ·
[[Unattended Upgrades]] · [[Least Privilege]] ·
[[Security Testing]] · [[Development Setup]]

## Sources

- [[ubuntu-server-openssh]] · [[ubuntu-server-firewall]] ·
  [[ubuntu-community-ufw]] · [[ubuntu-automatic-updates]]
  · [[lynis-readme]] · [[fail2ban-readme]]
