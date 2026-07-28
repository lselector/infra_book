---
type: Dashboard
title: "Development Setup - The Machine You Build From"
description: "The tools on your own computer before rung 1: a Unix shell, a password manager, a terminal, an editor, an AI coding agent, Homebrew, GitHub and SSH."
tags: [dev-environment, tooling, orientation, workstation]
timestamp: "2026-07-27T00:00:00Z"
---

# Development Setup — The Machine You Build From

Everything in [[Stacks]] assumes a working developer
machine. This page is rung zero: the small, stable set
of tools you install once and then stop thinking about.

None of it is exotic, and almost all of it is free. The
goal is a machine where the same commands work locally
and on the server, where credentials are never typed
twice, and where deploying is one command.

---

## 1. A Unix-based development environment

Servers run Linux. Every command in this wiki —
`ssh`, `systemctl`, `psql`, `caddy`, `rsync` — is a
Unix command. Develop on the same shape of system and
the gap between "works on my laptop" and "works in
production" mostly disappears.

Three ways to get one:

| | What it is | Notes |
|---|---|---|
| **Linux** | The real thing | [[Ubuntu Server]]'s desktop sibling, Fedora, Debian — closest to production |
| **macOS** | BSD-based Unix | The common choice; `brew` fills in the GNU tools |
| **WSL** | [[Windows Subsystem for Linux]] | A real Ubuntu kernel inside Windows; keep your code *inside* the Linux filesystem |

Plain Windows without WSL is the one setup that will
fight you at every step. Install WSL first.

## 2. A password manager

Non-negotiable, and the very first install. You are
about to create accounts at a registrar, a host, a
cloud provider, GitHub and an email provider — every
one of them a way into your infrastructure.

- **[[Bitwarden]]** — <https://bitwarden.com> — open
  source, free tier, apps and browser extensions on
  every platform.
- Generate a unique random password per site. Never
  reuse, never "remember" one in your head.
- Turn on [[Multi-Factor Authentication]] everywhere it
  is offered, starting with your email, your domain
  registrar and GitHub.
- Store recovery codes in the manager too — they are
  the thing people lose.

The password manager holds *your* credentials.
Application secrets are a different problem with a
different answer: [[Secrets Management]].

## 3. A convenient terminal

You will live here. The default terminal works, but a
better one pays for itself in split panes and search.

