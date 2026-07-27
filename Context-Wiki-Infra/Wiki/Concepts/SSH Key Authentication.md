---
type: Concept
title: "SSH Key Authentication"
description: "Replacing passwords with keypairs - the single highest-value change on a new server."
tags: [deployments, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# SSH Key Authentication

You hold a private key; the server holds the matching
public key. Nothing guessable crosses the network.

## Doing it properly

- Generate with `ssh-keygen -t ed25519`. Ed25519 is the
  current default: short, fast, strong.
- Protect the private key with a passphrase and an agent.
- Copy the public key with `ssh-copy-id`.
- Only then set `PasswordAuthentication no` — verify you
  can log in with the key first, in a second terminal you
  keep open.

## Why it matters here

Password authentication on port 22 is under constant
automated attack from the moment a VPS gets an IP.
Disabling it eliminates that entire attack class in one
setting.

## Watch out for

- Locking yourself out. Keep the existing session open
  until the new method is proven.
- Copying the *private* key to servers. Only the public
  key ever leaves your machine.
- Shared team keys. Give each person their own so
  offboarding is a line removed, which is also what an
  [[Access Review]] expects.

## Related

[[Linux Server Hardening]] · [[Least Privilege]] ·
[[Secrets Management]] · [[Access Review]]

## Sources

- [[ubuntu-server-openssh]] · [[ssh-keygen-man-page]]
