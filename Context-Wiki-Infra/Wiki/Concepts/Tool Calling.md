---
type: Concept
title: "Tool Calling"
description: "Letting the assistant do things, not just say things - the loop, the authorization rule, and where to put the confirm button."
wikipedia: "https://en.wikipedia.org/wiki/AI_agent"
tags: [ai-in-saas, architectures, security]
timestamp: "2026-07-28T00:00:00Z"
---

# Tool Calling

You describe some functions; the model, instead of
answering, replies "call `refund_order` with these
arguments"; your code runs it and hands back the result;
the model continues. That loop is the whole mechanism,
and it is what turns a chat box into something that can
act.

It is also the point where an [[AI Assistant Panel]] goes
from a component that can embarrass you to a component
that can damage you.

## The loop

1. Send `messages` plus a list of tool definitions —
   name, description, JSON schema for the arguments.
2. The reply contains a **tool-use** block instead of, or
   alongside, text.
3. Your code validates the arguments, checks permission,
   executes, and appends a **tool-result** block.
4. Send the whole conversation back. Repeat until the
   model answers in plain text.

Your code is always in the middle. The model never
executes anything — it produces a request that your
server may decline. Every SDK ships a helper that runs
this loop for you; the helper does not run your
authorization, which is still yours to write.

## The authorization rule

**A tool call executes with the permissions of the
signed-in user, checked at execution time, in the same
code path a normal API request would take.**

Not "the model was told to only do X". Not a service
account that can do everything. If the user cannot delete
that record through the UI, the tool must refuse — and
the refusal is a perfectly good tool result to hand back
("not permitted"), which the model will explain.

This one rule is what makes [[Prompt Injection]]
survivable. A poisoned document can make the assistant
*try* anything; it cannot grant it permissions.

## Designing the tool surface

- **Start read-only.** Search, fetch, summarise, compute.
  Most of the value, almost none of the risk.
- **Narrow beats general.** `create_invoice_draft(customer,
  lines)` is auditable and constrainable; `run_sql(query)`
  is a remote shell with extra steps.
- **Descriptions are prompts.** They are how the model
  decides when to call — say when *not* to, as well.
- **Validate against the schema** and then against your
  own rules. Treat arguments as hostile user input,
  because that is what they are
  ([[OWASP Top 10|input validation]]).
- **Make writes idempotent.** The loop retries; the model
  repeats itself. An idempotency key stops the second
  call charging the card again ([[Idempotency]],
  [[Duplicate Processing]]).

## Confirm anything you would not undo silently

For sending, deleting, paying, publishing or changing
permissions: render the proposed call in the panel with
its actual arguments and require a click. The user is
approving a specific action, not delegating a category.

Log every call — user, tenant, tool, arguments, result,
timestamp — and keep it with the rest of your
[[Audit Logging]]. When someone asks "why did it email
that", the transcript alone will not tell you; the tool
log will.

## Connecting to other systems

Rather than hand-writing an integration per SaaS, the
**Model Context Protocol** standardises how an assistant
discovers and calls tools exposed by an external server
— see [[Model Context Protocol]]. Providers can connect
to remote MCP servers directly from the API call.

The convenience is real and so is the exposure: a
third-party MCP server is a supply-chain dependency that
gets to see your prompts and offer the model tools whose
descriptions you did not write. Pin what you connect,
scope its credentials, and read what it declares
([[Least Privilege]]).

## Watch out for

- **Unbounded loops.** Cap iterations per turn. Models
  can ping-pong between tools until the budget is gone
  ([[Usage Quotas and Metering]]).
- **Every result re-enters the prompt.** A tool that
  returns 50,000 rows costs that in input tokens on
  every subsequent turn — paginate and summarise.
- **Latency compounds.** Four sequential tool calls is
  four round trips plus four generations. Return the
  needed data in one call where you can.
- **Tool descriptions from elsewhere are untrusted.**
  So are results — a fetched web page is not an
  instruction ([[Prompt Injection]]).
- **Long-running work does not belong in the loop.** Have
  the tool enqueue a job and report the id
  ([[Message Queues]]).
- **Test the failure paths.** What the model does with
  "permission denied" is part of your UX.

## Related

[[AI Assistant Panel]] · [[Prompt Injection]] ·
[[Authorization]] · [[Least Privilege]] ·
[[Audit Logging]] · [[Idempotency]] ·
[[Model Context Protocol]] · [[Claude API]] ·
[[Retrieval-Augmented Generation]] ·
[[Usage Quotas and Metering]] ·
[[OWASP Top 10 for LLM Applications]]

## Sources

- [[anthropic-tool-use]] · [[anthropic-mcp-connector]] ·
  [[mcp-introduction]] · [[owasp-llm-top-ten]] ·
  [[owasp-authorization-cheatsheet]] ·
  [[owasp-input-validation-cheatsheet]] ·
  [[vercel-ai-sdk-introduction]]
