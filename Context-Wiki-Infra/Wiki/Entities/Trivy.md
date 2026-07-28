---
type: Tool
title: "Trivy"
description: "One scanner for container images, filesystems, dependencies and IaC."
website: "https://trivy.dev/"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Trivy

Scans for known vulnerabilities and misconfigurations
across several targets with one tool: container images,
filesystems, Git repositories, Kubernetes manifests and
Terraform files.

## Why it is convenient

```bash
trivy image myapp:latest
trivy fs .
trivy config ./infra
```

Three commands cover [[Dependency Auditing]] for the
image, the source tree, and misconfiguration in your
[[Infrastructure as Code]] — without adding three tools.

## In a pipeline

Fail the build on HIGH and CRITICAL with a fix available.
Do not fail on everything: unfixable advisories in a base
image will block every build and the team will disable the
check.

## Watch out for

Findings in the base image are usually fixed by choosing a
smaller or newer base rather than by patching. `-slim` and
distroless images dramatically reduce the count.

## Related

[[Dependency Auditing]] · [[Docker]] ·
[[Security Testing]] · [[Infrastructure as Code]] ·
[[Container Images]] · [[Docker Build Cache]] ·
[[OSS-Fuzz]]

## Sources

- [[trivy-overview]] · [[docker-build-best-practices]]
