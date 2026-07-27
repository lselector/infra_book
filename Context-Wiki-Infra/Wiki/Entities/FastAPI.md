---
type: Tool
title: "FastAPI"
description: "A modern Python web framework - the backend assumed in this book's one-box stack."
tags: [deployments, application]
timestamp: "2026-07-27T00:00:00Z"
---

# FastAPI

A Python framework for HTTP APIs and applications, with
type-hint-driven validation and automatic OpenAPI
documentation.

## Why it appears here

It is the backend in rung 5 of [[The Ladder]]: quick to
write, fast enough by a wide margin for a small
application, and it produces interactive API docs for free
— which matters when the API is the product.

## Running it in production

FastAPI is served by an ASGI server, usually Uvicorn,
supervised by [[systemd]], behind [[Caddy]]:

```
Caddy :443  ->  127.0.0.1:8000  (uvicorn)  ->  app
```

The framework's own documentation is explicit that a proxy
should terminate TLS and that the app should not be
exposed directly.

## Watch out for

- Worker count. Too many processes on a small box exhaust
  memory and [[PostgreSQL]] connections — see
  [[Connection Pooling]].
- Blocking calls inside `async def` handlers stall the
  event loop; use `def` handlers for synchronous work.

## Related

[[Monolithic Web App]] · [[Caddy]] · [[systemd]] ·
[[Single Page Application and API]] · [[Django]]

## Sources

- [[fastapi-deployment-concepts]] ·
  [[fastapi-run-server-manually]]
