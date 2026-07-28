---
type: Summary
title: "Kamal — configuration overview (deploy.yml)"
description: "Configuration is read from the config/deploy.yml."
resource: "https://kamal-deploy.org/docs/configuration/overview/"
source_file: "Raw/03_deployments/kamal-configuration.md"
tags: [deployments, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Kamal — configuration overview (deploy.yml)

Extractive digest of the immutable capture in
`Raw/03_deployments/kamal-configuration.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://kamal-deploy.org/docs/configuration/overview/>

## Opening

> Configuration is read from the `config/deploy.yml`.
> When running commands, you can specify a destination with the `-d` flag, e.g., `kamal deploy -d staging`.
> In this case, the configuration will also be read from `config/deploy.staging.yml` and merged with the base configuration.
> Kamal will not accept unrecognized keys in the configuration file.

## Contents of the source document

- Kamal Configuration
  - Destinations
  - Extensions
  - The service name
  - The Docker image name
  - Labels
  - Volumes
  - Registry
  - Servers
  - Environment variables
  - Asset path
  - Hooks path
  - Hook output
  - Secrets path
  - Error pages
  - Require destinations
  - Primary role
  - Allowing empty roles

## Related pages

[[Docker]] · [[HTTP]] · [[Kamal]]
