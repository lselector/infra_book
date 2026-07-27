---
type: Concept
title: "Multi-Factor Authentication"
description: "A second factor - the highest-value security control per unit of effort, starting with your own accounts."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Multi-Factor Authentication

Something you know plus something you have. Passwords
leak; a second factor makes the leak insufficient.

## Where to enable it first

Before your application supports it at all, enable it on
the accounts that can destroy you:

1. Your domain registrar — losing the domain loses
   everything.
2. Your cloud root account.
3. Your GitHub account.
4. Your email — the reset path for all of the above.

## In your own application

Delegate it. [[Firebase Authentication]] and its peers
support TOTP and SMS factors as configuration. Prefer TOTP
or passkeys over SMS, which is vulnerable to SIM swapping.

## Why it matters here

It appears in essentially every security questionnaire and
in the common criteria of [[Trust Services Criteria]]. It
is also, straightforwardly, the control most likely to
prevent an actual compromise of your infrastructure.

## Related

[[Authentication]] · [[Least Privilege]] ·
[[Access Review]] · [[SOC 2]]

## Sources

- [[owasp-authentication-cheatsheet]] ·
  [[firebase-auth-manage-users]] · [[cis-controls-list]]
