---
type: Summary
title: "An overview of HTTP (MDN)"
description: "Clients and servers communicate by exchanging individual messages (as opposed to a stream of data)."
resource: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview"
source_file: "Raw/01_foundations/mdn-http-overview.md"
tags: [foundations, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# An overview of HTTP (MDN)

Extractive digest of the immutable capture in
`Raw/01_foundations/mdn-http-overview.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview>

## Opening

> Clients and servers communicate by exchanging individual messages (as opposed to a stream of data). The messages sent by the client are called _requests_ and the messages sent by the server as an answer are called _responses_.
> Designed in the early 1990s, HTTP is an extensible protocol which has evolved over time. It is an application layer protocol that is sent over [TCP](https://developer.mozilla.org/en-US/docs/Glossary/TCP), or over a [TLS](https://developer.mozilla.org/en-US/docs/Glossary/TLS)-encrypted TCP ...
> HTTP is a client-server protocol: requests are sent by one entity, the user-agent (or a proxy on behalf of it). Most of the time the user-agent is a Web browser, but it can be anything, for example, a robot that crawls the Web to populate and maintain a search engine index.
> Each individual request is sent to a server, which handles it and provides an answer called the _response_. Between the client and the server there are numerous entities, collectively called [proxies](https://developer.mozilla.org/en-US/docs/Glossary/Proxy_server), which perform different ...

## Contents of the source document

- Overview of HTTP
  - Components of HTTP-based systems
    - Client: the user-agent
    - The Web server
    - Proxies
  - Basic aspects of HTTP
    - HTTP is simple
    - HTTP is extensible
    - HTTP is stateless, but not sessionless
    - HTTP and connections
  - What can be controlled by HTTP
  - HTTP flow
  - HTTP Messages
    - Requests
    - Responses
  - APIs based on HTTP
  - Conclusion
  - See also

## Related pages

[[Authentication]] · [[HTTP]] · [[Load Balancing]]
