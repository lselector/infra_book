---
type: Concept
title: "CORS"
description: "The browser rule that stops one origin reading another's responses, and the headers that relax it."
tags: [architectures, security]
timestamp: "2026-07-27T00:00:00Z"
---

# CORS

Cross-Origin Resource Sharing. Browsers block a page on
one origin from reading responses from another unless the
responding server opts in with headers.

## What you actually configure

- `Access-Control-Allow-Origin` — the specific origin, not
  `*`, once credentials are involved.
- `Access-Control-Allow-Methods` and `-Headers` — what the
  preflight `OPTIONS` request is told is permitted.
- `Access-Control-Allow-Credentials` — required if cookies
  or auth headers are sent.

## Why it matters here

It is the first thing that breaks in a
[[Single Page Application and API]] setup, because the
static frontend and the API are on different origins by
design. It is not an attack you are seeing; it is the
browser doing its job.

## Watch out for

- `Allow-Origin: *` with credentials is rejected by
  browsers, and would be a bad idea if it were not.
- CORS is not authorisation. It restricts browsers, not
  `curl`. Anything sensitive still needs
  [[Authentication]] and [[Authorization]].

## Related

[[Single Page Application and API]] · [[HTTP]] ·
[[Security Headers]] · [[Authorization]]

## Sources

- [[mdn-cors]] · [[mdn-fetch-api-using]]
