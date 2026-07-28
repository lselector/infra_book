---
type: Tool
title: "Lynis"
description: "Audits a running Linux system and tells you what hardening you actually missed."
wikipedia: "https://en.wikipedia.org/wiki/Lynis"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Lynis

A shell-based auditing tool run on the host. It inspects
the live configuration — SSH, firewall, kernel parameters,
file permissions, installed packages — and produces
findings with a hardening index.

## Why it earns a place

[[Linux Server Hardening]] is a checklist you believe you
followed. Lynis checks the machine rather than your
memory, and it routinely finds the item you skipped: a
permissive SSH option, a service listening you forgot, a
missing auditd.

```bash
sudo lynis audit system
```

## How to treat the output

As a prioritised list, not a score to maximise. Many
suggestions are irrelevant to a single-purpose web server.
Work the ones that relate to network exposure and
authentication first, and record the ones you consciously
decline — that record is useful during a
[[SOC 2]] readiness exercise.

## Related

[[Linux Server Hardening]] · [[Security Testing]] ·
[[Ubuntu Server]] · [[Fail2Ban]] · [[SOC 2]]

## Sources

- [[lynis-readme]] · [[cis-controls-list]]
