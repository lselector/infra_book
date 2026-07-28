---
type: Summary
title: "429 Too Many Requests (MDN)"
description: "The HTTP 429 Too Many Requests client error response status code indicates the client has sent too many requests in a given amount of time."
resource: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429"
source_file: "Raw/12_ai_in_saas/mdn-http-429.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# 429 Too Many Requests (MDN)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/mdn-http-429.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429>

## Opening

> The HTTP **`429 Too Many Requests`** [client error response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#client_error_responses) status code indicates the client has sent too many requests in a given amount of time. This mechanism of asking the client to slow down the rate of ...
> A [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After) header may be included to this response to indicate how long a client should wait before making the request again.
> Implementations of rate limiting vary; restrictions may be server-wide or per resource. Typically, rate-limiting restrictions are based on a client's IP but can be specific to users or authorized applications if requests are authenticated or contain a ...
> http

## Contents of the source document

- 429 Too Many Requests
  - Status
  - Examples
    - Response containing Retry-After header
  - Specifications
- section-4](https://www.rfc-editor.org/info/rfc6585/#section-4)
  - See also
  - Help improve MDN

## Related pages

[[HTTP]] · [[Rate Limiting]]
