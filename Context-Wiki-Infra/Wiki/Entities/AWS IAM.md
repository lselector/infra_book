---
type: Service
title: "AWS IAM"
description: "Identity and access management on AWS - roles, policies, and the case against long-lived keys."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS IAM

Controls who and what may call which AWS API on which
resource. Every other AWS control rests on it.

## The practices that matter most

1. **Roles, not users, for workloads.** An
   [[Amazon EC2]] instance profile or an
   [[AWS Lambda]] execution role gives temporary
   credentials automatically — no access key stored
   anywhere. This removes an entire class of
   [[Secrets Management]] problem.
2. **MFA on every human**, and especially the root
   account — see [[Multi-Factor Authentication]].
3. **Lock the root account away.** Use it for the handful
   of tasks that require it and nothing else.
4. **Scope policies narrowly.** `Action: "*"` on
   `Resource: "*"` is where incidents begin. See
   [[Least Privilege]].
5. **No long-lived access keys** if a role will do; rotate
   them if it will not.

## Verifying rather than assuming

**IAM Access Analyzer** reports which permissions were
actually used over a period, and can generate a policy
from that activity. That turns least privilege from an
argument into evidence, and produces exactly the artefact
an [[Access Review]] wants.

It also flags resources shared outside the account — a
public bucket, a cross-account role — which is a cheap
way to catch a serious mistake.

## Related

[[Least Privilege]] · [[Access Review]] ·
[[Secrets Management]] · [[AWS CloudTrail]] ·
[[Shared Responsibility Model]] · [[AWS KMS]]

## Sources

- [[aws-iam-best-practices]] · [[aws-iam-access-analyzer]]
  · [[aws-well-architected-security-pillar]]
