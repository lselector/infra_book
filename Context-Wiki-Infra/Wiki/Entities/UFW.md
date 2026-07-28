---
type: Tool
title: "UFW"
description: "Uncomplicated Firewall - three commands between a fresh VPS and a closed one."
wikipedia: "https://en.wikipedia.org/wiki/Uncomplicated_Firewall"
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# UFW

A front end to iptables on Ubuntu, designed so that a
basic firewall is three commands rather than a project.

## The three commands

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw enable
```

Default policy is deny inbound, allow outbound. Everything
except SSH and HTTP(S) is now closed.

## Why it matters here

Combined with binding services to `127.0.0.1`, it means a
misconfigured database or a development server started on
`0.0.0.0` is not reachable from the internet — defence in
depth against your own future mistake.

## Watch out for

- Enabling UFW without first allowing SSH locks you out of
  a remote box. Allow SSH first, every time.
- Docker publishes ports by manipulating iptables directly
  and can bypass UFW rules. If you run
  [[Docker Compose]], verify what is actually exposed with
  `ss -tlnp` rather than trusting `ufw status`.

## Related

[[Linux Server Hardening]] · [[Ubuntu Server]] ·
[[VPC and Security Groups]] · [[Docker Compose]]

## Sources

- [[ubuntu-community-ufw]] · [[ubuntu-server-firewall]]
