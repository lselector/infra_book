---
type: Concept
title: "Penetration Testing"
description: "A human attacking your system on purpose - what it finds that scanners cannot, and when to buy one."
wikipedia: "https://en.wikipedia.org/wiki/Penetration_test"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Penetration Testing

An engagement in which a skilled person attempts to
compromise your system, with permission and within an
agreed scope.

## What it finds that automation does not

Business-logic flaws. A scanner cannot know that
discounting is meant to stop at 100%, that a user should
not be able to invite themselves to another tenant, or
that the password reset token is predictable. Those are
the findings worth paying for.

## When it is worth the money

- An enterprise customer requires one, often as part of
  [[SOC 2]] evidence.
- You handle payments or genuinely sensitive data.
- Before a significant architectural change goes live.

Not before you have done the free work: a
[[Security Testing]] pass and [[Dependency Auditing]]
first, so the tester spends their time on logic rather
than on missing headers.

## Before you start

- Written authorisation, with scope and dates.
- Check the provider's policy — see the AWS penetration
  testing policy for what is permitted without prior
  approval.
- A staging environment that mirrors production.

## Related

[[Security Testing]] · [[OWASP Top 10]] · [[SOC 2]] ·
[[Incident Response]]

## Sources

- [[aws-penetration-testing-policy]] · [[owasp-wstg]] ·
  [[portswigger-web-security-academy]]
