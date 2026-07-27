---
type: Summary
title: "GitHub Actions — workflow syntax reference"
description: "A workflow is a configurable automated process made up of one or more jobs."
resource: "https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax"
source_file: "Raw/05_ops_cicd_security/github-actions-workflow-syntax.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# GitHub Actions — workflow syntax reference

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/github-actions-workflow-syntax.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>

## Opening

> A workflow is a configurable automated process made up of one or more jobs. You must create a YAML file to define your workflow configuration.
> Workflow files use YAML syntax, and must have either a `.yml` or `.yaml` file extension. If you're new to YAML and want to learn more, see [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/).
> You must store workflow files in the `.github/workflows` directory of your repository.
> The name of the workflow. GitHub displays the names of your workflows under your repository's "Actions" tab. If you omit `name`, GitHub displays the workflow file path relative to the root of the repository.

## Contents of the source document

- Workflow syntax for GitHub Actions
  - In this article
  - About YAML syntax for workflows
  - name
  - run-name
    - Example of run-name
  - on
    - Using a single event
    - Using multiple events
    - Using activity types
    - Using filters
    - Using activity types and filters with multiple events
  - on.<event_name>.types
  - on.<pull_request|pull_request_target>.<branches|branches-ignore>
    - Example: Including branches
    - Example: Excluding branches
    - Example: Including and excluding branches
  - on.push.<branches|tags|branches-ignore|tags-ignore>

## Related pages

[[Authentication]] · [[Dependabot]] · [[Docker]] · [[GitHub Actions]] · [[HTTP]] · [[Nginx]] · [[Redis]]
