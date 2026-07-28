---
type: Tool
title: "Terraform"
description: "The default infrastructure-as-code tool - declare resources, plan, apply."
wikipedia: "https://en.wikipedia.org/wiki/Terraform_(software)"
tags: [scaling, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Terraform

Describes infrastructure in HCL, computes the difference
between the declared state and reality, and applies it.

## The workflow

```bash
terraform init     # download providers
terraform plan     # show the diff - read this
terraform apply    # make it so
```

`plan` is the feature. Seeing exactly what will change
before it changes is what makes infrastructure work
reviewable in a pull request.

## Where it pays off here

- A second environment — see [[Deployment Environments]].
- DNS records, which are tedious and error-prone by hand.
- Rebuilding after a disaster.

## Where it does not

One VPS and five records. Clicking is faster, and the
state file is a new thing to look after. See
[[Infrastructure as Code]].

## Watch out for

- **State.** It holds secrets in plaintext and is the
  source of truth. Store it remotely with locking; never
  in Git.
- Provider version pinning, or an upgrade will surprise
  you mid-apply.
- Manual console changes cause drift; [[AWS Config]] will
  tell you about them.

## Related

[[Infrastructure as Code]] · [[Pulumi]] ·
[[Deployment Environments]] · [[Secrets Management]]

## Sources

- [[terraform-intro]] · [[terraform-language]] ·
  [[terraform-iac-tutorial]]
