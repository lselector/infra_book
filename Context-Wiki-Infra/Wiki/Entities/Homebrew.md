---
type: Tool
title: "Homebrew"
description: "The package manager for macOS (and Linux) - one command to install the Unix tools, languages and libraries this wiki assumes."
wikipedia: "https://en.wikipedia.org/wiki/Homebrew_(package_manager)"
tags: [dev-environment, tooling, macos]
timestamp: "2026-07-27T00:00:00Z"
---

# Homebrew

<https://brew.sh> — installs Unix software into its own
prefix (`/opt/homebrew` on Apple Silicon), so nothing
touches the system directories and nothing needs `sudo`.

## Installing

```bash
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then add the shell environment line it prints to your
`~/.zshrc` or `~/.bashrc`.

## The starting set

```bash
brew install htop wget grep vim git fd
brew install uv
brew install ffmpeg imagemagick
brew install fzf ripgrep neovim        # optional
brew install coreutils diffutils       # optional
```

- `htop` — a readable `top`; the first thing you run on
  a machine that feels slow.
- `fd` and `ripgrep` — fast `find` and `grep` that
  respect `.gitignore`.
- `coreutils` / `diffutils` — GNU versions of the BSD
  tools macOS ships, so scripts behave the same locally
  as on [[Ubuntu Server]].

## Formulae and casks

- `brew install <name>` — command-line software.
- `brew install --cask <name>` — GUI applications
  ([[iTerm2]], [[Visual Studio Code]], [[Zed]],
  [[Bitwarden]] all install this way).
- `brew services start <name>` — run [[PostgreSQL]] or
  [[Redis]] locally as a background service.

## Keeping it healthy

```bash
brew update && brew upgrade && brew cleanup
brew doctor      # when something behaves oddly
brew list        # what you actually have
```

## Watch out for

- Do not use it to pin production versions. It tracks
  head-of-stream; your server should install from its
  distribution's packages or a lockfile.
- `brew upgrade` can move a language runtime under a
  project. Manage Python with [[uv]] and Node with a
  version manager rather than with brew alone.
- On Linux it works, but `apt` is usually the better
  first answer.

## Related

[[Development Setup]] · [[uv]] · [[just]] ·
[[GNU Make]] · [[iTerm2]] · [[Bash]] ·
[[Ubuntu Server]]

## Sources

- Upstream documentation: <https://brew.sh> and
  <https://docs.brew.sh>. Not part of the downloaded
  `Raw/` corpus — no capture to cite yet.
