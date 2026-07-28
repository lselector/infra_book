---
type: Tool
title: "Claude Code"
description: "Anthropic's coding agent - reads the repository, runs commands and edits files, in the terminal or inside your editor."
wikipedia: "https://en.wikipedia.org/wiki/Claude_(AI)"
tags: [dev-environment, tooling, ai]
timestamp: "2026-07-27T00:00:00Z"
---

# Claude Code

An AI coding agent from Anthropic that works against a
real repository: it reads files, runs commands, edits
code and shows you the diff. It runs in the terminal, in
the desktop and web apps, and as an extension inside
[[Zed]] and [[Visual Studio Code]].

## How it fits the workflow here

- Point it at a repo and ask for a change; it explores,
  edits, runs the tests, and reports.
- A `CLAUDE.md` in the repository root carries your
  project's conventions — formatting rules, build
  commands, deployment steps — and the agent follows
  them on every task. This wiki's own build scripts are
  governed that way.
- Good at the tedious, well-specified work: writing a
  deploy script, adding [[Security Headers]], wiring up
  a [[FastAPI]] endpoint, converting a directory of
  content, updating docs after a change.

## Rules that keep it safe

- **Review every diff.** Treat it as a fast contributor
  with perfect recall and no stake in your business.
- **Never paste live secrets into a prompt.** Keep
  `.env` in `.gitignore`; see [[Secrets Management]].
- **Give it a branch, not `main`.** Let CI and code
  review do their normal job — [[GitHub Actions]] does
  not care who wrote the commit.
- **Be specific about scope.** "Add pagination to the
  products endpoint" produces a reviewable diff;
  "improve the backend" does not.

## Alternatives

GitHub Copilot, Cursor's agent, Aider, and Gemini CLI
occupy the same space. The habits above apply to all of
them.

## Related

[[Development Setup]] · [[Zed]] ·
[[Visual Studio Code]] · [[Secrets Management]] ·
[[Git-Driven Deployment]] · [[GitHub Actions]]

## Sources

- Upstream documentation: <https://docs.claude.com/en/docs/claude-code>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
