---
type: Summary
title: "Message Batches API (Anthropic)"
description: "Process large volumes of Messages requests asynchronously with the Message Batches API, cutting costs by 50% and increasing throughput."
resource: "https://platform.claude.com/docs/en/build-with-claude/batch-processing.md"
source_file: "Raw/12_ai_in_saas/anthropic-batch-processing.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# Message Batches API (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-batch-processing.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/build-with-claude/batch-processing.md>

## Opening

> Process large volumes of Messages requests asynchronously with the Message Batches API, cutting costs by 50% and increasing throughput.
> Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing. This pattern is particularly useful when:
> The Message Batches API is Anthropic's first implementation of this pattern.
> <Note>

## Contents of the source document

- Batch processing
- Message Batches API
  - How the Message Batches API works
    - Batch limitations
    - Supported models
    - What can be batched
  - Pricing
  - How to use the Message Batches API
    - Prepare and create your batch
    - Tracking your batch
    - Listing all Message Batches
    - Retrieving batch results
    - Canceling a Message Batch
    - Using prompt caching with Message Batches
    - Server tools and the agentic loop
    - Extended output (beta)
    - Best practices for effective batching
    - Troubleshooting common issues

## Related pages

[[Claude API]] · [[HTTP]]
