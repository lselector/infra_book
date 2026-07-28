---
type: Tool
title: "GNU Make"
description: "make / gmake - the build tool on every machine, what it is genuinely good at, and why people misuse it as a task runner."
wikipedia: "https://en.wikipedia.org/wiki/Make_(software)"
tags: [tooling, dev-environment, deployments]
timestamp: "2026-07-28T00:00:00Z"
---

# GNU Make

The build automation tool: a `Makefile` declares
**targets**, their **prerequisites**, and the recipe that
produces one from the others. Make compares file
timestamps and runs only the recipes whose inputs are
newer than their outputs.

```make
site/index.html: content/index.md template.html
	pandoc $< --template template.html -o $@

.PHONY: clean
clean:
	rm -rf site/
```

`$@` is the target, `$<` the first prerequisite, and the
recipe lines **must** start with a tab.

## make, gmake, and macOS

`gmake` is GNU Make invoked under a name that
distinguishes it from BSD make, which owns `make` on the
BSDs. On macOS the situation is worse than it looks:
`/usr/bin/make` *is* GNU Make, but version **3.81** from
2006, kept for licence reasons. Anything written against
a modern Makefile may fail on it.

```bash
brew install make        # installs GNU Make 4.x as gmake
gmake --version
```

Scripts that must work everywhere either target 3.81 or
call `gmake` explicitly — which is where the habit of
writing `gmake` in documentation comes from.

## What it is genuinely excellent at

**Incremental work driven by file timestamps.** If your
build has expensive steps that only need redoing when
their inputs change, Make is still the right answer and
nothing here replaces it:

- Compiling C/C++ — the job it was built for in 1976.
- Rendering documents, LaTeX, diagrams, static pages from
  sources.
- Data pipelines where a stage takes minutes and the
  input rarely changes.
- Anything parallelisable: `make -j8` runs independent
  branches of the dependency graph concurrently, for free.

If you find yourself writing "skip this if the output is
newer" in a script, you are reimplementing Make badly.

## Why it is uncomfortable as a task runner

Most `Makefile`s in web projects contain no file
dependencies at all — they are a menu of commands
(`make test`, `make deploy`), and every feature above
becomes friction:

- **Timestamp logic you do not want.** A target named
  `test` silently does nothing if a file called `test`
  exists. Hence `.PHONY` on every target, forever.
- **Tabs are syntactic**, and an editor that helpfully
  inserts spaces produces `missing separator`.
- **Each recipe line is its own shell**, so `cd build`
  does not affect the next line; you chain with `&&` and
  `\`.
- **`$` is doubled** (`$$HOME`), because Make expands
  variables before the shell sees them.
- **Arguments are awkward** — `make deploy ENV=prod`
  rather than `deploy prod`.
- **It expects to run from its own directory.**

None of these are bugs. They are the cost of a build
system, charged to a use case that is not a build.

## The three in this family

| | **GNU Make** | [[just]] | [[Invoke]] |
|---|---|---|---|
| Kind | Build system | Command runner | Task runner |
| Language | Makefile syntax | justfile syntax | Python |
| Skips work by timestamp | **Yes** | No | No |
| Installed already | Almost always | `brew install just` | `pip`/`uv` |
| Best for | File → file builds | Project commands | Commands needing real logic |

Rule of thumb: **if the tool should decide whether to do
the work, use Make. If you decide, use [[just]] — or
[[Invoke]] when the task needs actual programming.**

## Watch out for

- **A `Makefile` that is 90% `.PHONY`** is telling you it
  wants to be a [[just]] file.
- **Recursive make** across subdirectories loses the
  dependency graph and the parallelism with it.
- **Non-deterministic timestamps** — a `git checkout`
  updates mtimes, so CI often rebuilds everything anyway
  ([[Continuous Integration and Delivery]] caches the
  artifacts instead, see [[Docker Build Cache]]).
- **Version drift** between GNU Make 3.81 on macOS and
  4.x on Linux, which is a
  [[Twelve-Factor App|dev/prod parity]] problem in
  miniature.

## Related

[[just]] · [[Invoke]] · [[Development Setup]] ·
[[Homebrew]] · [[Bash]] · [[Static Build Pipeline]] ·
[[Continuous Integration and Delivery]] ·
[[Docker Build Cache]] · [[Container Images]] ·
[[Twelve-Factor App]]

## Sources

- Upstream documentation:
  <https://www.gnu.org/software/make/manual/>. Not part
  of the downloaded `Raw/` corpus — related captures:
  [[12factor-dev-prod-parity]] ·
  [[docker-build-best-practices]] ·
  [[github-actions-workflow-syntax]].
