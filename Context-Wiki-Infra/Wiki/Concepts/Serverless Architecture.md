---
type: Concept
title: "Serverless Architecture"
description: "Functions that run on demand and cost nothing at rest - with real constraints attached."
wikipedia: "https://en.wikipedia.org/wiki/Serverless_computing"
tags: [deployments, architecture]
timestamp: "2026-07-27T00:00:00Z"
---

# Serverless Architecture

Code runs in response to events. There is no process to
keep alive, and you pay per invocation rather than per
hour.

## Why it matters here

- Genuinely $0 at zero traffic, which suits side projects,
  internal tools and spiky workloads.
- No patching, no capacity planning.
- Pairs naturally with a static frontend: files on
  [[Cloudflare Pages]], dynamic bits in
  [[Cloudflare Pages Functions]] or [[AWS Lambda]] behind
  [[Amazon API Gateway]].

## The constraints that bite

- **Cold starts** add latency to the first request after
  idle.
- **Execution time limits** rule out long jobs.
- **Database connections** do not pool well from
  thousands of short-lived invocations — this is what
  [[PgBouncer]] and serverless-aware drivers exist for.
- **Local development** is less pleasant than running one
  process.

## Cost reality

Cheap when traffic is low or spiky; often *more*
expensive than a $6 VPS under steady load. Model it before
committing.

## Related

[[Cloud Service Models]] · [[Managed PaaS]] ·
[[Connection Pooling]] · [[Cost Control]] ·
[[Micro-VMs]] · [[Cold Starts]] · [[Firecracker]] ·
[[Cloudflare Workers]] · [[Google Cloud Run]] ·
[[Event-Driven Architecture]] ·
[[Streaming Responses]]

## Sources

- [[aws-what-is-serverless]] · [[aws-lambda-welcome]] ·
  [[aws-apigateway-welcome]] ·
  [[cloudflare-pages-functions]]
