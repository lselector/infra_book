---
type: Concept
title: "Micro-VMs"
description: "Servers that boot in milliseconds - the technology that makes scale-to-zero practical, and where it fits."
wikipedia: "https://en.wikipedia.org/wiki/Virtual_machine"
tags: [deployments, architectures, serverless]
timestamp: "2026-07-28T00:00:00Z"
---

# Micro-VMs

A micro-VM is a virtual machine stripped to the minimum
needed to run one application: no BIOS, no legacy device
emulation, a handful of virtual devices, a few megabytes
of memory overhead. It boots in **tens of milliseconds**
rather than the tens of seconds a general-purpose VM
takes.

That single number changes what is architecturally
possible. If a server can start faster than a user
notices, you no longer need it running while nobody is
using it.

## The spectrum of "how fast can a thing start"

| Unit | Typical start | Isolation |
|---|---|---|
| Virtual machine | 30–60 s | Hardware, strongest |
| **Micro-VM** ([[Firecracker]]) | **~125 ms** | Hardware, strongest |
| Container ([[Docker]]) | 0.5–2 s | Kernel namespaces |
| V8 isolate ([[Cloudflare Workers]]) | **< 5 ms** | Language runtime |
| Warm process | 0 ms | None |

Reading down the table, start time improves and isolation
weakens. Micro-VMs are notable because they are the only
row that gets both: a full kernel per tenant, at
container-like speed. That is why [[AWS Lambda]],
[[AWS Fargate]] and [[Fly.io]] are built on them.

## What it buys you

- **Scale to zero honestly.** Idle costs nothing, and the
  first request after idle is still fast enough to serve
  ([[Cold Starts]]).
- **Per-request or per-tenant isolation.** Untrusted code
  — customer builds, AI-generated code, user plugins —
  can have its own kernel, which containers cannot offer.
- **Density.** Thousands of micro-VMs per host, because
  the overhead is megabytes rather than hundreds.
- **Ephemeral by construction.** A machine that exists
  for one job cannot accumulate state, drift, or an
  unpatched package.

## Where it shows up in this wiki's stacks

You mostly *consume* this rather than run it. It is the
implementation underneath serverless platforms
([[Serverless Architecture]]) and the reason
[[Cloudflare Workers]], [[Google Cloud Run]] and
[[Fly.io]] machines can sit at zero and wake on a
request. Running [[Firecracker]] yourself is worth it
only when multi-tenant isolation is the product — a CI
runner, a sandbox for other people's code, a
function-as-a-service platform of your own.

## Watch out for

- **Fast start is not stateless.** The application still
  has to reconnect to the database on every cold start;
  see [[Connection Pooling]] and [[PgBouncer]] for why
  thousands of short-lived instances are hard on
  [[PostgreSQL]].
- **Boot time is not the whole latency.** 125ms to boot
  plus 2s of runtime initialisation is a 2.1s cold start
  — the platform's number is the floor, not your number.
- **Isolation claims deserve care.** "Container-based
  serverless" and "micro-VM-based serverless" have
  materially different security properties, and only one
  of them puts a kernel boundary between tenants.

## Related

[[Serverless Architecture]] · [[Cold Starts]] ·
[[Firecracker]] · [[Cloudflare Workers]] ·
[[Google Cloud Run]] · [[AWS Lambda]] ·
[[AWS Fargate]] · [[Fly.io]] · [[Docker]] ·
[[Containers in Production]] · [[WebAssembly]] ·
[[Cost Control]]

## Sources

- [[aws-what-is-serverless]] · [[aws-lambda-welcome]] ·
  [[aws-ecs-fargate]] · [[flyio-launch]] ·
  [[cloudflare-wrangler-workers-commands]]
