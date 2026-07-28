---
type: Tool
title: "Pulumi"
description: "Infrastructure as code in a real programming language."
wikipedia: "https://en.wikipedia.org/wiki/Pulumi"
tags: [scaling, ops-and-security]
timestamp: "2026-07-27T00:00:00Z"
---

# Pulumi

The same declarative model as [[Terraform]], expressed in
TypeScript, Python, Go or C# rather than a purpose-built
configuration language.

## The argument for it

Loops, conditionals, functions and types come from the
language, so complex or repetitive infrastructure is
easier to express, and you get IDE completion and unit
tests over your infrastructure code.

## The argument against it

A general-purpose language makes it easy to write
infrastructure code that is clever, and clever
infrastructure code is hard to review. HCL's limitations
are partly the point.

## Choosing

Terraform if you want the largest ecosystem, the most
examples and the most hireable skill. Pulumi if your team
is strong in one of its languages and your infrastructure
genuinely has logic in it.

Either way, see [[Infrastructure as Code]] first for
whether you need one yet.

## Related

[[Infrastructure as Code]] · [[Terraform]] ·
[[Deployment Environments]]

## Sources

- [[pulumi-iac-concepts]] · [[terraform-intro]]
