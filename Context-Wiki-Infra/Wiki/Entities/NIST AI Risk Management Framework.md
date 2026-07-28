---
type: Reference
title: "NIST AI Risk Management Framework"
description: "The voluntary governance framework enterprise buyers ask about - Govern, Map, Measure, Manage."
wikipedia: "https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology"
tags: [ai-in-saas, compliance, ops-and-security]
timestamp: "2026-07-28T00:00:00Z"
---

# NIST AI Risk Management Framework

A voluntary framework published by the US National
Institute of Standards and Technology (AI RMF 1.0, 2023)
for identifying and managing the risks of AI systems.
Free, sector-neutral, and written for organisations
rather than for engineers.

Where the [[OWASP Top 10 for LLM Applications]] tells you
what to fix in the code, this tells you who decided to
ship it, on what evidence, and what happens after.

## The four functions

| Function | The question it answers |
|---|---|
| **Govern** | Who owns AI risk here, and under what policy? |
| **Map** | What is this system for, who does it affect, what could go wrong? |
| **Measure** | How do we test it, and what do we track once it is live? |
| **Manage** | What do we do about what we found, and in what order? |

Govern runs through the other three rather than beside
them. There is a companion Generative AI Profile that
applies the same structure to LLM-specific risks.

## Why a small team should care

Not because anyone is compelled to adopt it. Because the
moment your product has an AI feature, enterprise
security questionnaires acquire an AI section, and the
answers it wants are governance answers: what the feature
does, what data it sends where, who reviewed it, how you
monitor it, and how a customer opts out.

For a small team that is a one-page document, not a
programme:

- The feature, its purpose, and its limits in plain
  language.
- What data leaves your systems, to which provider,
  under what retention ([[Shared Responsibility Model]]).
- The controls: [[Rate Limiting]],
  [[Usage Quotas and Metering]], [[Audit Logging]],
  human confirmation on writes ([[Tool Calling]]).
- What is monitored, and who is paged
  ([[Monitoring and Alerting]]).
- Who approved it, and when it gets re-reviewed
  ([[Access Review]] happens on the same cadence).

Written once, it answers most of the questionnaire and
slots into the evidence you already collect for
[[SOC 2]]. The EU AI Act and similar regimes ask for
recognisably the same material, so the effort is not
single-use.

## Watch out for

- **It is a framework, not a checklist.** There is no
  certificate and no pass mark; claiming "NIST compliant"
  is a claim about nothing.
- **Do not let it become the work.** For a five-person
  team the page above is proportionate; a risk register
  with forty rows is not.
- **Model changes are changes.** Swapping the model
  changes behaviour, cost and failure modes — that is a
  Map/Measure event, not just a deploy
  ([[Continuous Integration and Delivery]]).

## Related

[[OWASP Top 10 for LLM Applications]] · [[SOC 2]] ·
[[Trust Services Criteria]] · [[Prompt Injection]] ·
[[Usage Quotas and Metering]] · [[Audit Logging]] ·
[[Incident Response]] · [[Security Testing]] ·
[[Shared Responsibility Model]]

## Sources

- [[nist-ai-rmf]] · [[owasp-llm-top-ten]] ·
  [[nist-incident-handling-guide]] ·
  [[aicpa-soc2-overview]] · [[cis-controls-list]]
