---
type: Tool
title: "Fail2Ban"
description: "Watches logs and bans IPs that keep failing to log in."
wikipedia: "https://en.wikipedia.org/wiki/Fail2ban"
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Fail2Ban

Monitors log files for repeated authentication failures
and adds temporary firewall bans for the offending
addresses.

## What it is genuinely for

Reducing noise and load from the constant automated SSH
brute-forcing that begins the moment a VPS gets a public
IP.

## The honest assessment

Once [[SSH Key Authentication]] is enforced and password
authentication is off, brute-forcing cannot succeed
anyway. Fail2Ban then buys you quieter logs and slightly
less wasted CPU — worthwhile, but it is not the control
protecting you.

Do the key change first. Fail2Ban is a supplement, never a
substitute.

## Where it earns more

Protecting application login endpoints, where you *do*
have passwords, by watching your app's log for failed
attempts.

## Related

[[Linux Server Hardening]] · [[SSH Key Authentication]] ·
[[UFW]] · [[Lynis]]

## Sources

- [[fail2ban-readme]] · [[ubuntu-server-openssh]]
