---
type: Summary
title: "Caddy — running as a systemd service"
description: "While Caddy can be run directly with its command line interface, there are numerous advantages to using a service manager to keep it running, such as ensuring it starts automatically when th"
resource: "https://caddyserver.com/docs/running"
source_file: "Raw/03_deployments/caddy-running-service.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Caddy — running as a systemd service

Extractive digest of the immutable capture in
`Raw/03_deployments/caddy-running-service.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://caddyserver.com/docs/running>

## Opening

> While Caddy can be run directly with its [command line interface](https://caddyserver.com/docs/command-line), there are numerous advantages to using a service manager to keep it running, such as ensuring it starts automatically when the system reboots and to capture stdout/stderr logs.
> The recommended way to run Caddy on Linux distributions with systemd is with our official systemd unit files.
> We provide two different systemd unit files that you can choose between, depending on your use case:
> They are very similar, but differ in the `ExecStart` and `ExecReload` commands to accommodate the workflows.

## Contents of the source document

- Keep Caddy Running
  - Linux Service
    - Unit Files
    - Manual Installation
    - Using the Service
    - Local HTTPS with systemd
    - Overrides
    - SELinux Considerations
  - Windows service
    - sc.exe
    - WinSW
  - Docker Compose
    - Setup
    - Usage
    - Local HTTPS with Docker

## Related pages

[[Caddy]] · [[Docker]] · [[Docker Compose]] · [[HTTP]] · [[systemd]]
