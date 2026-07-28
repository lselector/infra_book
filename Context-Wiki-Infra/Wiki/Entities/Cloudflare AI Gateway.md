---
type: Service
title: "Cloudflare AI Gateway"
description: "A proxy between your app and the model providers - logs, caching, rate limits, retries and fallback, for a changed base URL."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [ai-in-saas, ops-and-security]
timestamp: "2026-07-28T00:00:00Z"
---

# Cloudflare AI Gateway

A managed proxy that sits between your backend and
whichever model providers you call. You change the base
URL of the provider SDK to the gateway; it forwards the
request and gives you analytics, logging, caching, rate
limiting, retries and model fallback on the way through.

It is the "LLM ops" layer as a hosted product, and there
is a free tier.

## What it does that you would otherwise build

| Feature | Otherwise |
|---|---|
| Request/response logs with tokens and cost | your own metering table |
| Analytics per model and per app | a dashboard nobody built |
| Response caching for repeated prompts | a hash key in [[Redis]] |
| Rate limiting at the gateway | [[Rate Limiting]] in your app |
| Retries and provider fallback | code around the SDK |
| One endpoint across providers | an adapter module |

## Where it helps, and where it does not

It is genuinely good at the observability and the
multi-provider seam: when a provider degrades, failing
over is configuration rather than a deploy, and the
per-model cost breakdown arrives without you writing it.

It does **not** replace your own accounting. Its limits
are keyed on the gateway's view of the traffic, not on
your tenants, and its logs live outside your database.
Per-tenant quotas, plan enforcement and billing still
need your records ([[Usage Quotas and Metering]]), and
authentication still happens at your endpoint
([[LLM API Integration]]).

Think of it as a [[Reverse Proxy]] specialised for model
traffic — useful, and not the place your business logic
goes.

## Watch out for

- **It is another hop.** One more dependency between your
  request and the answer, with its own failure modes
  ([[Single Point of Failure]]).
- **Prompts pass through a third party.** That is a
  vendor and a data-flow question, and a line in your
  [[SOC 2]] subprocessor list.
- **Cached AI responses can be wrong to reuse.** Two
  users asking the same question in different tenants
  should not necessarily get the same answer — scope
  the cache key or leave the cache off.
- **Provider features can lag** behind the provider's own
  API when they are proxied.

## Related

[[LLM API Integration]] · [[Usage Quotas and Metering]] ·
[[Rate Limiting]] · [[Cloudflare]] · [[Reverse Proxy]] ·
[[Caching]] · [[Monitoring and Alerting]] ·
[[Cost Control]] · [[Claude API]]

## Sources

- [[cloudflare-ai-gateway]] ·
  [[cloudflare-rate-limiting-rules]] ·
  [[anthropic-rate-limits]] · [[anthropic-prompt-caching]]
