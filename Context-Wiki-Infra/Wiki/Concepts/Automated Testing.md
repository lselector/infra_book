---
type: Concept
title: "Automated Testing"
description: "The tests worth writing on a small project, in the order they pay off - and the one that pays off first."
wikipedia: "https://en.wikipedia.org/wiki/Test_automation"
tags: [ops-and-security, deployments, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Automated Testing

Checks that run without a human, on every push. The
question for a small team is never "should we test" but
**which tests earn their maintenance cost**, and the
answer is a specific short list.

## The layers, cheapest first

| Layer | What it covers | Cost to keep |
|---|---|---|
| **Type checks / linting** | Whole classes of typo and shape error | Almost none |
| **Unit tests** | One function's logic, especially edge cases | Low |
| **Integration tests** | Your code against a real database or API | Medium |
| **End-to-end tests** | A browser doing what a user does | High |
| **Smoke test after deploy** | "Is production actually up?" | Almost none |

Most small projects over-invest in the middle and skip
both ends. The two cheapest rows catch a surprising
share of real breakage.

## The first four tests to write

1. **A smoke test that hits the deployed URL** and
   asserts 200 plus one string from the page. It catches
   the deploy that succeeded and the site that did not.
2. **The money path.** Signup, checkout, whatever
   produces revenue — one end-to-end test
   ([[Playwright]]).
3. **The thing that broke last time.** Every bug fix gets
   a test that fails without the fix. This is the
   highest-value test you will ever write, because it is
   the only one aimed at a failure you *know* happens.
4. **A restore test.** Restoring last night's backup into
   a scratch database and counting rows is a test, and
   the one most likely to save the company
   ([[Database Backups]]).

## Where they run

In [[Continuous Integration and Delivery]], on every
push, with the build failing loudly when they fail. A
test suite that only runs on someone's laptop is
documentation.

Integration tests want a real dependency, not a mock of
one — a [[PostgreSQL]] container started by
[[Docker Compose]] in CI, torn down after. Mocking the
database mostly tests the mock.

## What to test in infrastructure

- **The config parses.** `caddy validate`,
  `nginx -t`, `docker compose config`,
  `terraform validate` — seconds each, and they catch the
  deploy that would have taken the site down.
- **Migrations run forward on a copy of production data**,
  not on an empty schema.
- **The health endpoint** returns non-200 when a
  dependency is missing, rather than always 200
  ([[Failure Modes]]).

## Watch out for

- **Flaky tests are worse than no tests.** A suite that
  fails randomly trains everyone to re-run it, and then
  to ignore it. Fix or delete; do not tolerate.
- **Coverage percentages are not a goal.** 90% coverage
  of getters says nothing about whether checkout works.
- **Slow suites do not get run.** Keep the push-time
  suite under a few minutes; move the rest to nightly.
- **Tests are not a security review.** They check what
  you thought of; [[Security Testing]], [[Fuzz Testing]]
  and [[Penetration Testing]] look for what you did not.

## Related

[[Continuous Integration and Delivery]] ·
[[Fuzz Testing]] · [[Security Testing]] ·
[[Chaos Engineering]] · [[Deployment Environments]] ·
[[Deployment Strategies]] · [[Database Backups]] ·
[[pytest]] · [[Playwright]] · [[GitHub Actions]] ·
[[Failure Modes]] · [[Twelve-Factor App]]

## Sources

- [[github-actions-understanding]] ·
  [[github-actions-workflow-syntax]] ·
  [[12factor-dev-prod-parity]] ·
  [[roadmap-sh-devops]] · [[django-deployment-checklist]]
