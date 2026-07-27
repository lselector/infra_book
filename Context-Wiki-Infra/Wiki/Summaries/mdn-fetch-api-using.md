---
type: Summary
title: "Using the Fetch API (MDN)"
description: "The Fetch API provides a JavaScript interface for making HTTP requests and processing the responses."
resource: "https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch"
source_file: "Raw/02_architectures/mdn-fetch-api-using.md"
tags: [architectures, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Using the Fetch API (MDN)

Extractive digest of the immutable capture in
`Raw/02_architectures/mdn-fetch-api-using.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>

## Opening

> The [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) provides a JavaScript interface for making HTTP requests and processing the responses.
> Fetch is the modern replacement for [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest): unlike `XMLHttpRequest`, which uses callbacks, Fetch is promise-based and is integrated with features of the modern web such as [service ...
> With the Fetch API, you make a request by calling [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch\(\)"), which is available as a global function in both [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window "window") and ...
> The `fetch()` function returns a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is fulfilled with a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object representing the server's response. You can then check the ...

## Contents of the source document

- Using the Fetch API
  - Making a request
    - Setting the method
    - Setting a body
    - Setting headers
    - Sending data in a GET request
    - Making cross-origin requests
    - Including credentials
    - Creating a Request object
  - Canceling a request
  - Handling the response
    - Checking response status
    - Checking the response type
    - Checking headers
    - Reading the response body
    - Streaming the response body
    - Processing a text file line by line
    - Locked and disturbed streams

## Related pages

[[Authorization]] · [[CORS]] · [[HTTP]] · [[Service Worker]]
