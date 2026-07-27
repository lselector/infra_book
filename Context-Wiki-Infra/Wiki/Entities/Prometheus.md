---
type: Tool
title: "Prometheus"
description: "Pull-based metrics and alerting - the open-source standard, and more than a small site needs."
tags: [ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Prometheus

Scrapes metrics from HTTP endpoints, stores them as time
series, and evaluates alerting rules over them with its
own query language.

## Where it fits here

At the point where "is the site up" is no longer enough
and you want to see request rates, error rates and
latency over time. Usually paired with Grafana for
dashboards and Alertmanager for routing.

## Be honest about the timing

For rung 5-8 of [[The Ladder]], an external uptime check
and log alerts cover most of the value at a fraction of
the effort — see [[Monitoring and Alerting]]. Prometheus
is another stateful service to run, and running your
monitoring on the machine it monitors is a well-known
mistake.

## If you do adopt it

- Instrument the four signals: traffic, errors, latency,
  saturation.
- Alert on symptoms, not causes.
- Keep retention short locally; ship long-term data
  elsewhere.

## Related

[[Monitoring and Alerting]] · [[Grafana Loki]] ·
[[Service Level Objectives]] · [[Uptime Kuma]]

## Sources

- [[prometheus-overview]] · [[sre-book-monitoring]]
