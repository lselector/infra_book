---
type: Tool
title: "Playwright"
description: "Browser automation for end-to-end tests - auto-waiting that kills most flakiness, and a headless browser in CI."
wikipedia: "https://en.wikipedia.org/wiki/Playwright_(software)"
tags: [tooling, frontend, dev-environment]
timestamp: "2026-07-28T00:00:00Z"
---

# Playwright

Microsoft's browser automation library. It drives
Chromium, Firefox and WebKit from JavaScript, Python,
Java or .NET, and is the current default choice for
end-to-end tests of a web app.

```python
def test_signup(page):
    page.goto("https://staging.example.com")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Email").fill("a@example.com")
    page.get_by_role("button", name="Create").click()
    expect(page.get_by_text("Check your inbox")).to_be_visible()
```

## Why it replaced the previous generation

**Auto-waiting.** Every action waits for the element to
be attached, visible, stable and enabled before acting.
That single design decision removes the `sleep(2)` calls
that made older end-to-end suites flaky, and flakiness is
the reason such suites get abandoned
([[Automated Testing]]).

Also worth having: **tracing** (a recorded timeline with
DOM snapshots for every failure, which turns "it failed
in CI" into something you can actually inspect),
**`codegen`** to record a flow into a starting script,
and **real mobile emulation** for checking a
[[Responsive Design]] layout.

## Where it fits

One or two tests on the money path — signup, checkout,
the core flow — run against a preview or staging
deployment in [[Continuous Integration and Delivery]]
after deploy ([[Deployment Environments]]). That is the
whole recommended investment for a small product; the
maintenance cost of a large end-to-end suite is real, and
it grows with every UI change.

It is also the honest way to verify a
[[Progressive Web App]] or a
[[Single Page Application and API]], where a `curl` of
the HTML proves nothing because the page is assembled in
the browser.

## Watch out for

- **Selector choice decides maintenance cost.** Use roles
  and labels (`get_by_role`, `get_by_label`) — they
  survive redesigns and double as an accessibility check.
  CSS paths do not.
- **Browsers must be installed in CI**
  (`playwright install --with-deps`), and the download is
  large — cache it ([[Docker Build Cache]] and CI caches
  both apply).
- **Test data.** An e2e test that signs up
  `a@example.com` twice fails the second time. Generate
  unique data, or clean up.
- Do not test everything through the browser; it is the
  slowest and most brittle layer by an order of
  magnitude.

## Related

[[Automated Testing]] · [[pytest]] ·
[[Continuous Integration and Delivery]] ·
[[Deployment Environments]] · [[Responsive Design]] ·
[[Progressive Web App]] ·
[[Single Page Application and API]] ·
[[Core Web Vitals]] · [[GitHub Actions]]

## Sources

- Upstream documentation: <https://playwright.dev/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet. CI integration:
  [[github-actions-workflow-syntax]].
