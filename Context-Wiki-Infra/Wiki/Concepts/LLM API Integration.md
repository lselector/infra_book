---
type: Concept
title: "LLM API Integration"
description: "Calling a model provider from your backend - the proxy endpoint, model choice, caching, retries, and what to log."
wikipedia: "https://en.wikipedia.org/wiki/Large_language_model"
tags: [ai-in-saas, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# LLM API Integration

A model provider is a [[Twelve-Factor App|backing
service]] like any other: an HTTPS API, a key, a bill,
and an SLA you do not control. The integration is
ordinary backend work — the only unusual parts are that
responses take seconds, the price is per token, and the
output is untrusted.

## The proxy endpoint is the design

Everything goes through one server-side endpoint:

    browser  ->  your API  ->  provider API
                    |
                    +-- auth, quota, rate limit,
                        prompt assembly, logging

Putting a provider key in the browser — or in a mobile
app, or in a Cloudflare Worker that anyone can call
without a session — is the same class of mistake as
shipping your database password. Keys live in a secret
store and are read from the environment
([[Secrets Management]]).

## The request

Four fields carry the weight:

- **`model`** — an explicit pinned id, never "latest".
- **`max_tokens`** — a hard ceiling on the reply.
- **`system`** — your stable instructions. Keep it
  byte-identical between requests so it can be cached.
- **`messages`** — the conversation, oldest first.

A minimal call with the vendor SDK:

```python
import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY
msg = client.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    system=SYSTEM_PROMPT,
    messages=[{"role": "user", "content": question}],
)
```

The API is **stateless**: there is no conversation on the
provider's side. You resend the whole thread every turn,
and you pay for it every turn. That single fact drives
caching, context trimming, and most of the cost curve.

## Choosing a model

| Want | Reach for |
|---|---|
| The default for real work | the top-tier model |
| High volume, simple turns | the mid-tier model |
| Classification, routing, extraction | the small model |

Prices are per million tokens and differ by roughly an
order of magnitude between tiers, so routing cheap work
to a cheap model is the largest cost lever you have —
larger than prompt tuning. Do it per feature, not per
user, and keep the tier in your usage records so you can
see the split ([[Usage Quotas and Metering]]).

## Four provider features worth using immediately

**Streaming.** Required in practice for anything long:
it shows progress and it keeps the HTTP connection from
idling out. See [[Streaming Responses]].

**Prompt caching.** Providers cache a stable *prefix* of
the request — system prompt, tool definitions, retrieved
documents — and charge a fraction of the input price to
re-read it. Cache reads are cheap; cache writes cost a
premium, so it pays off from the second request. The
trap is that it is a byte-exact prefix match: a timestamp
or a per-request id near the front of the system prompt
silently disables it. Put stable content first, volatile
content last, and check the cache-read counter in the
response ([[Caching]]).

**Batch processing.** Offline work — nightly summaries,
backfills, evaluations — goes through a batch endpoint at
roughly half price, in exchange for asynchronous
delivery. If a job does not have a user waiting on it,
it should not be paying interactive prices.

**Context window accounting.** The window is large but
finite, and it is shared by the system prompt, the
retrieved documents, the whole thread and the reply.
Decide up front what gets dropped first — usually the
middle of the thread, summarised.

## Failure handling

The provider will return 429 and 5xx. Treat it exactly
like any other flaky dependency:

- Retry only 429, 5xx and connection errors — never 400.
- Exponential backoff **with jitter**, honouring
  `Retry-After` when present ([[Retry Storm]]).
- Retry in one place. Most SDKs already retry twice by
  default; do not wrap that in your own loop.
- Set a timeout and a concurrency cap, so a slow provider
  cannot exhaust your workers ([[Cascading Failure]]).
- Have a defined degraded state: the panel says the
  assistant is unavailable and the rest of the product
  keeps working. AI is a feature, not a dependency of
  checkout.

## What to log for every call

Tenant, user, feature, model, input tokens, output
tokens, cached tokens, latency, stop reason, provider
request id, and the estimated cost. This one record
answers "why is the bill like that", "who is abusing
it", and "did that deploy make it slower" — see
[[Monitoring and Alerting]].

## Staying portable

Wrap the provider in one module with a narrow interface
(`complete(system, messages, tools) -> stream`). Model
ids, retries, token accounting and the SDK live behind
it. Providers deprecate models on a schedule measured in
months, so the swap will happen whether or not you plan
for it. Do not chase a lowest-common-denominator
abstraction across every vendor — the useful features
(caching, tool use, streaming shapes) differ, and the
abstraction that hides them costs more than it saves.

## Watch out for

- **Serverless timeouts.** A 60-second platform limit and
  a 90-second generation do not mix ([[Cold Starts]],
  [[Serverless Architecture]]).
- **Client disconnects.** If the user closes the panel and
  you do not cancel, you pay for tokens nobody reads.
- **Token counts are not word counts.** Use the
  provider's counting endpoint rather than a heuristic,
  and re-measure after a model change.
- **Model output is untrusted input.** It gets rendered,
  stored, and sometimes executed — see
  [[Prompt Injection]] and [[Tool Calling]].

## Related

[[AI Assistant Panel]] · [[Streaming Responses]] ·
[[Usage Quotas and Metering]] · [[Rate Limiting]] ·
[[Claude API]] · [[Cloudflare AI Gateway]] ·
[[Secrets Management]] · [[Retry Storm]] ·
[[Cost Control]] · [[Caching]] · [[Vercel AI SDK]]

## Sources

- [[anthropic-models-overview]] · [[anthropic-pricing]] ·
  [[anthropic-streaming]] · [[anthropic-prompt-caching]] ·
  [[anthropic-context-windows]] ·
  [[anthropic-batch-processing]] · [[anthropic-errors]] ·
  [[anthropic-rate-limits]] · [[12factor-backing-services]]
