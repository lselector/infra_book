---
type: Tool
title: "Caddy"
description: "A web server that obtains and renews TLS certificates by itself - the recommended reverse proxy here."
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# Caddy

An HTTP server written in Go whose distinguishing feature
is that HTTPS is on by default and requires no
configuration.

## The whole config

```
example.com {
    reverse_proxy 127.0.0.1:8000
}
```

That obtains a certificate from [[Let's Encrypt]],
installs it, renews it, redirects HTTP to HTTPS, and
proxies to the app. There is no separate certificate tool,
no cron entry, no renewal to forget.

## Why it is preferred over Nginx here

Not performance — both are fast enough. It is that
[[Automatic HTTPS]] removes an entire class of outage, and
that a five-line Caddyfile is comprehensible six months
later in a way an Nginx server block plus a
[[Certbot]] timer is not.

## Other useful features

- `file_server` for static files.
- Automatic HTTP/2 and HTTP/3.
- Local HTTPS with its own CA for development.
- `caddy reload` applies config with no dropped
  connections.

## Watch out for

- Port 80 must be reachable for the HTTP challenge, or
  configure DNS-01.
- Run it under [[systemd]] so it survives reboots — the
  packaged install does this for you.

## Related

[[Reverse Proxy]] · [[Automatic HTTPS]] ·
[[ACME Protocol]] · [[Nginx]] · [[One-Box Deployment]]

## Sources

- [[caddy-quickstart-reverse-proxy]] ·
  [[caddy-automatic-https]] ·
  [[caddy-caddyfile-concepts]] · [[caddy-install]] ·
  [[caddy-running-service]] ·
  [[caddy-quickstart-static-files]]