- **macOS** — [[iTerm2]] (<https://iterm2.com>), or
  Ghostty / WezTerm / Alacritty if you prefer.
- **Linux** — GNOME Terminal, Konsole, Kitty, Alacritty.
- **Windows** — Windows Terminal, running your WSL
  distribution.

Learn the three shortcuts that matter: split pane, new
tab, and search scrollback.

## 4. Bash shell knowledge

Not a tool to install — a skill, and the one with the
longest shelf life in this whole list. See [[Bash]].

Know these well enough not to look them up:

```bash
ls cd pwd cp mv rm mkdir           # moving around
cat less head tail grep find       # reading and searching
| > >> 2>&1                        # pipes and redirection
chmod chown sudo                   # permissions
ps top kill                        # processes
tar gzip scp rsync                 # moving files about
export $VAR ~/.bashrc              # environment
for while if [ ] $(...)            # enough scripting
```

Plus the habits: `set -euo pipefail` at the top of any
script you intend to trust, quote your `"$variables"`,
and `history | grep` before you retype anything.

## 5. A coding editor

Any of these is a fine choice; the wrong move is having
no opinion and editing production files in `nano` over
SSH.

- **[[Zed]]** — <https://zed.dev> — fast, native, AI
  built in.
- **[[Visual Studio Code]]** — the default for most
  people; Cursor is a fork of it with heavier AI.
- **Sublime Text** — very fast, very stable.
- **JetBrains** — WebStorm, PyCharm, RustRover — the
  most capable refactoring and debugging tools.
- **Neovim / Vim / Helix** — modal, terminal-native,
  and the reason knowing basic `vim` is still worth an
  afternoon: it is on every server you will ever SSH
  into.

Whatever you pick, configure format-on-save and a
linter for your language, and turn *off* anything that
uploads your `.env` files.

## 6. An AI coding agent

An agent that can read the repository, run commands and
edit files is now part of the toolchain rather than a
novelty.

- **[[Claude Code]]** — in the terminal, in [[Zed]], or
  in [[Visual Studio Code]].
- Point it at a repository with a `CLAUDE.md` describing
  the project's conventions, and it will follow them.
- Review every diff. An agent is a fast junior with
  perfect recall and no judgement about your business.
- Never paste live secrets into a prompt, and keep
  `.env` in `.gitignore` — see [[Secrets Management]].

## 7. Homebrew — the package manager

**[[Homebrew]]** — <https://brew.sh> — installs Unix
tools, languages and libraries on macOS (and Linux)
without `sudo` and without fighting the system.

```bash
# the tools you will use daily
brew install htop wget grep vim git fd

# Python, packaging and virtualenvs, fast
brew install uv

# one file of project commands, instead of make
brew install just

# media handling
brew install ffmpeg imagemagick

# optional but very good
brew install fzf ripgrep neovim

# optional: GNU versions of the BSD tools on macOS
brew install coreutils diffutils
```

On Ubuntu/Debian the same list is `apt install`, minus
`uv` (install it with the upstream script). See [[uv]]
for why it replaces `pip`, `venv` and `pyenv` at once,
and [[just]] for why a `justfile` beats a `Makefile` for
the handful of commands every project accumulates —
[[GNU Make]] for when it does not, and [[Invoke]] when a
task needs to be a Python function rather than a shell
line.

Keep it tidy: `brew update && brew upgrade`, then
`brew cleanup`, every few weeks.

## 8. A GitHub account and local Git config

[[Git]] is the version control system; [[GitHub]] is
where the repository lives and what
[[Git-Driven Deployment]] and [[GitHub Actions]] hang
off.

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global core.editor "code --wait"
```

Then, on GitHub itself: turn on
[[Multi-Factor Authentication]], add your SSH public
key (below), and save the recovery codes in
[[Bitwarden]].

A first `.gitignore` worth having everywhere:

```gitignore
.env
.env.*
*.pem
*.key
__pycache__/
.venv/
node_modules/
.DS_Store
```

## 9. SSH configuration

One directory, one config file, and a key per purpose.
The full argument for keys over passwords is in
[[SSH Key Authentication]].

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "you@example.com" \
  -f ~/.ssh/id_ed25519_github
ssh-keygen -t ed25519 -C "you@example.com" \
  -f ~/.ssh/id_ed25519_server
```

`~/.ssh/config` — so you type `ssh myserver`, never an
IP address:

```sshconfig
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes

Host myserver
    HostName 203.0.113.10
    User deploy
    IdentityFile ~/.ssh/id_ed25519_server
    IdentitiesOnly yes
    ServerAliveInterval 60
```

Then:

- `chmod 600 ~/.ssh/config ~/.ssh/id_ed25519_*` — SSH
  refuses to use keys that others can read.
- Add the *public* key (`.pub`) to GitHub and to the
  server's `~/.ssh/authorized_keys`. The private key
  never leaves your machine.
- Test with `ssh -T git@github.com` and `ssh myserver`.
- Back up `~/.ssh` into [[Bitwarden]] as a secure note
  or file attachment, encrypted.
- Only once key login works: disable password login on
  the server ([[Linux Server Hardening]]).

---

## The whole setup as a checklist

| # | Item | Done when |
|---|---|---|
| 1 | Unix-based machine | Linux, macOS, or WSL installed |
| 2 | Password manager | [[Bitwarden]] installed, MFA on email |
| 3 | Terminal | [[iTerm2]] or equivalent, panes learned |
| 4 | Shell | Comfortable with the [[Bash]] list above |
| 5 | Editor | Installed, format-on-save configured |
| 6 | AI agent | [[Claude Code]] running in your repo |
| 7 | [[Homebrew]] | `brew install` list completed, [[just]] included |
| 8 | [[Git]] / [[GitHub]] | `git config` set, account has MFA |
| 9 | SSH | `ssh myserver` and `ssh -T git@github.com` both work |

Nine items, an afternoon, once. After that you are
standing at rung 1 of [[Stacks]] with nothing between
you and a deployed site.

## See also

* [[Stacks]] — the ten-rung ladder this page precedes.
* [[Topics]] — the keyword plan behind the wiki.
* [[Static Build Pipeline]] — the local build scripts
  these tools run, and [[just]] as their front door.
* [[Linux Server Hardening]] — the same care, applied to
  the machine at the other end of your SSH config.

---

Created: 2026-07-27
Last updated: 2026-07-27
