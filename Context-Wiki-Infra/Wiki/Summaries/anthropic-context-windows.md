---
type: Summary
title: "Context windows (Anthropic)"
description: "Understand how the context window works, how extended thinking and tool use count toward it, and how to manage context as conversations grow."
resource: "https://platform.claude.com/docs/en/build-with-claude/context-windows.md"
source_file: "Raw/12_ai_in_saas/anthropic-context-windows.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Context windows (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-context-windows.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/build-with-claude/context-windows.md>

## Opening

> Understand how the context window works, how extended thinking and tool use count toward it, and how to manage context as conversations grow.
> As conversations grow, you'll eventually approach context window limits. For long-running conversations and agentic workflows, [server-side compaction](/docs/en/build-with-claude/compaction) is the primary strategy for context management.
> The "context window" refers to all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window ...
> <Tip>

## Contents of the source document

- Context windows
  - How the context window works
  - Context window sizes by model
  - The context window with thinking
  - The context window with thinking and tool use
  - Context awareness
    - How it works
  - Manage context with compaction
  - Context window overflow behavior
  - Next steps

## Related pages

[[Claude API]]
