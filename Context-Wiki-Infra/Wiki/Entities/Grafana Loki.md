---
type: Tool
title: "Grafana Loki"
description: "Log aggregation that indexes labels rather than content - cheap to run."
tags: [ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Grafana Loki

Aggregates logs and indexes only their labels, not the
full text, which makes storage and operation much cheaper
than a full search cluster.

## Why the design matters

Elasticsearch-style log stacks are famously expensive to
run for a small team. Loki trades full-text indexing for
label-based selection plus a grep over the selected
stream — which for "show me this service's errors in the
last hour" is exactly right.

## Where it fits

Once you have more than one machine or more than a couple
of services and `journalctl` on the box has stopped being
sufficient. Below that, [[systemd]]'s journal is a
perfectly good log store.

## Notes

- Label cardinality is the thing to control; a label per
  user ID will hurt.
- Never log secrets or personal data — see
  [[Audit Logging]].

## Related

[[Monitoring and Alerting]] · [[Prometheus]] ·
[[Audit Logging]] · [[systemd]]

## Sources

- [[grafana-loki-get-started]] ·
  [[owasp-logging-cheatsheet]]
