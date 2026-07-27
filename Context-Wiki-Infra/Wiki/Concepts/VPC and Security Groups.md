---
type: Concept
title: "VPC and Security Groups"
description: "The minimal network mental model - private subnets, and firewalls attached to instances."
tags: [storage-and-databases, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# VPC and Security Groups

A VPC is your private network in the cloud. Security
groups are stateful firewalls attached to resources inside
it.

## The minimum model

- **Public subnet** — things with a public IP: the
  [[Reverse Proxy]], a load balancer.
- **Private subnet** — things without: the database,
  internal workers.
- **Security group** — allow the proxy to reach the app
  port, allow the app to reach the database port, deny
  everything else. Reference groups by name rather than
  by IP range.

## Why it matters here

On a single VPS you get most of this benefit for free by
binding services to `127.0.0.1` and running [[UFW]] — the
concept is identical, the implementation simpler. The VPC
vocabulary becomes necessary once components live on
separate machines.

## Watch out for

- `0.0.0.0/0` on a database port. This is how databases
  end up in breach reports.
- NAT gateways are a real and often surprising line on an
  AWS bill.

## Related

[[Linux Server Hardening]] · [[UFW]] · [[Amazon VPC]] ·
[[Least Privilege]]

## Sources

- [[aws-what-is-vpc]] · [[aws-vpc-security-groups]] ·
  [[aws-vpc-subnets]]
