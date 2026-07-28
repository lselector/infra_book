---
type: Tool
title: "Bash"
description: "The shell your servers run and your scripts target - the most portable skill in this wiki."
wikipedia: "https://en.wikipedia.org/wiki/Bash_(Unix_shell)"
tags: [dev-environment, foundations, scripting]
timestamp: "2026-07-27T00:00:00Z"
---

# Bash

The GNU Bourne-Again Shell: the default login shell on
[[Ubuntu Server]] and most Linux distributions, and the
interpreter behind nearly every deploy script,
`Dockerfile` `RUN` line and CI step you will write.

macOS ships `zsh` as the interactive default, which is
Bash-compatible for everything in this list; scripts
should still start `#!/usr/bin/env bash`.

## The working set

```bash
ls cd pwd cp mv rm mkdir           # navigation
cat less head tail                 # reading
grep find fd rg                    # searching
| > >> 2>&1 <                      # pipes, redirection
chmod chown sudo                   # permissions
ps top htop kill                   # processes
tar gzip scp rsync                 # moving files
df du free                         # what is full
export $VAR ~/.bashrc              # environment
for while if [ ] $(...)            # scripting
```

## Habits that prevent outages

- `set -euo pipefail` at the top of any script you will
  run unattended: stop on error, on undefined variable,
  and on a failing stage of a pipeline.
- Quote every expansion — `"$file"`, not `$file`. A
  space in a filename is how `rm -rf $DIR/` deletes the
  wrong thing.
- `rsync -avn` (dry run) before `rsync -av`.
- Prefer absolute paths in scripts; `cd` failures are
  silent otherwise.
- `shellcheck` your scripts. It catches the quoting
  bugs you cannot see.

## When to stop

Past roughly a hundred lines, or as soon as you need
data structures, error handling or tests, rewrite it in
Python. Bash is glue, not an application language —
the build scripts in [[Static Build Pipeline]] are
Python for exactly this reason.

## Related

[[Development Setup]] · [[iTerm2]] · [[Homebrew]] ·
[[SSH Key Authentication]] · [[Ubuntu Server]] ·
[[Static Build Pipeline]] · [[Twelve-Factor App]]

## Sources

- Upstream documentation: the GNU Bash manual,
  <https://www.gnu.org/software/bash/manual/>. Not part
  of the downloaded `Raw/` corpus — no capture to cite
  yet.
