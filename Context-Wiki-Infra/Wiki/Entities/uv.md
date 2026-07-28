---
type: Tool
title: "uv"
description: "A fast Python package and project manager that replaces pip, venv, pipx and pyenv with one binary."
website: "https://docs.astral.sh/uv/"
tags: [dev-environment, tooling, python]
timestamp: "2026-07-27T00:00:00Z"
---

# uv

From Astral, written in Rust. `brew install uv`, or the
upstream install script on Linux. It resolves and
installs Python dependencies an order of magnitude
faster than `pip`, and it manages the interpreter too.

## The commands worth knowing

```bash
uv init myproject          # pyproject.toml + .venv
uv add fastapi uvicorn     # install and record the dep
uv remove requests
uv sync                    # reproduce the locked env
uv run python app.py       # run inside the project env
uv run pytest
uv python install 3.13     # get an interpreter
uv tool install ruff       # global CLI tool (pipx)
uvx ruff check .           # run one without installing
```

## Why it matters for deployment

`uv.lock` pins every transitive dependency with hashes,
so the environment on your laptop, in [[GitHub Actions]]
and on the server are the same environment. That is the
dependency half of [[Twelve-Factor App]] handled by a
single checked-in file.

On the server, `uv sync --frozen` in the deploy step
installs exactly the lockfile — no resolution, no
surprise upgrade at 2am. In [[Docker]], copy
`pyproject.toml` and `uv.lock` first so the dependency
layer caches.

## Watch out for

- Commit `uv.lock`; never `.gitignore` it.
- It is young and moving fast. Pin the uv version in CI
  if a release ever surprises you.
- `pip` still works inside a uv-created venv, but
  installing that way leaves the lockfile lying.

## Related

[[Development Setup]] · [[Homebrew]] · [[FastAPI]] ·
[[GitHub Actions]] · [[Docker]] · [[Twelve-Factor App]] ·
[[Static Build Pipeline]]

## Sources

- Upstream documentation: <https://docs.astral.sh/uv/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
