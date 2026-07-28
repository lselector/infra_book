---
type: Concept
title: "Reverse Proxy"
description: "The process in front of your app that terminates TLS, serves static files and forwards the rest."
wikipedia: "https://en.wikipedia.org/wiki/Reverse_proxy"
tags: [deployments, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# Reverse Proxy

A server that accepts public requests and forwards them to
one or more application processes behind it.

## What it takes off your app

- **TLS termination** — the app speaks plain HTTP on
  localhost. See [[Automatic HTTPS]].
- **Static file serving**, far faster than an app
  framework doing it.
- **Compression, timeouts, request size limits**.
- **A stable public port** while the app restarts.
- **[[Security Headers]]** applied in one place.

## Why it matters here

Never expose an application server directly. Gunicorn,
Uvicorn and friends are explicit that they expect a proxy
in front, and it is where you get HTTPS for free.

[[Caddy]] is the recommended default in this book: two
lines of config and certificates are obtained and renewed
automatically. [[Nginx]] is the incumbent — more knobs,
more configuration, and certificate renewal is a separate
concern you must wire up with [[Certbot]].

## Watch out for

Forgetting to forward the original client IP and protocol
headers, after which your app logs every request as coming
from `127.0.0.1` and builds `http://` redirect URLs.

## Related

[[Automatic HTTPS]] · [[TLS and HTTPS]] ·
[[One-Box Deployment]] · [[Load Balancing]] ·
[[Security Headers]]

## Sources

- [[caddy-quickstart-reverse-proxy]] ·
  [[nginx-reverse-proxy-guide]] ·
  [[fastapi-run-server-manually]]
