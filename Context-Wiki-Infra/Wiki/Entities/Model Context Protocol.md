---
type: Reference
title: "Model Context Protocol"
description: "An open standard for connecting AI assistants to tools and data - one integration instead of one per pair."
wikipedia: "https://en.wikipedia.org/wiki/Model_Context_Protocol"
tags: [ai-in-saas, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Model Context Protocol

An open protocol, published by Anthropic and now
implemented widely, for how an AI application discovers
and calls capabilities exposed by an external server. The
standard analogy is USB-C: one plug shape instead of a
cable per device pair.

An **MCP server** exposes three kinds of thing — tools
(functions the model may call), resources (data it may
read) and prompts (templates it may use). An **MCP
client**, inside the assistant, connects and uses them.

## Why it exists

Without it, every assistant integrates every system by
hand: N clients times M systems. With it, a vendor
publishes one server and every compliant assistant can
use it. That is the same argument that produced
[[OAuth 2.0 and OpenID Connect]] and every other
integration standard, and it plays out the same way.

For a SaaS product there are two sides to it:

- **Consuming.** Your assistant reaches other systems —
  GitHub, a ticketing tool, a database — without you
  writing each integration ([[Tool Calling]]).
- **Publishing.** You ship an MCP server for *your*
  product, so that other people's assistants can work
  with it. This is becoming a real distribution channel,
  and it is the same job as designing an API: a stable
  surface, scoped credentials, versioning.

## How it reaches the model

Either your application runs the MCP client and passes
the resulting tools into the API call, or the provider
connects to a remote MCP server on your behalf — the
[[Claude API]] takes a list of server URLs plus a toolset
entry per server, and handles the connection itself.
Credentials for those servers are supplied separately
rather than embedded in the shared configuration.

## Watch out for

- **A third-party server is a supply-chain dependency**
  that sees your prompts and supplies tool descriptions
  you did not write — which the model reads as
  instructions ([[Prompt Injection]], risk 03 of the
  [[OWASP Top 10 for LLM Applications]]).
- **Scope the credentials you hand it.** A token that can
  do everything gives the assistant everything
  ([[Least Privilege]]).
- **Authorization is still yours.** Connecting a server
  does not decide who may call what
  ([[Authorization]]).
- **It is young and moving.** Pin versions, and expect
  the transport and auth details to change under you.
- **Every connected tool is context.** Definitions occupy
  the window and the bill on every turn
  ([[Usage Quotas and Metering]]).

## Related

[[Tool Calling]] · [[Claude API]] ·
[[LLM API Integration]] · [[Prompt Injection]] ·
[[OWASP Top 10 for LLM Applications]] ·
[[Least Privilege]] · [[Claude Code]] ·
[[AI Assistant Panel]]

## Sources

- [[mcp-introduction]] · [[anthropic-mcp-connector]] ·
  [[anthropic-tool-use]] · [[owasp-llm-top-ten]]
