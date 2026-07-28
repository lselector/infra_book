---
type: Concept
title: "Deployment Environments"
description: "Production, staging and previews - how many you need, and when a second one starts paying for itself."
wikipedia: "https://en.wikipedia.org/wiki/Deployment_environment"
tags: [ops-and-security, scaling]
timestamp: "2026-07-27T00:00:00Z"
---

# Deployment Environments

Separate running copies of the system for separate
purposes.

## How many you actually need

- **One (production).** Correct for a static site with
  preview deployments, which [[Cloudflare Pages]] gives
  per branch for free.
- **Two (production + staging).** Worth it once a bad
  deploy costs real money, or once migrations are
  irreversible.
- **Per-pull-request previews.** Worth it once more than
  one person is reviewing.

## What must differ between them

- Separate databases. Always. A staging job pointed at the
  production database is a career-defining incident.
- Separate credentials — see [[Secrets Management]].
- Separate third-party accounts in test mode: [[Stripe]]
  test keys, [[Amazon SES]] sandbox.

## What must not differ

The database engine and the deployment mechanism.
[[Twelve-Factor App]] calls this dev/prod parity, and
violating it is how you get bugs that only exist in
production.

## Related

[[Continuous Integration and Delivery]] ·
[[Git-Driven Deployment]] · [[Secrets Management]] ·
[[Twelve-Factor App]] · [[Deployment Strategies]] ·
[[Automated Testing]] · [[Chaos Engineering]]

## Sources

- [[github-environments]] ·
  [[cloudflare-pages-preview-deployments]]
