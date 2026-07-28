---
type: Tool
title: "OWASP ZAP"
description: "A free web application scanner that runs happily in CI."
wikipedia: "https://en.wikipedia.org/wiki/ZAP_(software)"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP ZAP

An open-source dynamic application security testing tool:
an intercepting proxy, a spider, and passive and active
scanners.

## The two ways to use it

- **Baseline scan**, in Docker, against a staging URL. It
  spiders the site and reports passively — no attack
  traffic — in a few minutes. Safe to run on every build
  in [[Continuous Integration and Delivery]].
- **Desktop, interactively**, proxying your browser while
  you use the application, then actively scanning specific
  requests. This is where it finds more.

## What it reliably catches

Missing [[Security Headers]], cookie flags, information
disclosure, mixed content, obvious injection points, and
outdated client-side libraries.

## What it cannot catch

Business-logic and access-control flaws. No scanner knows
that user A should not see user B's invoice — that is the
manual step in [[Security Testing]] and the reason for
[[Penetration Testing]].

## Watch out for

Active scanning is real attack traffic. Never point it at
production or at systems you do not own — see the AWS
penetration testing policy.

## Related

[[Security Testing]] · [[OWASP]] · [[OWASP Top 10]] ·
[[Security Headers]] ·
[[Continuous Integration and Delivery]]

## Sources

- [[zap-getting-started]] · [[zap-docker-baseline-scan]] ·
  [[zap-desktop-getting-started]] ·
  [[aws-penetration-testing-policy]]
