---
type: Summary
title: "MCP connector (Anthropic)"
description: "Connect to remote MCP servers directly from the Messages API without an MCP client, and allowlist, denylist, or configure individual tools."
resource: "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector.md"
source_file: "Raw/12_ai_in_saas/anthropic-mcp-connector.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# MCP connector (Anthropic)

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/anthropic-mcp-connector.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://platform.claude.com/docs/en/agents-and-tools/mcp-connector.md>

## Opening

> Connect to remote MCP servers directly from the Messages API without an MCP client, and allowlist, denylist, or configure individual tools.
> Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.
> <Note>
> The previous version (`mcp-client-2025-04-04`) is deprecated. See [Deprecated version: mcp-client-2025-04-04](#deprecated-version-mcp-client-2025-04-04).

## Contents of the source document

- MCP connector
  - Key features
  - When Claude uses MCP tools
  - Limitations
  - Using the MCP connector in the Messages API
    - Basic example
  - MCP server configuration
    - Field descriptions
  - MCP toolset configuration
    - Basic structure
    - Field descriptions
    - Tool configuration options
    - Configuration merging
  - Common configuration patterns
    - Enable all tools with default configuration
    - Allowlist: enable only specific tools
    - Denylist: disable specific tools
    - Mixed: allowlist with per-tool configuration

## Related pages

[[Authentication]] · [[Authorization]] · [[Claude API]] · [[HTTP]] · [[Model Context Protocol]] · [[Node.js]] · [[Tool Calling]]
