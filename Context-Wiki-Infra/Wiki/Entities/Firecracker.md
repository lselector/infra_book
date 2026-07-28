---
type: Tool
title: "Firecracker"
description: "Amazon's open-source micro-VM monitor - the thing under Lambda and Fargate that boots a VM in ~125 ms."
wikipedia: "https://en.wikipedia.org/wiki/Firecracker_(software)"
tags: [deployments, serverless, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Firecracker

An open-source virtual machine monitor written in
[[Rust]], built at AWS to run serverless workloads. It
creates **micro-VMs**: minimal virtual machines with a
handful of emulated devices, an in-process API, and a
memory overhead measured in single-digit megabytes.

Published figures: boot to application code in about
**125 ms**, and up to **150 micro-VMs per second per
host**.

## Why it exists

[[AWS Lambda]] needs to run many customers' code on
shared hardware. Containers alone share a kernel, which
is a weaker boundary than a multi-tenant platform wants;
full VMs are too slow and too heavy to start per
invocation. Firecracker is the answer: hardware
virtualisation with the startup cost of a container.

It now runs [[AWS Lambda]] and [[AWS Fargate]], and
outside AWS it powers [[Fly.io]] machines and a number
of CI and code-sandbox providers.

## How it achieves it

- **Minimal device model** — virtio block, net, vsock, a
  serial console. No BIOS, no PCI, no legacy emulation.
- **KVM** for the actual virtualisation; Firecracker is
  the userspace monitor around it.
- **One process per micro-VM**, controlled over a REST
  API on a Unix socket, and confined by a jailer with
  seccomp filters and cgroups.
- **Rust**, chosen for memory safety in code that sits
  directly on the tenant boundary.

## When you would run it yourself

When **isolating other people's code is your product**:
a CI runner, a sandbox for AI-generated or user-supplied
code, a function platform, a per-customer preview
environment. Then the kernel boundary is worth operating.

For running *your own* application, this is the wrong
layer. You want a platform built on it —
[[AWS Lambda]], [[Fly.io]], [[Google Cloud Run]] — or
plain [[Docker Compose]] on a VPS. Firecracker gives you
a bare VM: you supply the kernel, the root filesystem,
the networking and the orchestration.

## Watch out for

- **Linux and KVM only**, on x86-64 or arm64 with nested
  virtualisation available. It does not run on most
  laptops without help, and not inside most VMs.
- **No orchestration included.** Scheduling, networking,
  images and lifecycle are yours to build.
- Related tools solve adjacent problems: **gVisor**
  intercepts syscalls in userspace instead of using a
  VM, and **Kata Containers** wraps OCI containers in
  micro-VMs with a container-shaped interface.

## Related

[[Micro-VMs]] · [[Cold Starts]] ·
[[Serverless Architecture]] · [[AWS Lambda]] ·
[[AWS Fargate]] · [[Fly.io]] · [[Rust]] ·
[[Docker]] · [[Containers in Production]] ·
[[Container Orchestration]]

## Sources

- Upstream documentation:
  <https://firecracker-microvm.github.io/>. Not part of
  the downloaded `Raw/` corpus — the platforms built on
  it are: [[aws-lambda-welcome]] · [[aws-ecs-fargate]] ·
  [[flyio-launch]].
