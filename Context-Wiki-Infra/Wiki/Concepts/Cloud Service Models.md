---
type: Concept
title: "Cloud Service Models"
description: "IaaS, PaaS, serverless and SaaS - who operates what, and what you give up for convenience."
wikipedia: "https://en.wikipedia.org/wiki/Cloud_computing"
tags: [foundations, architecture]
timestamp: "2026-07-27T00:00:00Z"
---

# Cloud Service Models

Four ways to rent computing, distinguished by where the
line falls between what you operate and what the provider
operates.

## The four models

| Model | You operate | Provider operates | Example here |
|---|---|---|---|
| IaaS | OS, runtime, app, data | hardware, network | [[Hetzner Cloud]], [[Amazon EC2]] |
| PaaS | app, data | OS, runtime, scaling | [[Render]], [[Fly.io]], [[Railway]] |
| Serverless | functions, data | everything else | [[AWS Lambda]], [[Cloudflare Pages Functions]] |
| SaaS | configuration only | everything | [[Web3Forms]], [[AWeber]], [[Stripe]] |

## Why it matters here

- The cheapest stack for a small project is usually the
  one where you operate the least. A static site on
  [[Cloudflare Pages]] costs nothing and has no server to
  patch; the same site on a VPS costs money *and* time.
- Cost per unit of compute runs the other way: IaaS is
  cheapest per CPU-hour, SaaS most expensive. The trade is
  always money against operational burden.
- Most real stacks mix models. A typical rung on
  [[The Ladder]] is IaaS for the app, SaaS for email and
  payments, PaaS for nothing at all.

## Watch out for

- Serverless is not automatically cheap. It is cheap when
  traffic is spiky or low, and can be expensive under
  steady high load.
- Managed PaaS pricing tends to step sharply once you
  exceed the free tier.

## Related

[[Serverless Architecture]] · [[Managed PaaS]] ·
[[One-Box Deployment]] · [[The Ladder]] ·
[[Shared Responsibility Model]] · [[Cost Control]]

## Sources

- [[gcp-iaas-paas-saas]] · [[aws-what-is-cloud-computing]]
  · [[aws-what-is-serverless]]
