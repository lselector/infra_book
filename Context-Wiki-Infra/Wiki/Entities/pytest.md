---
type: Tool
title: "pytest"
description: "The Python test runner - plain assert statements, fixtures instead of setup boilerplate, and the plugins worth having."
wikipedia: "https://en.wikipedia.org/wiki/Pytest"
tags: [tooling, python, dev-environment]
timestamp: "2026-07-28T00:00:00Z"
---

# pytest

The de facto test framework for Python. A test is a
function whose name starts with `test_` and whose body
uses the ordinary `assert` statement; pytest rewrites the
assertion so a failure prints both sides of the
comparison.

```python
def test_slugify():
    assert slugify("Hello World") == "hello-world"
```

No class to subclass, no `assertEqual`, no boilerplate —
which matters because the friction of writing a test is
the reason tests do not get written.

## Fixtures

Setup and teardown as dependency injection. Declare what
a test needs as a parameter; pytest builds it, caches it
at the scope you choose, and tears it down after.

```python
@pytest.fixture
def db():
    conn = connect(TEST_URL)
    yield conn                # test runs here
    conn.rollback()           # always cleaned up
```

This is what makes integration tests against a real
[[PostgreSQL]] practical: a transaction per test, rolled
back at the end, so tests are isolated without rebuilding
the schema each time.

## The parts you will use

- `-x` stop at first failure, `-k pattern` select by
  name, `--lf` re-run only last failures.
- `@pytest.mark.parametrize` — one test, many cases.
  Usually the answer when you are about to copy-paste a
  test.
- `pytest.raises` for expected exceptions.
- `conftest.py` for fixtures shared across a directory.
- Plugins: `pytest-cov` (coverage), `pytest-xdist`
  (parallel), `pytest-asyncio`, and Hypothesis for
  property-based [[Fuzz Testing]] — which plugs in as
  ordinary pytest tests.

## In this stack

Run it in [[Continuous Integration and Delivery]] on
every push, alongside `pip-audit` for
[[Dependency Auditing]]. Install it with [[uv]]
(`uv run pytest`) so the test environment is the locked
one rather than whatever is on the machine. For a
[[FastAPI]] app, `TestClient` plus pytest covers the API
layer without starting a server.

## Watch out for

- **Fixtures with `scope="session"` that hold state**
  leak between tests and produce order-dependent
  failures. Run with `-p no:randomly` off — that is,
  shuffle — occasionally to find them.
- **Mocking the database** tests the mock. Prefer a real
  one in a container ([[Docker Compose]]).
- **Coverage as a target** rather than a diagnostic; see
  [[Automated Testing]].

## Related

[[Automated Testing]] · [[Fuzz Testing]] ·
[[Playwright]] · [[Continuous Integration and Delivery]]
· [[FastAPI]] · [[PostgreSQL]] · [[uv]] ·
[[Docker Compose]] · [[Dependency Auditing]] ·
[[GitHub Actions]]

## Sources

- Upstream documentation: <https://docs.pytest.org/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet. CI integration:
  [[github-actions-workflow-syntax]] ·
  [[pip-audit-readme]].
