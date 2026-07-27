---
type: Summary
title: "systemd — passing credentials to services (LoadCredential)"
description: "The systemd service manager supports a “credential” concept for securely acquiring and passing credential data to systems and services."
resource: "https://systemd.io/CREDENTIALS/"
source_file: "Raw/05_ops_cicd_security/systemd-credentials.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# systemd — passing credentials to services (LoadCredential)

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/systemd-credentials.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://systemd.io/CREDENTIALS/>

## Opening

> The `systemd` service manager supports a “credential” concept for securely acquiring and passing credential data to systems and services. The precise nature of the credential data is up to applications, but the concept is intended to provide systems and services with potentially security sensitive ...
> Traditionally, data of this nature has often been provided to services via environment variables (which is problematic because by default they are inherited down the process tree, have size limitations, and issues with binary data) or simple, unencrypted files on disk. `systemd`’s system and ...
> 1. Service credentials are acquired at the moment of service activation, and released on service deactivation. They are immutable during the service runtime.
> 2. Service credentials are accessible to service code as regular files, the path to access them is derived from the environment variable `$CREDENTIALS_DIRECTORY`.

## Contents of the source document

- System and Service Credentials
  - Configuring per-Service Credentials
  - Programming Interface from Service Code
  - Programming Interface from Generator Code
  - Tools
  - Encryption
  - Acquisition from Cloud Instance Metadata Services (IMDS)
  - Well-Known Credentials
  - Relevant Paths
  - Conditionalizing Services

## Related pages

[[Authentication]] · [[systemd]]
