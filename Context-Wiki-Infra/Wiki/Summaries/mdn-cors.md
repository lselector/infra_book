---
type: Summary
title: "Cross-Origin Resource Sharing (CORS) (MDN)"
description: "Baseline Widely available This feature is well established and works across many devices and browser versions."
resource: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS"
source_file: "Raw/02_architectures/mdn-cors.md"
tags: [architectures, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Cross-Origin Resource Sharing (CORS) (MDN)

Extractive digest of the immutable capture in
`Raw/02_architectures/mdn-cors.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS>

## Opening

> Baseline  Widely available
> This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.
> An example of a cross-origin request: the front-end JavaScript code served from `https://domain-a.com` uses [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch\(\)") to make a request for `https://domain-b.com/data.json`.
> For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts. For example, `fetch()` and [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) follow the [same-origin ...

## Contents of the source document

- Cross-Origin Resource Sharing (CORS)
  - What requests use CORS?
  - Functional overview
  - Examples of access control scenarios
    - Simple requests
    - Preflighted requests
    - Requests with credentials
  - The HTTP response headers
    - Access-Control-Allow-Origin
    - Access-Control-Expose-Headers
    - Access-Control-Max-Age
    - Access-Control-Allow-Credentials
    - Access-Control-Allow-Methods
    - Access-Control-Allow-Headers
  - The HTTP request headers
    - Origin
    - Access-Control-Request-Method
    - Access-Control-Request-Headers

## Related pages

[[Authentication]] · [[Authorization]] · [[CORS]] · [[HTTP]]
