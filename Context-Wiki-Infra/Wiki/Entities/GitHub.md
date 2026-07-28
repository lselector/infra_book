---
type: Service
title: "GitHub"
description: "Where the repository lives - and, through Actions and build integrations, the thing most deployments hang off."
wikipedia: "https://en.wikipedia.org/wiki/GitHub"
tags: [dev-environment, ops-and-security, deployments]
timestamp: "2026-07-27T00:00:00Z"
---

# GitHub

<https://github.com> — hosted [[Git]] repositories, pull
requests, issues, CI ([[GitHub Actions]]), and the
integration point [[Cloudflare Pages]] and every PaaS
([[Render]], [[Fly.io]], [[Railway]]) build from.

Free for private repositories, which is all a small
project needs. GitLab and Codeberg are equivalent
choices; the account matters more than the vendor.

## Securing the account

It is a deployment credential, not a social profile.
Treat it accordingly:

- [[Multi-Factor Authentication]] on, recovery codes in
  [[Bitwarden]].
- SSH key added from your machine (public key only —
  see [[SSH Key Authentication]]).
- Sign commits, or at least know that unsigned commits
  prove nothing about authorship.
- Review the OAuth apps and personal access tokens you
  have granted; delete what you no longer use
  ([[Least Privilege]]).

## Repository hygiene

- `.gitignore` covering `.env`, keys, build output and
  `node_modules/` from the first commit.
- **Secret scanning** and **push protection** on — they
  block a committed token before it reaches the remote.
- **[[Dependabot]]** alerts on, so you hear about a
  vulnerable dependency ([[Dependency Auditing]]).
- Branch protection on `main` once more than one person
  or agent is pushing.
- **Actions secrets** for deploy tokens, never in the
  workflow file.

## What connects to it

| Consumer | Effect of a push |
|---|---|
| [[Cloudflare Pages]] | Builds and deploys the site, with a preview URL per branch |
| [[GitHub Actions]] | Runs tests, builds, deploys ([[Continuous Integration and Delivery]]) |
| [[Render]] / [[Fly.io]] / [[Railway]] | Rebuilds and redeploys the app |
| Your VPS | `git pull` in a deploy script ([[Git-Driven Deployment]]) |

## Related

[[Development Setup]] · [[Git]] · [[GitHub Actions]] ·
[[Git-Driven Deployment]] · [[Dependabot]] ·
[[Secrets Management]] · [[SSH Key Authentication]]

## Sources

- Upstream documentation: <https://docs.github.com>.
  The Actions, secret-scanning and Dependabot material
  in the `Raw/` corpus is cited on
  [[GitHub Actions]] and [[Dependabot]]; this page has
  no capture of its own.
