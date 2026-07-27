---
type: Service
title: "Amazon API Gateway"
description: "The HTTP front door for Lambda functions - routing, auth and throttling."
tags: [deployments, serverless]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon API Gateway

Accepts HTTP requests and routes them to
[[AWS Lambda]] functions or other backends, adding
authorisation, throttling and request validation.

## What it provides

- Routing and stage management (dev, prod).
- Throttling and usage plans — useful for
  [[Cost Control]] as much as for abuse prevention.
- Authorisers, including [[JSON Web Token]] validation, so
  auth happens before your code runs.
- [[CORS]] configuration, which you will need for a
  [[Single Page Application and API]].

## Watch out for

- HTTP APIs are cheaper and simpler than REST APIs; the
  naming is confusing and the default is not always the
  one you want.
- Per-request pricing is fine at low volume and becomes a
  real line at high volume.
- Payload and timeout limits constrain what can be served
  through it.

## Related

[[AWS Lambda]] · [[Serverless Architecture]] · [[CORS]] ·
[[Single Page Application and API]]

## Sources

- [[aws-apigateway-welcome]] · [[aws-lambda-welcome]]
