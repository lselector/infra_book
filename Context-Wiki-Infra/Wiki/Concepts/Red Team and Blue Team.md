---
type: Concept
title: "Red Team and Blue Team"
description: "Attackers and defenders as roles, not job titles - what an exercise proves, and the version a tiny team can run."
wikipedia: "https://en.wikipedia.org/wiki/Red_team"
tags: [ops-and-security, security, compliance]
timestamp: "2026-07-28T00:00:00Z"
---

# Red Team and Blue Team

Two roles in a security exercise, borrowed from military
wargaming.

- **Red team** — attacks, without telling the defenders
  how or when. Goal: achieve a specific objective (read
  the customer table, get into production, obtain a
  domain admin credential).
- **Blue team** — defends, detects and responds, usually
  without knowing an exercise is running.
- **Purple team** — the two working together in the open,
  attacking and tuning detection in the same room. For a
  small organisation this is nearly always the right
  format: you learn the same lessons in a day instead of
  a quarter.

## Red team vs penetration test

They are commonly confused and answer different
questions.

| | [[Penetration Testing]] | Red team |
|---|---|---|
| Question | *What vulnerabilities exist?* | *Would we notice and stop a real attack?* |
| Scope | An agreed system, broad coverage | An objective, any route to it |
| Defenders know? | Yes | No |
| Stealth | Not required | Central to the exercise |
| Output | A findings list | A narrative and a detection timeline |
| Typical cost | Thousands | Tens of thousands |

A red team engagement tests **the blue team**, not the
software. Buying one before you have a pen test, logging
and alerting is paying to be told you have no detection —
which you already know.

## What the blue team actually needs

The exercise is only meaningful if there is something to
detect with:

- **Logs that exist and are kept** — auth attempts,
  admin actions, deploys ([[Audit Logging]]).
- **Alerts on the things that matter**: failed logins in
  bulk, a new IAM user, a login from a new country, a
  changed security group ([[Monitoring and Alerting]]).
- **A runbook and a person on call**
  ([[Incident Response]]).
- **The basics closed off first**: MFA, [[Least Privilege]],
  [[SSH Key Authentication]], patched dependencies
  ([[Dependency Auditing]]).

## The version a small team can run this month

Two hours, two people, no budget:

1. Pick one objective: *"read a row from the production
   users table from outside the office."*
2. One person attacks for 90 minutes, from a documented
   IP, in writing, with permission. Try the obvious: a
   leaked key in git history ([[Gitleaks]]), a default
   credential, an exposed admin path, a password reset
   flaw, an S3 bucket left public.
3. The other person watches the logs and writes down
   **what they saw and when**.
4. Compare the two timelines. The gap between "what
   happened" and "what was visible" is the finding, and
   it is usually large.
5. Add one alert that would have closed the gap. Repeat
   next quarter.

Written authorisation, agreed scope and dates, and no
testing of anything you do not own — the same rules as
[[Security Testing]]. Cloud providers publish what is
permitted; read that policy first.

## Frameworks worth borrowing

[[MITRE ATT&CK]] catalogues real attacker techniques, so
both sides can be specific: "can we detect T1078, valid
accounts?" beats "can we detect hackers?". For compliance
work, [[SOC 2]] does not require a red team, but it does
require evidence that you detect and respond — which is
what the exercise produces.

## Related

[[Penetration Testing]] · [[Security Testing]] ·
[[Fuzz Testing]] · [[MITRE ATT&CK]] ·
[[Incident Response]] · [[Audit Logging]] ·
[[Monitoring and Alerting]] · [[OWASP Top 10]] ·
[[Least Privilege]] · [[SOC 2]] ·
[[Chaos Engineering]] · [[Gitleaks]]

## Sources

- [[aws-penetration-testing-policy]] · [[owasp-wstg]] ·
  [[portswigger-web-security-academy]] ·
  [[nist-incident-handling-guide]] · [[cis-controls-list]]
