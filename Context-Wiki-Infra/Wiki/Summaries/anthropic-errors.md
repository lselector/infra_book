---
type: Summary
title: "API errors and HTTP status codes (Anthropic)"
description: "Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions."
resource: "https://platform.claude.com/docs/en/api/errors.md"
source_file: "Raw/12_ai_in_saas/anthropic-errors.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# API errors and HTTP status codes (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-errors.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/api/errors.md>

## Opening

> Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.
> The API follows a predictable HTTP error code format:
> <Warning>
> 529 errors can occur when the API experiences high traffic across all users.

## Contents of the source document

- Claude API errors
  - HTTP errors
  - Request size limits
  - Error shapes
  - SDK error types
  - Request ID
  - Long requests
  - Common validation errors
    - Prefill not supported
    - Thinking blocks cannot be modified
    - Extended thinking not supported
    - Adaptive thinking not supported
    - Thinking cannot be disabled
    - Outbound web identity federation disabled (Claude Platform on AWS)
  - Next steps

## Related pages

[[AWS IAM]] · [[Authentication]] · [[Claude API]] · [[Claude Code]] · [[Cloudflare]] · [[HTTP]]
