---
type: Reference
title: "MITRE ATT&CK"
description: "A free catalogue of how real attackers actually operate - the shared vocabulary for red and blue teams."
wikipedia: "https://en.wikipedia.org/wiki/ATT%26CK"
tags: [security, ops-and-security, compliance]
timestamp: "2026-07-28T00:00:00Z"
---

# MITRE ATT&CK

A public knowledge base of adversary behaviour,
maintained by MITRE, organised as **tactics** (the
attacker's goal) and **techniques** (how it is achieved),
each with real-world examples, detection guidance and
mitigations.

`ATT&CK` stands for Adversarial Tactics, Techniques and
Common Knowledge. It is free, versioned, and used as
common vocabulary by defenders, tool vendors and threat
reports.

## The shape of it

Tactics run roughly in attack order — Initial Access,
Execution, Persistence, Privilege Escalation, Defense
Evasion, Credential Access, Discovery, Lateral Movement,
Collection, Exfiltration, Impact — with dozens of
techniques under each, identified as `T1078` (Valid
Accounts), `T1190` (Exploit Public-Facing Application),
and so on. There are separate matrices for Enterprise,
Cloud, Containers and Mobile.

## How it differs from the other lists here

| Framework | Answers |
|---|---|
| [[OWASP Top 10]] | What flaws does my web app have? |
| **ATT&CK** | What would an attacker *do*, and would I see it? |
| CIS Controls ([[cis-controls-list]]) | What should I configure? |
| [[Trust Services Criteria]] | What must I prove to an auditor? |

ATT&CK is the behavioural one. OWASP describes the hole;
ATT&CK describes the intruder's path once they are
through it.

## Using it at small scale

You are not going to implement detection for 200
techniques. Pick the handful that match how a small SaaS
actually gets breached, and check you would notice each:

- **T1078 Valid Accounts** — a stolen credential used
  successfully. Do you alert on login from a new country
  or a new device? ([[Multi-Factor Authentication]] is
  the mitigation.)
- **T1190 Exploit Public-Facing Application** — an
  unpatched dependency ([[Dependency Auditing]]).
- **T1552 Unsecured Credentials** — a key in git history
  ([[Gitleaks]], [[Secrets Management]]).
- **T1098 Account Manipulation** — a new IAM user or
  policy nobody requested ([[Audit Logging]],
  [[AWS CloudTrail]]).
- **T1530 Data from Cloud Storage** — a bucket made
  public ([[Object Storage]], [[Least Privilege]]).

That short list makes a [[Red Team and Blue Team]]
exercise concrete, and the detection gaps it exposes are
the alerts worth building
([[Monitoring and Alerting]]).

## Related

[[Red Team and Blue Team]] · [[Penetration Testing]] ·
[[Security Testing]] · [[OWASP Top 10]] ·
[[Incident Response]] · [[Audit Logging]] ·
[[Monitoring and Alerting]] · [[Least Privilege]] ·
[[Multi-Factor Authentication]] · [[SOC 2]]

## Sources

- Upstream: <https://attack.mitre.org/>. Not part of the
  downloaded `Raw/` corpus — related captures:
  [[nist-incident-handling-guide]] ·
  [[cis-controls-list]] · [[owasp-top-ten]] ·
  [[aws-penetration-testing-policy]].
