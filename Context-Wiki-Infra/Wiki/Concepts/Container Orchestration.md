---
type: Concept
title: "Container Orchestration"
description: "Scheduling containers across machines - what you take on when one box stops being enough."
wikipedia: "https://en.wikipedia.org/wiki/Orchestration_(computing)"
tags: [architectures, deployments, scaling]
timestamp: "2026-07-28T00:00:00Z"
---

# Container Orchestration

Running containers on *one* machine is
[[Containers in Production]]: `docker compose up`, and
you are done. Orchestration is what the word means when
there is more than one machine — something has to decide
which container runs where, restart the ones that die,
roll new versions out without dropping traffic, and give
them a way to find each other.

## What an orchestrator actually gives you

| Job | Why it matters |
|---|---|
| **Scheduling** | Place containers on machines with room, and move them when a machine dies |
| **Health and restart** | A crashed container comes back without a human |
| **Rolling deploys** | New version in, old version out, no downtime, with a rollback |
| **Service discovery** | `api` resolves to whichever instances are alive right now |
| **Horizontal scale** | Three replicas of the web tier, one of the worker, per-service |
| **Secrets and config** | Injected at run time, not baked into the image |

## The options, cheapest first

- **[[Docker Compose]] on one box** — not orchestration,
  and right for most of this wiki. Restart policies and
  a `deploy.sh` cover more than people admit.
- **[[AWS Fargate]] / Cloud Run / [[Fly.io]]** — you
  hand over a container image and a count. No cluster to
  patch. This is the rung most teams should stop at.
- **[[Kubernetes]]** — genuinely powerful, genuinely a
  second full-time system. Managed control planes (EKS,
  GKE, DOKS) remove the hardest part and none of the
  conceptual weight.

## The prerequisite nobody enjoys

Orchestration only works on stateless containers. Before
you can schedule freely you need session state out of
process (see [[Sticky Sessions]]), uploads in
[[Object Storage]], the database managed elsewhere, and
config in the environment ([[Twelve-Factor App]]).
Skipping that step is how people end up with a
Kubernetes cluster running one pod they are afraid to
restart.

## Watch out for

- **Cost.** A minimum-viable cluster with redundancy
  starts around $150–300/month before your app.
- **The YAML surface.** Deployments, services, ingresses,
  config maps, secrets — each a place to be wrong.
- **Debugging distance.** `ssh` and `tail -f` become
  `kubectl logs` across ephemeral pods; you need
  [[Monitoring and Alerting]] before you need this.

**Climb when:** you have several services in different
languages, or scale-to-fit-load is a real requirement —
not because containers are on your CV.

## Related

[[Containers in Production]] · [[Docker]] ·
[[Docker Compose]] · [[Kubernetes]] · [[AWS Fargate]] ·
[[Sticky Sessions]] · [[Twelve-Factor App]] ·
[[Infrastructure as Code]] · [[Anti-Patterns]]

## Sources

- [[docker-compose-production]] · [[kubernetes-overview]]
