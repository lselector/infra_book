---
type: Tool
title: "Bitwarden"
description: "Open-source password manager with a usable free tier - the first thing to install and the vault every other credential lives in."
wikipedia: "https://en.wikipedia.org/wiki/Bitwarden"
tags: [dev-environment, ops-and-security, credentials]
timestamp: "2026-07-27T00:00:00Z"
---

# Bitwarden

<https://bitwarden.com> — a password manager with
clients for every platform, browser extensions, a CLI,
and a free tier that covers a solo developer.

## Why this one

- Open source and independently audited.
- Free tier includes unlimited passwords and sync
  across all your devices.
- Self-hostable if you would rather (Vaultwarden is the
  common lightweight server).
- 1Password is an equally good paid alternative; the
  important decision is *using one*, not which.

## What goes in it

- One unique generated password per account — registrar,
  host, cloud console, [[GitHub]], email.
- Recovery codes for every account with
  [[Multi-Factor Authentication]] turned on. These are
  what people actually lose.
- SSH private keys and `~/.ssh/config`, as encrypted
  file attachments, so a dead laptop is an
  inconvenience rather than a catastrophe.
- TOTP codes, if you accept that this puts the second
  factor in the same vault as the first.

## What does not go in it

Application secrets — database passwords, API keys the
server needs at runtime. Those belong in environment
variables and a secret store; see
[[Secrets Management]] and [[AWS Secrets Manager]].
A human vault is for humans.

## The master password

It protects everything else, so: long, memorable,
unique, never typed anywhere but the vault, and written
down once on paper in a safe place along with the
recovery kit.

## Related

[[Development Setup]] · [[Multi-Factor Authentication]] ·
[[Secrets Management]] · [[SSH Key Authentication]] ·
[[Least Privilege]]

## Sources

- Upstream documentation: <https://bitwarden.com/help/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
