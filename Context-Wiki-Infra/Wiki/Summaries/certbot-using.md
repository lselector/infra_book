---
type: Summary
title: "Certbot — user guide"
description: "Certbot uses a number of different commands (also referred to as “subcommands”) to request specific actions such as obtaining, renewing, or revoking certificates."
resource: "https://eff-certbot.readthedocs.io/en/stable/using.html"
source_file: "Raw/03_deployments/certbot-using.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Certbot — user guide

Extractive digest of the immutable capture in
`Raw/03_deployments/certbot-using.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://eff-certbot.readthedocs.io/en/stable/using.html>

## Opening

> Certbot uses a number of different commands (also referred to as “subcommands”) to request specific actions such as obtaining, renewing, or revoking certificates. The most important and commonly-used commands will be discussed throughout this document; an exhaustive list also appears near the end ...
> The `certbot` script on your web server might be named `letsencrypt` if your system uses an older package. Throughout the docs, whenever you see `certbot`, swap in the correct name as needed.
> Certbot helps you achieve two tasks:
> 1. Obtaining a certificate: automatically performing the required authentication steps to prove that you control the domain(s), saving the certificate to `/etc/letsencrypt/live/` and renewing it on a regular schedule.

## Contents of the source document

- User Guide
  - Certbot Commands
  - Getting certificates (and choosing plugins)
    - Apache
    - Webroot
    - Nginx
    - Standalone
    - DNS Plugins
    - Manual
    - Combining plugins
    - Third-party plugins
  - Managing certificates
    - Re-creating and Updating Existing Certificates
    - Changing a Certificate’s Domains
    - RSA and ECDSA keys
    - Revoking certificates
    - Deleting certificates
    - Renewing certificates

## Related pages

[[ACME Protocol]] · [[Authentication]] · [[Authorization]] · [[Certbot]] · [[Cloudflare]] · [[DigitalOcean]] · [[Docker]] · [[Hetzner Cloud]] · [[Homebrew]] · [[Let's Encrypt]] · [[Nginx]] · [[systemd]]
