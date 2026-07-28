---
type: Tool
title: "Certbot"
description: "The EFF's ACME client - how Nginx and Apache get Let's Encrypt certificates."
wikipedia: "https://en.wikipedia.org/wiki/Let's_Encrypt"
tags: [deployments, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Certbot

A command-line ACME client that obtains certificates from
[[Let's Encrypt]] and can configure [[Nginx]] or Apache to
use them.

## Typical use

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

This validates the domains, writes the certificate files,
edits the server config, and installs a systemd timer for
renewal.

## Verify renewal, do not assume it

```bash
sudo certbot renew --dry-run
```

Run this after setup. A renewal that fails silently is
discovered by your users, 90 days later, at a weekend.

## Watch out for

- The `--nginx` plugin edits your configuration. Know what
  it changed.
- Renewal needs the same challenge path to still work —
  a later config change that intercepts
  `/.well-known/` breaks it.

## The alternative

[[Caddy]] makes Certbot unnecessary by doing this
internally. If you are choosing rather than inheriting,
that is the simpler path.

## Related

[[Let's Encrypt]] · [[ACME Protocol]] · [[Nginx]] ·
[[Automatic HTTPS]]

## Sources

- [[certbot-using]] · [[letsencrypt-getting-started]]
