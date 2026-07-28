---
type: Tool
title: "Windows Subsystem for Linux"
description: "A real Linux kernel inside Windows - the way to develop against the same system your servers run."
wikipedia: "https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux"
tags: [dev-environment, tooling, windows]
timestamp: "2026-07-27T00:00:00Z"
---

# Windows Subsystem for Linux

WSL 2 runs a genuine Linux kernel in a lightweight VM
managed by Windows, with the filesystem, networking and
`systemd` support that make it behave like the
[[Ubuntu Server]] you deploy to.

## Installing

```powershell
wsl --install                 # Ubuntu by default
wsl --install -d Ubuntu-24.04 # or pick the release
wsl -l -v                     # list, check it says 2
```

Then, inside it, you are on Ubuntu: `apt`, [[Bash]],
`ssh`, `systemctl`.

## The one rule that matters

**Keep your code in the Linux filesystem**
(`~/projects`), not under `/mnt/c/`. Cross-filesystem
access is slow enough to make `git status` and test
runs painful, and file permissions do not survive the
boundary — which breaks `chmod 600 ~/.ssh/config` and
therefore [[SSH Key Authentication]].

## Working setup

- **Windows Terminal** as the front end, with the
  Ubuntu profile as default.
- [[Visual Studio Code]] with the **WSL** extension:
  the UI runs on Windows, the language server and
  terminal run in Linux. `code .` from inside WSL opens
  it correctly.
- `explorer.exe .` opens the current Linux directory in
  Windows Explorer when you need it.
- Docker Desktop hands [[Docker]] to WSL directly.

## Watch out for

- Line endings. Set `git config --global core.autocrlf
  input` and add a `.gitattributes`; a CRLF in a shell
  script produces a baffling `bad interpreter` error on
  the server.
- WSL 1 still exists and lacks the real kernel. Confirm
  version 2.
- Localhost forwarding between Windows and WSL is
  usually automatic, but firewall rules can interfere.

## Related

[[Development Setup]] · [[Bash]] · [[Ubuntu Server]] ·
[[Visual Studio Code]] · [[Docker]] ·
[[SSH Key Authentication]]

## Sources

- Upstream documentation: <https://learn.microsoft.com/windows/wsl/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
