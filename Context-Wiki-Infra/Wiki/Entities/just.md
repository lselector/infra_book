---
type: Tool
title: "just"
description: "A command runner with make's syntax and none of its traps - one justfile as the front door to a project."
website: "https://just.systems/"
tags: [tooling, dev-environment, deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# just

A command runner. You write a `justfile` listing the
commands a project needs — build, test, deploy, migrate —
and run them with `just build`, `just test`, `just
deploy`.

It looks like `make` on purpose, but it is **not a build
system**: it does not track file timestamps and never
decides that a target is "up to date" and silently skips
it. That single difference removes most of the reasons
`make` is unpleasant to use as a task runner.

## A justfile for a project in this wiki

```just
set dotenv-load                 # loads .env

default:                        # `just` with no args
    @just --list

clean:
    uv run s1_clean_inventory.py

images:
    uv run s2_clean_images.py

build: clean images
    uv run s3_build_site.py

serve: build
    uv run server.py

deploy branch="preview": build
    @echo "deploying to {{ branch }}"
    wrangler pages deploy ./dist --project-name site \
        --branch {{ branch }}

test:
    uv run pytest -q

fmt:
    ruff format .
```

`just deploy` ships a preview; `just deploy main` ships
production. `just --list` prints every recipe, which
makes the file its own README.

## Why not make

| | `make` / `gmake` | `just` |
|---|---|---|
| Purpose | Build files from files | Run named commands |
| Skips work if a file is newer | Yes — the classic surprise | No, always runs |
| Tabs required | Yes | No |
| `.PHONY` boilerplate | Every target | Never |
| Each line a separate shell | Yes | No, a recipe is one script |
| Arguments to a target | Awkward | `just deploy production` |
| `$` and shell quoting | Doubled `$$`, escaping rules | Ordinary shell |
| Runs from a subdirectory | Fails | Finds the justfile upwards |
| Variables from `.env` | Manual | `set dotenv-load` |

Make is excellent at what it was built for — compiling C
when the sources change. Almost nobody uses it for that
any more; they use it as a menu of project commands, and
for *that* job `just` is simply the better tool.

## Why it earns a place on the ladder

Every project in this wiki accumulates the same handful
of commands: build the site, run the server locally,
deploy, dump the database, rotate a key. They end up
scattered across a README, someone's shell history and
five numbered scripts.

A `justfile` puts them in one committed file, so:

- **Onboarding is `just --list`.** No archaeology.
- **CI runs exactly what you run.** The workflow calls
  `just test` and `just build`, so the pipeline cannot
  drift from the laptop
  ([[Continuous Integration and Delivery]]).
- **The [[Static Build Pipeline]] gets a front door.**
  The numbered scripts stay as they are; `just build`
  names the order once, and `just deploy` means nobody
  runs stage 4 having skipped stage 1.
- **Deploy steps stop being tribal knowledge**, which is
  half of what [[Git-Driven Deployment]] is trying to
  fix.

## Installing it

```bash
brew install just          # macOS and Linux, see Homebrew
cargo install just         # or from source
```

Single binary, written in [[Rust]], no runtime. On a
server it is one file to copy; there is nothing to
install alongside it.

## Watch out for

- **It is not a build system.** If you genuinely need
  incremental rebuilds based on file times, that is
  `make`, `ninja` or your language's own tool. `just`
  will happily run the slow thing every time.
- **Recipes run with `sh` by default.** Set
  `set shell := ["bash", "-uc"]` if you rely on bash
  features, and keep the strictness habits from
  [[Bash]].
- **`{{ }}` is just's own interpolation**, evaluated
  before the shell sees the line — a real source of
  confusion in recipes that also use `${}`.
- **Keep secrets out of it.** `set dotenv-load` reads
  `.env`, and `.env` stays out of git
  ([[Secrets Management]]).
- **Do not let it become a shell script in disguise.**
  A recipe longer than about ten lines wants to be a
  script that `just` calls.

## Related

[[Development Setup]] · [[Homebrew]] · [[Bash]] ·
[[Static Build Pipeline]] ·
[[Continuous Integration and Delivery]] ·
[[Git-Driven Deployment]] · [[Automated Testing]] ·
[[uv]] · [[Rust]] · [[Wrangler]] ·
[[Deployment Strategies]] · [[Twelve-Factor App]]

## Sources

- Upstream documentation: <https://just.systems/> and
  the manual at <https://just.systems/man/en/>. Not part
  of the downloaded `Raw/` corpus — related captures:
  [[github-actions-workflow-syntax]] ·
  [[12factor-dev-prod-parity]] ·
  [[cloudflare-wrangler-pages-commands]].
