---
type: Tool
title: "Git"
description: "The version control system underneath everything here - your history, your rollback, and the trigger for most deployments."
wikipedia: "https://en.wikipedia.org/wiki/Git"
tags: [dev-environment, ops-and-security, tooling]
timestamp: "2026-07-27T00:00:00Z"
---

# Git

Distributed version control. Every deployment method in
this wiki above rung 1 keys off it: a push builds a
[[Cloudflare Pages]] site, a tag triggers
[[GitHub Actions]], a `git pull` on the server is the
first honest form of [[Git-Driven Deployment]].

## Configure once, on a new machine

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global core.editor "code --wait"
git config --global push.autoSetupRemote true
```

`git config --global --list` shows the result;
`~/.gitconfig` is the file it writes.

## The daily commands

```bash
git status                 # before anything else
git switch -c feature-x    # branch
git add -p                 # stage hunk by hunk
git commit -m "..."        # small, described commits
git push
git log --oneline --graph  # what happened
git diff HEAD~1            # what changed
git restore --staged FILE  # unstage
git revert <sha>           # undo, safely, in public
```

`git revert` rather than `git reset --hard` on anything
already pushed: rollback should be a new commit, not a
rewritten history.

## What must never be committed

`.env`, `*.pem`, `*.key`, API tokens, database dumps.
Once pushed, a secret is compromised even after
deletion — rotate it, do not just remove it. Enable
secret scanning on [[GitHub]] and read
[[Secrets Management]].

## Related

[[Development Setup]] · [[GitHub]] ·
[[Git-Driven Deployment]] · [[GitHub Actions]] ·
[[Secrets Management]] · [[Continuous Integration and Delivery]] ·
[[Deployment Environments]]

## Sources

- Upstream documentation: <https://git-scm.com/doc>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
