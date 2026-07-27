# Wiki Tools (find / grep module)

`wiki_tools.py` is a small, stdlib-only Python module
with find / grep / read utilities for a local context
wiki (a directory of Markdown/OKF files). No server,
no dependencies — import it, run it from the command
line, or wrap its functions as agent tools.

## Configuration

| Setting   | Default | Override |
|-----------|---------|----------|
| Wiki root | `Context-Wiki-Infra/` next to the module | `WIKI_ROOT` env var, or `root=` argument |

## Functions

| Function | Description |
|----------|-------------|
| `find(pattern="*", root=None)` | List relative doc paths matching a glob pattern (matched against full relative path or filename) |
| `grep(query, root=None, regex=False, ignore_case=True)` | Return `path:line: text` hits across all documents |
| `read(path, root=None)` | Read one document by relative path (paths outside the wiki root are rejected) |
| `docs(root=None)` | All `.md` files as `Path` objects |
| `get_root(root=None)` | Resolve the active wiki root |

## Usage from Python

```python
import wiki_tools as wt

wt.find("Dashboards/*")
wt.grep("internal controls")
wt.grep(r"Section 40[0-9]", regex=True)
wt.read("Dashboards/Topics.md")
```

## Usage from the command line

```bash
python wiki_tools.py find "Dashboards/*"
python wiki_tools.py grep "internal controls"
python wiki_tools.py read Dashboards/Topics.md
```

## Usage from Claude Code

Nothing to register — Claude Code can call the module
directly via Bash (`python wiki_tools.py grep ...`) or
import it in Python scripts.

## Usage with claude-agent-sdk

To expose the functions as tools for an agent, wrap
them with the SDK's in-process tool helpers:

```python
from claude_agent_sdk import (
    tool, create_sdk_mcp_server,
    ClaudeAgentOptions, query,
)
import wiki_tools as wt


@tool("wiki_find", "List wiki documents by glob pattern",
      {"pattern": str})
async def wiki_find(args):
    docs = wt.find(args.get("pattern", "*"))
    return {"content": [
        {"type": "text", "text": "\n".join(docs)}]}


@tool("wiki_grep", "Search wiki documents for a string",
      {"query": str})
async def wiki_grep(args):
    hits = wt.grep(args["query"])
    return {"content": [
        {"type": "text", "text": "\n".join(hits)}]}


@tool("wiki_read", "Read one wiki document",
      {"path": str})
async def wiki_read(args):
    return {"content": [
        {"type": "text", "text": wt.read(args["path"])}]}


wiki_server = create_sdk_mcp_server(
    name="context-wiki",
    version="1.0.0",
    tools=[wiki_find, wiki_grep, wiki_read],
)

options = ClaudeAgentOptions(
    mcp_servers={"wiki": wiki_server},
    allowed_tools=[
        "mcp__wiki__wiki_find",
        "mcp__wiki__wiki_grep",
        "mcp__wiki__wiki_read",
    ],
)
```

This runs in-process — no separate server needed.

## See also

- [d3_howto_context_wiki.md](d3_howto_context_wiki.md)
  — the wiki structure these tools operate on.
- [d1_okf.md](d1_okf.md) — the OKF file format.
