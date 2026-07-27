---
type: Concept
title: "Monitoring and Alerting"
description: "Knowing the site is down before your users tell you - starting with one uptime check."
tags: [ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Monitoring and Alerting

Monitoring records what the system is doing. Alerting
wakes someone when it matters.

## In order of value per hour spent

1. **An external uptime check.** Something outside your
   infrastructure fetching your homepage every minute.
   [[Uptime Kuma]] self-hosted, or any hosted checker.
2. **Certificate expiry** and **domain expiry** alerts —
   two outages that are entirely preventable.
3. **Error rate.** A spike in `5xx` responses.
4. **Disk space.** The classic one-box outage: logs fill
   the disk and the database stops accepting writes.
5. **Backup success**, from [[Database Backups]].
6. Then latency, saturation, and everything else.

## Why it matters here

The Google SRE guidance on symptom-based alerting applies
at any size: alert on things users experience, not on
every metric that moves. An alert that fires without
requiring action trains everyone to ignore alerts.

## Related

[[Service Level Objectives]] · [[Audit Logging]] ·
[[Incident Response]] · [[Prometheus]] · [[Uptime Kuma]]

## Sources

- [[sre-book-monitoring]] · [[prometheus-overview]] ·
  [[grafana-loki-get-started]] · [[uptime-kuma-readme]]
