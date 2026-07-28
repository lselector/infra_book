---
type: Concept
title: "OWASP Top 10 for LLM Applications"
description: "The ten risks specific to shipping an LLM feature, and which page in this wiki covers each one."
wikipedia: "https://en.wikipedia.org/wiki/OWASP"
tags: [ai-in-saas, ops-and-security, security]
timestamp: "2026-07-28T00:00:00Z"
---

# OWASP Top 10 for LLM Applications

A companion list to the [[OWASP Top 10]], produced by
[[OWASP]]'s Gen AI project, covering the risks that only
appear once a model is part of the product. It is short,
free, and specific enough to use as a launch checklist.

It does not replace the web Top 10. An AI feature is
still a web feature, and still has all the ordinary ways
to be broken.

## The 2025 list, and where it lands here

| # | Risk | Covered by |
|---|---|---|
| 01 | Prompt injection | [[Prompt Injection]] |
| 02 | Sensitive information disclosure | [[Multi-Tenant SaaS]], [[Encryption at Rest]] |
| 03 | Supply chain | [[Dependency Auditing]], [[Model Context Protocol]] |
| 04 | Data and model poisoning | [[Retrieval-Augmented Generation]] |
| 05 | Improper output handling | [[Security Headers]], [[OWASP Top 10]] |
| 06 | Excessive agency | [[Tool Calling]], [[Least Privilege]] |
| 07 | System prompt leakage | [[Prompt Injection]] |
| 08 | Vector and embedding weaknesses | [[Retrieval-Augmented Generation]] |
| 09 | Misinformation | below |
| 10 | Unbounded consumption | [[Rate Limiting]], [[Usage Quotas and Metering]] |

## The four that catch small teams

**Excessive agency (06).** The assistant was given a tool
that does more than the task requires — a database
connection instead of one query, write access instead of
read. The fix is scoping, not prompting.

**Improper output handling (05).** Model output rendered
as HTML, passed to a shell, or interpolated into SQL.
Every injection class you already defend against comes
back, now with a generator that produces plausible
payloads on request.

**Unbounded consumption (10).** No cap on requests,
tokens or context size, so cost scales with the
attacker's patience. This is the one that shows up on an
invoice rather than in a breach report, and it is the
most likely to actually happen to you.

**Misinformation (09).** The model states something
false with complete confidence and a user acts on it.
Mitigate in the product, not the prompt: ground answers
in retrieved sources, show citations, mark the output as
AI-generated, and keep a human between the assistant and
any consequential decision.

## Using it

Run through the ten before launch, the same way as the
pre-launch pass in [[Security Testing]]: for each item,
write down the control and the file it lives in. Items
with no control are your backlog.

For governance rather than engineering — who signed off,
how the risk was assessed, what is monitored after launch
— the companion document is the
[[NIST AI Risk Management Framework]]. Enterprise
security questionnaires increasingly ask about both, and
they arrive at the same time as the [[SOC 2]] questions.

## Related

[[Prompt Injection]] · [[Tool Calling]] ·
[[Rate Limiting]] · [[Usage Quotas and Metering]] ·
[[Retrieval-Augmented Generation]] · [[OWASP Top 10]] ·
[[OWASP]] · [[Security Testing]] ·
[[NIST AI Risk Management Framework]] ·
[[AI Assistant Panel]]

## Sources

- [[owasp-llm-top-ten]] ·
  [[owasp-llm-prompt-injection-cheatsheet]] ·
  [[owasp-top-ten]] · [[owasp-asvs]] · [[nist-ai-rmf]]
