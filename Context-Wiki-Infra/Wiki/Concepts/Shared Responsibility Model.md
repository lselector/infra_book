---
type: Concept
title: "Shared Responsibility Model"
description: "Which security controls your cloud provider owns and which remain yours - the question every audit asks."
tags: [ops-and-security, compliance]
timestamp: "2026-07-27T00:00:00Z"
---

# Shared Responsibility Model

Cloud providers secure the infrastructure *of* the cloud;
you secure what you put *in* it. The dividing line moves
with the service model.

## Where the line falls

| You run | Provider covers | You still own |
|---|---|---|
| IaaS ([[Amazon EC2]]) | hardware, hypervisor, network | OS patching, firewall, app, data |
| PaaS ([[Render]]) | + OS and runtime | app, data, access control |
| Serverless ([[AWS Lambda]]) | + execution environment | code, IAM, data |
| SaaS ([[Stripe]]) | almost everything | your account's access control |

In every row, **identity, access control and your data
stay yours**.

## Why it matters here

- It decides what a [[SOC 2]] auditor asks *you* about.
  Physical security of the data centre is inherited from
  the provider's own report, obtainable through
  [[AWS Artifact]]; access reviews and encryption
  configuration are not.
- It explains why moving up [[The Ladder]] increases the
  compliance burden — each rung down the stack you take
  over is a control you must now evidence.

## Watch out for

Assuming "the provider encrypts it" is sufficient.
Provider-managed encryption at rest is real, but key
custody, access policy and backups remain your decisions.

## Related

[[SOC 2]] · [[Trust Services Criteria]] ·
[[Least Privilege]] · [[Encryption at Rest]] ·
[[Cloud Service Models]]

## Sources

- [[aws-soc-faqs]] · [[aws-artifact-what-is]] ·
  [[gcp-soc2-compliance]] ·
  [[aws-well-architected-security-pillar]]
