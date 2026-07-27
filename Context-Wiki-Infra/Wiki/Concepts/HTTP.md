---
type: Concept
title: "HTTP"
description: "Methods, status codes, headers and caching - the protocol every layer of this book manipulates."
tags: [foundations, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# HTTP

The request/response protocol the whole stack speaks. Most
infrastructure work is, in practice, deciding which
component sets which header.

## The parts that matter operationally

- **Methods** — `GET` and `HEAD` are safe and cacheable;
  `POST`, `PUT`, `DELETE` are not.
- **Status codes** — `2xx` fine, `3xx` redirect, `4xx`
  your caller's problem, `5xx` yours. Alert on `5xx`.
- **Headers** — caching (`Cache-Control`, `ETag`),
  security ([[Security Headers]]), content negotiation,
  and CORS.
- **Redirects** — `301` is cached by browsers more or less
  forever; use `302` while you are still deciding.

## Why it matters here

- [[Cache Busting]] and [[Content Delivery Network]]
  behaviour are entirely `Cache-Control` decisions.
- A [[Reverse Proxy]] exists to rewrite and forward these
  requests, and to add the headers your app forgot.
- Local previews need `Cache-Control: no-store` or you
  will debug a cached copy of yesterday's page.

## Related

[[TLS and HTTPS]] · [[Reverse Proxy]] ·
[[Security Headers]] · [[Cache Busting]]

## Sources

- [[mdn-http-overview]] · [[mdn-cors]] ·
  [[mdn-what-is-a-web-server]]
