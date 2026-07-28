---
type: Tool
title: "Express"
description: "The minimal Node.js web framework - the JavaScript equivalent of the FastAPI rung."
wikipedia: "https://en.wikipedia.org/wiki/Express.js"
tags: [architectures, deployments, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# Express

The long-standing minimal web framework for
[[Node.js]]: routes, middleware, and almost nothing
else. If your backend is JavaScript, this is the
counterpart to [[FastAPI]] in the one-box stack at rung
5 of [[Stacks]].

```javascript
import express from "express"

const app = express()
app.get("/healthz", (_req, res) => res.send("ok"))
app.get("/api/items", async (req, res) => {
  res.json(await listItems(req.query.q))
})
app.listen(process.env.PORT ?? 8000)
```

Behind [[Caddy]], supervised by [[systemd]] or a
container restart policy, that is a production service.

## The middleware you actually need

- `helmet` — sets the [[Security Headers]] you would
  otherwise forget.
- `cors` — configured to your origins, not `*`
  ([[CORS]]).
- A rate limiter on anything unauthenticated.
- `express.json({ limit: "1mb" })` — an unbounded body
  parser is a denial-of-service waiting to happen.
- Structured request logging with a correlation ID.

## Alternatives worth knowing

Fastify (faster, schema-first validation), Hono (edge
and Workers), NestJS (opinionated, Angular-shaped) and
the built-in `node:http` for something truly small. The
operational story is identical for all of them; pick on
ergonomics.

## Watch out for

- **Unhandled promise rejections.** Express 4 does not
  catch async errors thrown in handlers — wrap them or
  use Express 5.
- **Blocking the event loop** in a handler stalls every
  other request ([[Node.js]]).
- **`trust proxy`.** Behind a reverse proxy, set it, or
  client IPs and rate limits are wrong.
- **Graceful shutdown.** Close the server on `SIGTERM`
  so deploys drain rather than cut.

## Related

[[Node.js]] · [[FastAPI]] · [[Reverse Proxy]] ·
[[Caddy]] · [[systemd]] · [[Security Headers]] ·
[[CORS]] · [[Single Page Application and API]]

## Sources

- Upstream documentation: <https://expressjs.com>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
