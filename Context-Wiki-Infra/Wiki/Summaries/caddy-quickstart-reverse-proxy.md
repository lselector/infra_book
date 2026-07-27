---
type: Summary
title: "Caddy quick start — reverse proxy"
description: "This guide will show you how to get a production-ready reverse proxy with or without HTTPS up and running quickly."
resource: "https://caddyserver.com/docs/quick-starts/reverse-proxy"
source_file: "Raw/03_deployments/caddy-quickstart-reverse-proxy.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Caddy quick start — reverse proxy

Extractive digest of the immutable capture in
`Raw/03_deployments/caddy-quickstart-reverse-proxy.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://caddyserver.com/docs/quick-starts/reverse-proxy>

## Opening

> This guide will show you how to get a production-ready reverse proxy with or without HTTPS up and running quickly.
> This tutorial assumes that you have a backend HTTP service running at `127.0.0.1:9000`. These commands are for Linux, but the same principles apply to other operating systems.
> You can get a simple reverse proxy running without a config file, or you can use a config file for more flexibility and control.
> To start a plaintext HTTP proxy from port 2080 to port 9000 on your machine:

## Contents of the source document

- Reverse proxy quick-start
  - Command line
  - Caddyfile
  - HTTPS from client to proxy
  - HTTPS from proxy to backend

## Related pages

[[Caddy]] · [[HTTP]] · [[Reverse Proxy]]
