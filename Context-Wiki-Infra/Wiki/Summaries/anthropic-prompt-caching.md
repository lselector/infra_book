---
type: Summary
title: "Prompt caching (Anthropic)"
description: "Cache prompt prefixes with cachecontrol to cut costs and latency, using automatic caching or explicit breakpoints with 5-minute or 1-hour TTLs."
resource: "https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md"
source_file: "Raw/12_ai_in_saas/anthropic-prompt-caching.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Prompt caching (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-prompt-caching.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md>

## Opening

> Cache prompt prefixes with `cache_control` to cut costs and latency, using automatic caching or explicit breakpoints with 5-minute or 1-hour TTLs.
> Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts. This significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.
> <Note>
> For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Contents of the source document

- Prompt caching
  - How prompt caching works
  - Pricing
  - Supported models
  - Automatic caching
    - How automatic caching works in multi-turn conversations
    - TTL support
    - Combining with block-level caching
    - What stays the same
    - Edge cases
  - Explicit cache breakpoints
    - Structuring your prompt
    - Understanding cache breakpoint costs
  - Caching strategies and considerations
    - Cache limitations
    - What can be cached
    - What cannot be cached
    - What invalidates the cache

## Related pages

[[Claude API]] · [[Render]]
