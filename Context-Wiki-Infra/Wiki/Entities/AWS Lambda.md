---
type: Service
title: "AWS Lambda"
description: "Functions that run on demand - the serverless compute primitive."
wikipedia: "https://en.wikipedia.org/wiki/AWS_Lambda"
tags: [deployments, serverless]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Lambda

Runs a function in response to an event — an HTTP request
via [[Amazon API Gateway]], a queue message, a schedule —
and bills per millisecond of execution.

## Where it fits here

- The backend half of a static frontend plus API,
  described in [[Serverless Architecture]].
- Glue: processing an [[Amazon SES]] bounce notification,
  resizing an upload, running a nightly job.

## The constraints to design around

- **Cold starts.** First invocation after idle is slower.
- **Execution timeout.** Long jobs need a different
  compute model.
- **Database connections.** Many short-lived invocations
  exhaust [[PostgreSQL]] connections; use
  [[Connection Pooling]] via a proxy.
- **Statelessness.** Nothing persists between
  invocations.

## Watch out for

Cost intuition. Cheap at low and spiky volume; frequently
more expensive than a $6 VPS under steady load. Model it.

## Related

[[Serverless Architecture]] · [[Amazon API Gateway]] ·
[[Connection Pooling]] · [[Cost Control]]

## Sources

- [[aws-lambda-welcome]] · [[aws-apigateway-welcome]] ·
  [[aws-what-is-serverless]]
