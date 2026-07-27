---
type: Summary
title: "Docker Compose — using secrets in services"
description: "A secret is any piece of data, such as a password, certificate, or API key, that shouldn’t be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source"
resource: "https://docs.docker.com/compose/how-tos/use-secrets/"
source_file: "Raw/05_ops_cicd_security/docker-compose-secrets.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Docker Compose — using secrets in services

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/docker-compose-secrets.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.docker.com/compose/how-tos/use-secrets/>

## Opening

> A secret is any piece of data, such as a password, certificate, or API key, that shouldn’t be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.
> Docker Compose provides a way for you to use secrets without having to use environment variables to store information. If you’re injecting passwords and API keys as environment variables, you risk unintentional information exposure. Services can only access secrets when explicitly granted by a ...
> Environment variables are often available to all processes, and it can be difficult to track access. They can also be printed in logs when debugging errors without your knowledge. Using secrets mitigates these risks.
> Secrets are mounted as a file in `/run/secrets/<secret_name>` inside the container.

## Contents of the source document

- Manage secrets securely in Docker Compose
  - Use secrets
  - Examples
    - Single-service secret injection
    - Multi-service secret sharing and password management
    - Build secrets
  - Resources

## Related pages

[[Docker]] · [[Docker Compose]]
