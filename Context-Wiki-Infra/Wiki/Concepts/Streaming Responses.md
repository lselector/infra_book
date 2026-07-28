---
type: Concept
title: "Streaming Responses"
description: "Server-sent events from your API to the chat panel - and the proxies, timeouts and buffers that quietly break them."
wikipedia: "https://en.wikipedia.org/wiki/Server-sent_events"
tags: [ai-in-saas, architectures, performance]
timestamp: "2026-07-28T00:00:00Z"
---

# Streaming Responses

A model generates tokens one at a time over several
seconds. Waiting for the whole reply and then rendering
it feels broken; streaming the text as it arrives feels
fast even when it is not. Every chat UI streams, and the
mechanism is older and simpler than the AI feature that
made it fashionable.

## Pick the boring transport

| Transport | Direction | Use when |
|---|---|---|
| **Server-sent events (SSE)** | server → client | the default for chat replies |
| Chunked `fetch` + `ReadableStream` | server → client | you need custom headers or POST bodies |
| WebSocket | both ways | live collaboration, not chat replies |

SSE is plain HTTP with `Content-Type: text/event-stream`,
a stream of `data:` lines, and automatic client
reconnection. It survives proxies, needs no new protocol
in your stack, and requires no [[Sticky Sessions]] if
each stream is a single request.

The one real limitation of the `EventSource` API is that
it only issues GETs with no custom headers, which is
awkward when the request carries a long message and a
bearer token. The common answer is a streaming `fetch()`
POST that parses the same SSE framing by hand — the wire
format stays standard, only the client parser changes.

## The shape on your side

Your endpoint opens the provider stream, and forwards
text deltas as they arrive:

    data: {"delta": "Sure, the invoice "}
    data: {"delta": "was voided on 3 May."}
    data: {"done": true, "message_id": 91}

Forward *your* events, not the provider's raw ones. You
want to add message ids, drop provider internals, and
keep the panel working after a provider change.

Also emit a heartbeat comment (`: ping`) every 15-30
seconds during long silences, or an idle-timeout
somewhere in the path will close the connection during a
long generation.

## What breaks it

Almost every streaming bug is buffering somewhere in the
middle. Symptom: the whole reply appears at once, at the
end.

- **nginx** buffers proxied responses by default. Set
  `proxy_buffering off;` for the endpoint, or send
  `X-Accel-Buffering: no` from the app
  ([[Reverse Proxy]]).
- **Caddy** streams by default, but compression can
  still batch; disable `encode` on the stream route if
  chunks arrive late.
- **Compression middleware** in your own framework will
  happily buffer to make a bigger gzip block. Exclude
  `text/event-stream`.
- **Load balancer idle timeouts** cut long generations —
  raise them, or heartbeat.
- **Serverless platforms** vary: some buffer the whole
  response, some cap request duration well below the time
  a long answer takes. Check before designing around it
  ([[Serverless Architecture]]).

## Reconnection is not resumption

`EventSource` reconnects automatically and replays
`Last-Event-ID`, and that is genuinely useful for event
feeds. A model stream is not resumable: the provider will
not continue a generation you dropped.

So make the server the source of truth. Persist the
finished message when the generation completes, and on
reconnect have the panel re-fetch the thread rather than
try to resume the stream. If the user's laptop slept
mid-answer, the answer is waiting for them in the thread.

## Cancel means cancel

When the user hits stop or closes the panel, the client
aborts the request. Your handler must notice the
disconnect and cancel the upstream provider call. If it
does not, generation continues to completion and you are
billed for text nobody will ever see — a small leak that
scales exactly with how impatient your users are
([[Usage Quotas and Metering]]).

## Watch out for

- **Partial output is not a complete answer.** Save it as
  cancelled, not as the assistant's reply.
- **Errors mid-stream.** The HTTP status was already 200.
  Send an explicit `event: error` and render it.
- **Markdown arrives in fragments.** Render progressively
  but sanitise on every paint, or an unclosed code fence
  becomes an HTML injection ([[Security Headers]]).
- **Connection budget.** Every open stream is a held
  connection and, on some stacks, a held worker. Cap
  concurrent streams per user ([[Rate Limiting]]).

## Related

[[AI Assistant Panel]] · [[LLM API Integration]] ·
[[Reverse Proxy]] · [[Sticky Sessions]] · [[HTTP]] ·
[[Serverless Architecture]] · [[Rate Limiting]] ·
[[Caddy]] · [[Nginx]] · [[Vercel AI SDK]]

## Sources

- [[mdn-server-sent-events]] · [[mdn-eventsource]] ·
  [[anthropic-streaming]] · [[nginx-reverse-proxy-guide]]
  · [[caddy-quickstart-reverse-proxy]] ·
  [[vercel-ai-sdk-introduction]] · [[mdn-http-overview]]
