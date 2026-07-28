---
type: Tool
title: "AFL++"
description: "The coverage-guided fuzzer most others descend from - instrument, mutate, keep what reaches new code."
wikipedia: "https://en.wikipedia.org/wiki/American_Fuzzy_Lop_(software)"
tags: [tooling, security]
timestamp: "2026-07-28T00:00:00Z"
---

# AFL++

A coverage-guided fuzzer: the community-maintained
successor to American Fuzzy Lop (AFL), with the research
improvements of the last decade folded in.

## How it works

1. **Instrument the target at compile time**
   (`afl-clang-fast`), so every branch taken is recorded.
2. **Start from seed inputs** — a few small, valid
   examples of what the program parses.
3. **Mutate** them: flip bits, splice inputs, insert
   dictionary tokens.
4. **Keep any input that reaches a new branch**, and
   mutate that further.

The feedback loop in step 4 is the whole idea. Random
input would never guess a valid ZIP header; a fuzzer that
notices "this input got one branch deeper" walks into the
parser one condition at a time.

## What to point it at

Code that parses untrusted bytes: file formats, network
protocols, decompressors, image and media handling,
template engines. It is at its most valuable against
memory-unsafe languages, where the bugs it finds are
buffer overflows rather than exceptions.

Build with sanitizers on (`AFL_USE_ASAN=1`) so memory
corruption is caught at the moment it occurs. A crash
without a sanitizer often does not reproduce; with one it
comes with a stack trace pointing at the exact write.

## Whether you need it

Most web and SaaS work does not. If you write Python,
JavaScript or safe [[Rust]] over a database, the
practical form of [[Fuzz Testing]] is property-based
testing in [[pytest]] with Hypothesis, and the practical
security work is [[Security Testing]] and
[[Dependency Auditing]].

AFL++ becomes relevant when you **ship a parser** — a
library, a file-format handler, a protocol
implementation, C or C++ code, or `unsafe` Rust. Then it
is the standard tool, and [[OSS-Fuzz]] will run it for
you continuously if the project is open source.

## Watch out for

- **Seeds matter more than runtime.** Good small valid
  inputs, plus a dictionary of the format's keywords,
  outperform days of extra fuzzing from a blank file.
- **It runs until you stop it.** Set a time budget.
- **Crashes need triaging and de-duplicating** — many
  distinct inputs usually hit one bug.
- **Only on code you own or are authorised to test**, and
  never against a live service ([[Penetration Testing]]
  on authorisation).

## Related

[[Fuzz Testing]] · [[OSS-Fuzz]] · [[Security Testing]] ·
[[Penetration Testing]] · [[Rust]] · [[pytest]] ·
[[Automated Testing]] · [[CodeQL]] · [[OWASP Top 10]]

## Sources

- Upstream documentation: <https://aflplus.plus/>.
  Not part of the downloaded `Raw/` corpus — related
  captures: [[owasp-wstg]] · [[owasp-asvs]] ·
  [[github-code-scanning]].
