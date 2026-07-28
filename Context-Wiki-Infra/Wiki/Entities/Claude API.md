---
type: Service
title: "Claude API"
description: "Anthropic's hosted models behind one Messages endpoint - streaming, prompt caching, batches and tool use."
wikipedia: "https://en.wikipedia.org/wiki/Claude_(AI)"
tags: [ai-in-saas]
timestamp: "2026-07-28T00:00:00Z"
---

# Claude API

Anthropic's developer API. One main endpoint —
`POST /v1/messages` — takes a model id, a system prompt
and a conversation, and returns a reply. Official SDKs
exist for Python, TypeScript, Java, Go, Ruby, C# and PHP;
everything else is plain HTTPS.

Used here as the worked example of
[[LLM API Integration]]. The competing providers expose
the same shape of thing; the reasoning transfers, the
field names do not.

## The call

```python
import anthropic

client = anthropic.Anthropic()   # ANTHROPIC_API_KEY
with client.messages.stream(
    model="claude-opus-5",
    max_tokens=4096,
    system=SYSTEM_PROMPT,
    messages=thread,
) as stream:
    for text in stream.text_stream:
        yield text
```

The API is stateless — you resend the thread each turn,
and you pay for it each turn.

## Model tiers

| Tier | For | Relative price |
|---|---|---|
| Opus | the default for real product work | highest |
| Sonnet | high-volume features | middle |
| Haiku | classification, routing, extraction | lowest |

Prices are quoted per million input and output tokens,
with output several times dearer than input, and the
spread between tiers is large enough that per-feature
model routing is the biggest cost lever you have
([[Usage Quotas and Metering]]). Pin an exact model id
rather than a moving alias, and expect to revisit it —
models are deprecated on a published schedule.

## The four features that change the architecture

- **Streaming** — server-sent events carrying text
  deltas. The default for anything a user waits on
  ([[Streaming Responses]]).
- **Prompt caching** — mark a stable prefix and re-read
  it at a fraction of the input price. Prefix match is
  byte-exact, so stable content goes first
  ([[Caching]]).
- **Message Batches** — asynchronous bulk processing at
  roughly half price, for work with nobody waiting.
- **Tool use** — the model requests a function call, your
  code executes it, the result goes back
  ([[Tool Calling]]). Remote [[Model Context Protocol]]
  servers can be connected the same way.

## Limits and errors

Rate limits are applied per organisation as requests per
minute and input/output tokens per minute, with the
remaining budget reported in response headers. Over the
limit is `429` with `Retry-After`; `500` and `529` mean
try again later; `400` never will be.

The SDKs already retry `429`, `408`, `409` and `5xx` with
backoff twice by default — do not wrap that in a second
loop ([[Retry Storm]]). Usage counts come back on every
response, which is what you record for
[[Usage Quotas and Metering]].

## Watch out for

- **The key is a server-side secret.** Read it from the
  environment, never ship it to a browser
  ([[Secrets Management]]).
- **Long generations need streaming**, or the request
  will sit past a proxy or platform timeout.
- **Caching fails silently.** A timestamp early in the
  system prompt costs you the whole discount and reports
  no error — watch the cache-read counter.
- **Token counts are model-specific.** Re-baseline after
  a model change rather than reusing old estimates.

## Related

[[LLM API Integration]] · [[AI Assistant Panel]] ·
[[Streaming Responses]] · [[Tool Calling]] ·
[[Model Context Protocol]] · [[Rate Limiting]] ·
[[Usage Quotas and Metering]] · [[Caching]] ·
[[Secrets Management]] · [[Cloudflare AI Gateway]] ·
[[Claude Code]]

## Sources

- [[anthropic-models-overview]] · [[anthropic-pricing]] ·
  [[anthropic-streaming]] · [[anthropic-prompt-caching]] ·
  [[anthropic-batch-processing]] · [[anthropic-tool-use]]
  · [[anthropic-rate-limits]] · [[anthropic-errors]] ·
  [[anthropic-context-windows]] ·
  [[anthropic-mcp-connector]]
