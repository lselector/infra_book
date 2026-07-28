---
type: Tool
title: "iTerm2"
description: "The terminal emulator most macOS developers use instead of Terminal.app - split panes, searchable scrollback, profiles."
wikipedia: "https://en.wikipedia.org/wiki/ITerm2"
tags: [dev-environment, tooling, macos]
timestamp: "2026-07-27T00:00:00Z"
---

# iTerm2

<https://iterm2.com> — a free, mature terminal emulator
for macOS. `brew install --cask iterm2`.

## What you get over Terminal.app

- Split panes (`⌘D` vertical, `⌘⇧D` horizontal) — an
  editor, a log tail and an SSH session at once.
- Searchable scrollback (`⌘F`) with match highlighting.
- Profiles: a colour scheme and starting directory per
  project or per server, so a production shell *looks*
  different from a local one.
- `⌘;` autocomplete from scrollback history.
- Instant replay, triggers, and a proper hotkey window.

## Worth configuring on day one

- A distinct background colour for any profile that
  SSHes into production. Colour is a cheap safety
  interlock.
- Unlimited scrollback, or at least 100,000 lines.
- Natural-text editing so `⌥←`/`⌥→` move by word.

## Alternatives

Ghostty, WezTerm, Alacritty and Kitty are all fast,
GPU-accelerated and cross-platform; on Linux use your
desktop's terminal or Kitty; on Windows use Windows
Terminal with [[Windows Subsystem for Linux]]. Any of
them is fine — the terminal is a means to [[Bash]].

## Related

[[Development Setup]] · [[Bash]] · [[Homebrew]] ·
[[SSH Key Authentication]]

## Sources

- Upstream documentation:
  <https://iterm2.com/documentation.html>. Not part of
  the downloaded `Raw/` corpus — no capture to cite yet.
