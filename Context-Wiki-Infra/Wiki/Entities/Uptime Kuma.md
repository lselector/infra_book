---
type: Tool
title: "Uptime Kuma"
description: "Self-hosted uptime monitoring with a good UI - the first monitoring you should set up."
tags: [ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Uptime Kuma

A self-hosted monitor that checks HTTP endpoints, TCP
ports, DNS and certificates on a schedule, and notifies
you through many channels when something fails.

## Why it is the recommended first step

It answers the question that matters most — is the site
up — and it does so from outside the application. It also
watches **certificate expiry**, which closes one of the
most common and most preventable outage causes.

Setup is one container and a few minutes.

## The one rule

**Run it somewhere else.** A monitor on the machine it
monitors goes down with it and tells you nothing. A
different provider, a cheap second VPS, or a hosted
checker.

## Related

[[Monitoring and Alerting]] · [[TLS and HTTPS]] ·
[[Incident Response]] · [[Prometheus]]

## Sources

- [[uptime-kuma-readme]] · [[sre-book-monitoring]]
