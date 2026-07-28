---
type: Tool
title: "Zed"
description: "A fast native code editor with an AI agent built in - one of several fine choices, and the one that starts quickest."
wikipedia: "https://en.wikipedia.org/wiki/Zed_(text_editor)"
tags: [dev-environment, tooling, editor]
timestamp: "2026-07-27T00:00:00Z"
---

# Zed

<https://zed.dev> — an open-source editor written in
Rust, GPU-rendered, with language servers, multiplayer
editing and an agent panel built in rather than bolted
on. macOS and Linux; `brew install --cask zed`.

## Why it shows up here

- Starts and opens large files noticeably faster than
  Electron-based editors.
- Language server support is built in: `gopls`,
  `pyright`, `rust-analyzer` and friends configure
  themselves for most projects.
- The agent panel runs [[Claude Code]]-style edits
  inside the editor, with a diff view before anything
  is written.
- `zed .` from the terminal, `cmd-shift-p` for commands,
  vim mode if you want it.

## Alternatives, all reasonable

| Editor | Best at |
|---|---|
| [[Visual Studio Code]] | The largest extension ecosystem; Cursor is a fork with heavier AI |
| Sublime Text | Speed and stability, small footprint |
| WebStorm / PyCharm / RustRover | Deep refactoring and debugging per language |
| Neovim / Vim / Helix | Terminal-native, modal, present on every server |

## Configure before writing code

- Format on save, with the project's formatter.
- A linter for your language.
- `.env`, `*.pem` and `*.key` excluded from indexing and
  from any AI context — see [[Secrets Management]].

## Related

[[Development Setup]] · [[Claude Code]] ·
[[Visual Studio Code]] · [[Homebrew]]

## Sources

- Upstream documentation: <https://zed.dev/docs>. Not
  part of the downloaded `Raw/` corpus — no capture to
  cite yet.
