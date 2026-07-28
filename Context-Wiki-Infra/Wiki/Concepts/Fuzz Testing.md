---
type: Concept
title: "Fuzz Testing"
description: "Throwing generated garbage at your code until it breaks - the cheapest way to find the inputs you never imagined."
wikipedia: "https://en.wikipedia.org/wiki/Fuzzing"
tags: [ops-and-security, security, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Fuzz Testing

Feeding a program large volumes of generated input —
malformed, extreme, random, or mutated from real
examples — and watching for crashes, hangs, memory
errors and assertion failures.

Ordinary tests check the inputs you thought of. Fuzzing
finds the ones you did not, which is the same set an
attacker is looking for.

## The three kinds

**Coverage-guided (the modern kind).** The fuzzer
instruments the binary, watches which branches each input
reaches, and keeps inputs that reach new code, mutating
them further. It is a feedback loop, not random noise,
and it is why fuzzers find bugs behind three levels of
parsing. [[AFL++]] and libFuzzer work this way;
[[OSS-Fuzz]] runs them continuously for open-source
projects.

**Property-based.** You state a property that must always
hold and the tool generates inputs trying to break it,
then *shrinks* any failure to the smallest case that
still fails. Hypothesis (Python), fast-check
(JavaScript) and proptest (Rust) are the common ones.
This is the version most web developers should reach for
first.

```python
@given(st.text())
def test_slug_roundtrip(s):
    assert unslug(slug(s)) == s.strip()
    # fails on "", "---", and an emoji you had not considered
```

**Dumb / mutation.** Take a valid input, corrupt bytes at
random, submit it. Crude, requires no instrumentation,
and still finds things in file parsers and network
protocols.

## What it is good at

- Parsers of every kind: JSON, XML, CSV, images, archives,
  dates, URLs, user-supplied templates.
- Anything with a length, an index or an offset in it.
- Memory-unsafe code — C and C++, and `unsafe` blocks in
  [[Rust]]. Combine with sanitizers (ASan, UBSan) so
  corruption is caught at the moment it happens rather
  than three functions later.
- Decoders reachable from untrusted input, which is the
  attack surface [[OWASP Top 10]] injection findings
  usually start from.

## What it will not find

Business-logic flaws. A fuzzer does not know that a
discount should stop at 100% or that user A must not read
user B's invoices — that is [[Penetration Testing]] and
manual review. Fuzzing finds *crashes and violations of
stated properties*, not misplaced authorisation.

## Doing it on a small project

1. Pick the function that eats untrusted input. There is
   usually exactly one obvious candidate.
2. Write three or four property tests around it with
   Hypothesis or the equivalent ([[pytest]] integrates
   directly).
3. Run them in [[Continuous Integration and Delivery]]
   with a fixed seed budget so the build stays fast.
4. **Keep every failing input as a regression test**,
   with its shrunk minimal form. That is where the value
   compounds.
5. If you ship a library that parses anything, consider
   [[OSS-Fuzz]] — it is free for open source and runs
   continuously.

## Watch out for

- **Fuzzing has no natural end.** Budget time, not
  completion.
- **A crash is not automatically a vulnerability** — but
  it is automatically a bug, and it is where you look
  next.
- **Do not fuzz production.** Fuzz a local build; fuzzing
  a live service is a denial-of-service test you did not
  authorise ([[Security Testing]] on authorisation).

## Related

[[Automated Testing]] · [[Security Testing]] ·
[[Penetration Testing]] · [[Red Team and Blue Team]] ·
[[AFL++]] · [[OSS-Fuzz]] · [[pytest]] · [[Rust]] ·
[[OWASP Top 10]] · [[Dependency Auditing]] ·
[[Continuous Integration and Delivery]]

## Sources

- [[owasp-wstg]] · [[owasp-asvs]] ·
  [[owasp-input-validation-cheatsheet]] ·
  [[portswigger-web-security-academy]] ·
  [[github-code-scanning]]
