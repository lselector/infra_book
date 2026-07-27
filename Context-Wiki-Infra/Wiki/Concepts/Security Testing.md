---
type: Concept
title: "Security Testing"
description: "Finding your own vulnerabilities first - the scan, the audit and the manual pass before launch."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Security Testing

Deliberately looking for weaknesses in your own system,
on a schedule, with tools.

## A pre-launch pass, in order

1. **TLS and headers.** Check the certificate chain and
   the [[Security Headers]] set. Minutes.
2. **[[Dependency Auditing]].** `npm audit`, `pip-audit`,
   or [[Dependabot]] in CI.
3. **Dynamic scan.** An [[OWASP ZAP]] baseline scan
   against a staging URL — it crawls and reports passively
   in a few minutes and runs happily in
   [[Continuous Integration and Delivery]].
4. **Server audit.** [[Lynis]] on the box, to catch what
   [[Linux Server Hardening]] missed.
5. **Container and IaC scan.** [[Trivy]], if you use them.
6. **Manual access-control review.** Log in as user A and
   try to reach user B's records. No tool finds this.
7. **Fix, then re-test.** The re-test is the step people
   skip.

## The authorisation point

Only test systems you own or are contracted to test.
Cloud providers publish policies on this — see the AWS
penetration testing policy — and scanning infrastructure
you do not own is both a contract breach and, in many
jurisdictions, an offence.

## Related

[[OWASP Top 10]] · [[Dependency Auditing]] ·
[[Penetration Testing]] · [[OWASP ZAP]] ·
[[Security Headers]]

## Sources

- [[owasp-wstg]] · [[owasp-wstg-stable]] ·
  [[zap-getting-started]] · [[zap-docker-baseline-scan]] ·
  [[lynis-readme]] · [[aws-penetration-testing-policy]]
