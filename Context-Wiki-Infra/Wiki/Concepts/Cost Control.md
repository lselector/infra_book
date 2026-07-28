---
type: Concept
title: "Cost Control"
description: "Keeping the bill boring - budgets, alerts, and knowing which line items actually grow."
tags: [ops-and-security, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Cost Control

Small infrastructure should cost a predictable, small
amount. Surprises come from a handful of specific places.

## Set these up on day one

- A **budget with an alert** — AWS Budgets, Google Cloud
  budget alerts. Set it well below the number that would
  hurt.
- **Billing alerts to an address you read.**
- A **spend ceiling** where the provider offers one.

## Where bills actually surprise people

| Line | Why |
|---|---|
| Egress bandwidth | charged per GB out; media-heavy sites are hit hardest |
| NAT gateways | hourly plus per-GB, easy to forget |
| Managed database | often the largest single line on a small stack |
| Logs and metrics retention | ingestion charges accumulate silently |
| Idle load balancers and volumes | billed whether used or not |

## The structural answers

- [[Cloudflare R2]] instead of S3 for anything served to
  users — no egress fee.
- A [[Content Delivery Network]] in front of everything,
  so origin bandwidth stays low.
- [[SQLite]] or self-hosted [[PostgreSQL]] until managed
  is genuinely required.
- Delete unused resources; a monthly sweep pays for
  itself.
- A rented VPS instead of a hyperscaler footprint, where
  the load balancer, NAT gateway and managed database in
  the table above simply have no line item — see
  [[VPS Instead of Hyperscaler]].

## Related

[[Cloud Service Models]] · [[Managed PaaS]] ·
[[Object Storage]] · [[The Ladder]] · [[Anti-Patterns]] ·
[[VPS Instead of Hyperscaler]] · [[Self-Hosted PaaS]]

## Sources

- [[aws-budgets-managing-costs]] · [[gcp-billing-budgets]]
  · [[cloudflare-pages-limits]] · [[aws-ses-pricing]]
