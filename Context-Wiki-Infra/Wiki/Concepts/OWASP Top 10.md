---
type: Concept
title: "OWASP Top 10"
description: "The consensus list of the most critical web application risks - a checklist, not a syllabus."
wikipedia: "https://en.wikipedia.org/wiki/OWASP"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP Top 10

A periodically updated ranking of the most serious and
prevalent web application security risks, maintained by
the Open Worldwide Application Security Project.

## The ones that bite small projects hardest

- **Broken access control.** Users reaching objects that
  are not theirs — see [[Authorization]].
- **Cryptographic failures.** Plaintext transport, weak or
  home-made encryption — see [[Encryption in Transit]].
- **Injection.** Untrusted input concatenated into a
  query. Parameterised queries solve it entirely.
- **Security misconfiguration.** Default credentials, a
  debug endpoint left on, an open bucket.
- **Vulnerable components.** Outdated dependencies — see
  [[Dependency Auditing]].
- **Identification and authentication failures** — see
  [[Authentication]].

## How to use it

As a review checklist before launch, not as reading. If
the product includes an AI feature, run the companion
[[OWASP Top 10 for LLM Applications]] beside it — that
list covers the risks this one does not, and neither
replaces the other. Pair both
with a [[Security Testing]] pass: the scanner finds
misconfiguration and known-vulnerable components; the list
reminds you to check access control by hand, because no
scanner can.

## Related

[[Security Testing]] · [[Authorization]] ·
[[Dependency Auditing]] · [[Security Headers]] ·
[[Penetration Testing]] ·
[[OWASP Top 10 for LLM Applications]]

## Sources

- [[owasp-top-ten]] · [[owasp-asvs]] ·
  [[owasp-sql-injection-prevention]] ·
  [[owasp-xss-prevention]] · [[owasp-csrf-prevention]] ·
  [[owasp-input-validation-cheatsheet]]
