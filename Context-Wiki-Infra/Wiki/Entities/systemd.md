---
type: Tool
title: "systemd"
description: "The Linux service manager - what makes your app start on boot and restart when it dies."
tags: [deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# systemd

The init system on Ubuntu and most current Linux
distributions. For this book, the thing that supervises
your application process.

## A minimal unit

```ini
[Unit]
Description=My app
After=network.target

[Service]
User=app
WorkingDirectory=/srv/app
EnvironmentFile=/etc/app.env
ExecStart=/srv/app/venv/bin/uvicorn main:app --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

`Restart=always` is the line that turns a crash into a
blip. `User=app` keeps it off root, per
[[Least Privilege]].

## Why it matters here

Without a service manager, an app started in a terminal
dies with the SSH session and does not come back after a
reboot. This file is the difference between a demo and a
deployment.

## Useful specifics

- `EnvironmentFile` reads config without it entering the
  repository — see [[Secrets Management]].
- `LoadCredential` passes secrets to the process without
  exposing them in the environment.
- `journalctl -u app -f` is your log stream, which
  satisfies the [[Twelve-Factor App]] logging convention.

## Related

[[One-Box Deployment]] · [[Ubuntu Server]] ·
[[Secrets Management]] · [[Caddy]] ·
[[Monolithic Web App]]

## Sources

- [[systemd-service-unit]] · [[systemd-credentials]] ·
  [[caddy-running-service]]
