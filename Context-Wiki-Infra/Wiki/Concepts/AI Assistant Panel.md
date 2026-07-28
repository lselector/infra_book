---
type: Concept
title: "AI Assistant Panel"
description: "The side-panel chat bolted onto an existing SaaS - what it is made of, and the four things that make it safe to ship."
wikipedia: "https://en.wikipedia.org/wiki/Chatbot"
tags: [ai-in-saas, product-patterns, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# AI Assistant Panel

The now-standard way to put AI in a SaaS product: a
collapsible panel on the right-hand side of the app,
holding a chat with an assistant that can see what the
user is looking at.

It is a small feature with a large blast radius. The
chat box is two days of work; everything below is the
rest of it.

## What it is made of

| Piece | Lives in | Notes |
|---|---|---|
| Panel UI | your frontend | drawer, chat log, input, stop button |
| `/assistant/messages` | your backend | auth, limits, logging — the choke point |
| Context assembly | your backend | system prompt + tenant data + page context |
| Provider call | your backend | [[Claude API]] or equivalent |
| Thread storage | your database | `threads`, `messages`, both keyed by tenant |

The one non-negotiable: **the browser never talks to the
model provider.** It talks to your endpoint, which
authenticates the user, checks their quota, assembles the
prompt, and calls the provider with a key the browser has
never seen. Everything in [[LLM API Integration]],
[[Rate Limiting]] and [[Usage Quotas and Metering]] hangs
off that single endpoint existing.

## Why a side panel rather than a page

Because the panel knows where the user is. An assistant
opened on invoice 4471 should already have invoice 4471
in its context — the user should not have to describe
their own screen. Pass a small, explicit context object
with each turn:

    {"page": "invoice", "id": 4471, "tenant": 12}

Then resolve the ids **server-side**, from your own
database, with the user's own permissions. Never let the
client send the record contents — a client that can send
"here is invoice 9999" can read invoice 9999.

## The request path

1. Browser POSTs the user's message plus page context.
2. Backend authenticates ([[Authentication]]) and
   authorizes the referenced records
   ([[Authorization]]).
3. Backend checks the tenant's quota and rate limit.
4. Backend loads the thread, fetches the record data,
   and builds the prompt.
5. Backend calls the provider with streaming on.
6. Deltas stream back to the panel as they arrive
   ([[Streaming Responses]]).
7. Backend writes the finished message, the token counts
   and the cost to storage.

Step 7 is not optional. Without it there is no usage
history, no per-tenant cost, no abuse signal, and nothing
to show an auditor.

## Storage

Two tables, both with a `tenant_id` column and a foreign
key to the user:

- `assistant_threads` — id, tenant, user, title, created.
- `assistant_messages` — thread, role, content, model,
  input/output tokens, cost, created.

Set a retention period and honour it. Chat logs are the
most candid text your users will ever type into your
product; they belong under the same rules as the rest of
their data ([[SOC 2]], [[Encryption at Rest]]).

## Scope: answer first, act later

Ship the read-only version first — it explains, searches,
summarises and drafts. Only then consider
[[Tool Calling]], where the assistant changes data. The
difference in risk is enormous and the difference in
perceived value is smaller than you think.

For grounding answers in the customer's own data, see
[[Retrieval-Augmented Generation]] — and note that the
simplest useful version is "put the record the user is
looking at into the prompt", not a vector database.

## Watch out for

- **Tenant leakage.** The prompt is assembled from
  database reads; one missing `WHERE tenant_id = ?` and
  one customer's data appears in another's chat. Same
  failure mode as [[Multi-Tenant SaaS]], now with a
  component that paraphrases what it read.
- **The record is untrusted input.** Anything a user
  typed into a field can carry instructions to the model
  — see [[Prompt Injection]].
- **Rendering the answer.** Model output rendered as HTML
  is an XSS sink. Render Markdown with a sanitiser and a
  strict [[Security Headers|Content Security Policy]].
- **Silence looks broken.** First token can take seconds.
  Stream, and show a stop button that actually cancels.
- **Cost per active user is now variable.** A support
  seat that costs you $2/month in infrastructure can cost
  $40/month in tokens if nothing caps it
  ([[Cost Control]]).
- **Users paste secrets into chat boxes.** Say what you
  retain and for how long, in the panel, before they do.

## Related

[[LLM API Integration]] · [[Streaming Responses]] ·
[[Rate Limiting]] · [[Usage Quotas and Metering]] ·
[[Prompt Injection]] · [[Bot Protection]] ·
[[Tool Calling]] · [[Retrieval-Augmented Generation]] ·
[[Multi-Tenant SaaS]] · [[Authentication]] ·
[[Claude API]]

## Sources

- [[anthropic-streaming]] · [[anthropic-models-overview]]
  · [[mdn-server-sent-events]] · [[owasp-llm-top-ten]] ·
  [[usersnap-saas-architecture]] ·
  [[azure-multitenant-overview]]
