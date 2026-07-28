---
type: Tool
title: "Invoke"
description: "Python task runner - tasks.py with @task decorators, so project commands can contain real logic."
website: "https://www.pyinvoke.org/"
tags: [tooling, python, dev-environment]
timestamp: "2026-07-28T00:00:00Z"
---

# Invoke

A task execution tool for Python. You write a `tasks.py`
with decorated functions; Invoke turns each into a
subcommand with its own flags, and `c.run()` shells out.

```python
from invoke import task

@task
def clean(c):
    """Validate and clean the inventory JSON."""
    c.run("uv run s1_clean_inventory.py")

@task(pre=[clean])
def build(c, minify=False):
    """Build the static site."""
    c.run(f"uv run s3_build_site.py {'--minify' if minify else ''}")

@task(pre=[build])
def deploy(c, branch="preview"):
    """Deploy to Cloudflare Pages."""
    c.run(f"wrangler pages deploy ./dist --branch {branch}")

@task
def test(c, k=None):
    c.run(f"uv run pytest -q {f'-k {k}' if k else ''}")
```

```bash
inv --list              # every task with its docstring
inv build --minify      # flags generated from the signature
inv deploy main
```

The signature *is* the CLI: parameters become options,
booleans become flags, docstrings become help text.

## What it gives you that a runner cannot

**It is Python, not a config format.** Tasks can loop
over a list of environments, read a JSON file, branch on
what a previous command returned, import your own
modules, and raise real exceptions. When a "command" has
genuinely become a small program — a migration with a
safety check, a release that reads the changelog, a
deploy that fans out over eight targets — this is the
right shape, and [[just]] or [[GNU Make]] would just be
wrapping a script you had to write anyway.

Practical details that matter in use:

- `c.run("cmd", warn=True)` returns a `Result` instead of
  aborting, so you can inspect `.ok`, `.stdout`.
- `hide=True`, `pty=True`, `env={...}`, `echo=True`.
- `c.cd("subdir")` — a context manager that actually
  persists across commands, unlike a `Makefile` recipe.
- Namespaces (`Collection`) group tasks as
  `inv db.migrate`, which scales past twenty tasks better
  than a flat file.
- Configuration from `invoke.yaml`, env vars, or the CLI.

## Fabric: the same tasks, over SSH

[Fabric](https://www.fabfile.org/) is built on Invoke by
the same author, and swaps the local runner for an SSH
connection: `c.run()` executes on a remote host,
`c.put()` uploads. For a [[One-Box Deployment]] this is
the honest middle ground between running commands by hand
and adopting [[Infrastructure as Code]] — the same
`@task` functions, aimed at the server
([[SSH Key Authentication]] does the authentication).

## Where it fits against the other two

| | [[GNU Make]] | [[just]] | **Invoke** |
|---|---|---|---|
| Written in | Makefile syntax | justfile syntax | Python |
| Task logic | Shell only | Shell only | Full language |
| Skips work by timestamp | Yes | No | No |
| Startup | Instant | Instant | ~200 ms (interpreter) |
| Needs a runtime | No | No | **Yes — Python** |
| Argument parsing | Manual | Positional | Generated from the signature |

**Choose Invoke when the project is already Python and
the tasks need real logic or remote execution.** Choose
[[just]] when they are one-liners you want to name.
Choose [[GNU Make]] when the tool should decide whether
the work is needed at all.

## Watch out for

- **The bootstrap problem.** Invoke lives in a Python
  environment, so `inv` cannot be the thing that creates
  that environment. [[uv]] resolves this neatly:
  `uv run inv build` installs and runs in one step, from
  a clean checkout, with no activation ritual.
- **It pins to your project's Python.** A task runner
  that breaks during a Python upgrade is an annoyance a
  single static binary ([[just]]) does not have.
- **Tasks quietly becoming an application.** The freedom
  cuts both ways; when `tasks.py` passes a few hundred
  lines it wants to be a module that tasks call.
- **Do not put secrets in `tasks.py`** — it is committed
  code ([[Secrets Management]]).

## Related

[[just]] · [[GNU Make]] · [[uv]] · [[pytest]] ·
[[Development Setup]] · [[Static Build Pipeline]] ·
[[Continuous Integration and Delivery]] ·
[[One-Box Deployment]] · [[SSH Key Authentication]] ·
[[Bash]] · [[FastAPI]]

## Sources

- Upstream documentation: <https://www.pyinvoke.org/>
  and <https://www.fabfile.org/>. Not part of the
  downloaded `Raw/` corpus — related captures:
  [[12factor-dev-prod-parity]] ·
  [[ssh-keygen-man-page]] ·
  [[cloudflare-wrangler-pages-commands]].
