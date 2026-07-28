---
type: Summary
title: "Streaming Messages (Anthropic)"
description: "Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas."
resource: "https://platform.claude.com/docs/en/build-with-claude/streaming.md"
source_file: "Raw/12_ai_in_saas/anthropic-streaming.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Streaming Messages (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-streaming.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/build-with-claude/streaming.md>

## Opening

> Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
> When creating a Message, you can set `"stream": true` to incrementally stream the response using [server-sent events](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents) (SSE).
> The [Python SDK](https://github.com/anthropics/anthropic-sdk-python) and [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript) offer multiple ways of streaming. The [PHP SDK](https://github.com/anthropics/anthropic-sdk-php) provides streaming through `createStream()`. The Python ...
> <CodeGroup>

## Contents of the source document

- Streaming messages
  - Streaming with SDKs
  - Get the final message without handling events
  - Event types
    - Ping events
    - Error events
    - Other events
  - Content block delta types
    - Text delta
    - Input JSON delta
    - Thinking delta
  - Full HTTP stream response
    - Basic streaming request
    - Streaming request with tool use
    - Streaming request with thinking
    - Streaming request with web search tool use
  - Error recovery
    - Claude 4.5 and earlier

## Related pages

[[HTTP]]
