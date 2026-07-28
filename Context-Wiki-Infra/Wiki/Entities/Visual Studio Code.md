---
type: Tool
title: "Visual Studio Code"
description: "The default editor for most developers - huge extension ecosystem, remote-SSH editing, and the base Cursor is forked from."
wikipedia: "https://en.wikipedia.org/wiki/Visual_Studio_Code"
tags: [dev-environment, tooling, editor]
timestamp: "2026-07-27T00:00:00Z"
---

# Visual Studio Code

<https://code.visualstudio.com> — free, cross-platform,
Electron-based, and the editor most job postings assume.
`brew install --cask visual-studio-code`.

## What it is good at

- The extension marketplace: a maintained extension for
  every language, formatter and cloud CLI you will meet
  in this wiki.
- **Remote - SSH**: open a folder on your VPS and edit
  it as if it were local, with the language server
  running on the server. Convenient — but treat it as a
  debugging tool, not a deployment method. Deploys
  belong to [[Git-Driven Deployment]].
- **Dev Containers**: develop inside the same [[Docker]]
  image you ship.
- Integrated terminal, so [[Bash]] is always one panel
  away.
- `code --wait` works as `core.editor` for [[Git]]
  commit messages.

## Cursor

A fork of VS Code with a deeper AI integration and its
own subscription. Your settings and extensions carry
over. [[Claude Code]] runs as an extension in stock VS
Code if you would rather not switch editors.

## Configure before writing code

- Format on save; a linter for your language.
- Add `.env`, `*.pem`, `*.key` to
  `files.exclude`/`search.exclude` and to `.gitignore`.
- Review what each extension is allowed to send off the
  machine — see [[Secrets Management]].

## Related

[[Development Setup]] · [[Zed]] · [[Claude Code]] ·
[[Docker]] · [[Git]]

## Sources

- Upstream documentation: <https://code.visualstudio.com/docs>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
