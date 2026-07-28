---
type: Concept
title: "VPS Instead of Hyperscaler"
description: "Running the same small app on a rented Linux box instead of AWS - what it saves, what it costs you, and the tools that close the ergonomics gap."
wikipedia: "https://en.wikipedia.org/wiki/Virtual_private_server"
tags: [deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# VPS Instead of Hyperscaler

Most small apps do not need AWS. They need a Linux box
with a public IP, and a way to get code onto it without
ceremony. That is a $5–20/month decision rather than a
$150–400/month one, and for rungs 5 through 9 of
[[The Ladder]] it is usually the right one.

This page is the *why and how*. [[One-Box Deployment]] is
the shape of the resulting stack.

## Where the hyperscaler bill actually comes from

The instance is rarely the expensive part. On AWS a
minimal "production-shaped" footprint accumulates:

| Line item | Rough US monthly cost |
|---|---|
| Small EC2 instance | $10–20 |
| Application Load Balancer | ~$18 base, before traffic |
| NAT Gateway (if private subnets) | ~$32, before traffic |
| Managed RDS Postgres, smallest | $15–30 |
| Egress at $0.08–0.09/GB | grows with success |

None of those are unreasonable prices for what they are.
The point is that four of the five have no line item at
all on a VPS: the box has a public IP, a firewall, a
reverse proxy you run yourself, a database on the same
disk, and traffic included in the monthly price.

Treat the numbers above as order-of-magnitude — check the
current calculator before quoting them at anyone. The
ratio is the durable part, not the digits.

## What you are actually giving up

Be honest about this before you move:

- **Managed database failover.** RDS multi-AZ fails over
  for you. Your box does not. See [[Database Backups]] —
  the backup and the tested restore now matter more.
- **Instance roles.** No credential-free access to
  provider APIs, so secrets live in files or a secret
  store — see [[Secrets Management]].
- **Autoscaling and multi-AZ.** One machine is one
  [[Single Point of Failure]]. A VPS reboot is an outage.
- **The managed services themselves.** If you genuinely
  use [[Amazon SES]], [[AWS KMS]] or [[Amazon S3]], you
  can still call them from a VPS — this is a compute
  decision, not an all-or-nothing exit.
- **Somebody else patching the OS.** That is now you; see
  [[Linux Server Hardening]] and [[Unattended Upgrades]].

## Doing it

1. **Rent the box.** [[Hetzner Cloud]] for the best price
   per GB of RAM, [[DigitalOcean]] for the friendlier
   console and docs.
2. **Harden it** — SSH keys only, no root password login,
   [[UFW]] closed except 22/80/443, unattended upgrades.
   [[SSH Key Authentication]] is the first step.
3. **Terminate TLS** with [[Caddy]], which obtains and
   renews certificates with no cron job — see
   [[Automatic HTTPS]].
4. **Ship code with a tool, not with SSH by hand.** This
   is the part that used to be miserable and no longer is.

## The four ways to deploy onto it

Pick the leftmost one that solves your problem:

| Approach | What it gives you | Cost of the abstraction |
|---|---|---|
| `git pull` + [[systemd]] | nothing to learn | no rollback, brief downtime, drift between machines |
| [[Docker Compose]] | reproducible builds, see [[Containers in Production]] | you still script the deploy |
| [[Kamal]] | zero-downtime container deploys over SSH, rollback, multiple servers | needs a registry and a Dockerfile |
| [[Coolify]] | a web UI, push-to-deploy, managed-feeling databases and TLS — see [[Self-Hosted PaaS]] | a control plane you now operate |

[[Kamal]] and [[Coolify]] are the two that make this
comparison interesting. They deliver most of what people
actually buy [[Managed PaaS]] for — push to deploy, TLS,
rollback, preview environments — on a machine you rent
for a tenth of the price.

## When to stay on the hyperscaler anyway

- You are already deep in one provider's IAM model and
  the operational cost of splitting exceeds the savings.
- A compliance requirement names a region, a control, or
  an audit artefact you cannot produce yourself — see
  [[SOC 2]] and [[Shared Responsibility Model]].
- Your load is genuinely spiky and scale-to-zero is worth
  real money — see [[Serverless Architecture]].
- Nobody on the team wants to own a machine. That is a
  legitimate answer, and [[Managed PaaS]] is the cheaper
  way to buy it than AWS.

## Watch out for

- **The savings are real; the ops burden is also real.**
  You have traded money for time. If the time is worth
  more than the money, do not make the trade.
- **One box with no backups is not cheaper than AWS, it
  is a deferred loss.** Nightly dumps off the machine,
  and restore them once.
- **Provider snapshots are a rollback, not a backup.**
  They live in the same account as the thing they protect.
- **Do not skip the reverse proxy** and expose the app
  process on port 80 directly; see [[Reverse Proxy]].

## Related

[[One-Box Deployment]] · [[Self-Hosted PaaS]] ·
[[Kamal]] · [[Coolify]] · [[Managed PaaS]] ·
[[Cost Control]] · [[Hetzner Cloud]] · [[DigitalOcean]] ·
[[Amazon EC2]] · [[Containers in Production]] ·
[[Cloud Service Models]] · [[Anti-Patterns]] ·
[[Deployment Strategies]] · [[The Ladder]]

## Sources

- [[kamal-home]] · [[coolify-introduction]] ·
  [[hetzner-create-a-server]] ·
  [[digitalocean-droplet-quickstart]] ·
  [[aws-ec2-get-started]] · [[aws-budgets-managing-costs]]
