#!/usr/bin/env python3
"""Find / grep utilities for a local context wiki.

Plain Python module (stdlib only) for working with a
directory of Markdown/OKF files (the context wiki).
Use it directly from Python, from the command line,
from Claude Code, or wrap the functions as tools via
the claude-agent-sdk.

Usage (Python):
    import wiki_tools as wt
    wt.find("*.md")           # list documents
    wt.grep("serverless")     # search lines
    wt.read("claude.md")      # read one document

Usage (command line):
    python wiki_tools.py find "Dashboards/*"
    python wiki_tools.py grep "load balancer"
    python wiki_tools.py read Dashboards/Topics.md

The wiki root defaults to Context-Wiki-Infra next to
this file; override with the WIKI_ROOT environment
variable or the root= argument.

Created: 2026-07-15
Last updated: 2026-07-27
"""

import fnmatch
import os
import re
import sys
from pathlib import Path

DEFAULT_ROOT = (
    Path(__file__).parent / "Context-Wiki-Infra"
)


# --------------------------------------------------------------
def get_root(root=None):
    """Resolve the wiki root directory."""
    if root is None:
        root = os.environ.get("WIKI_ROOT", DEFAULT_ROOT)
    return Path(root).resolve()


# --------------------------------------------------------------
def docs(root=None):
    """Return sorted list of all .md Paths in the wiki."""
    return sorted(get_root(root).rglob("*.md"))


# --------------------------------------------------------------
def find(pattern="*", root=None):
    """List relative doc paths matching a glob pattern."""
    base = get_root(root)
    rels = [
        p.relative_to(base).as_posix() for p in docs(root)
    ]
    return [
        r for r in rels
        if fnmatch.fnmatch(r, pattern)
        or fnmatch.fnmatch(Path(r).name, pattern)
    ]


# --------------------------------------------------------------
def grep(query, root=None, regex=False,
         ignore_case=True):
    """Return 'path:line: text' hits matching query."""
    base = get_root(root)
    flags = re.IGNORECASE if ignore_case else 0
    if not regex:
        query = re.escape(query)
    rx = re.compile(query, flags)
    hits = []
    for p in docs(root):
        rel = p.relative_to(base).as_posix()
        text = p.read_text(
            encoding="utf-8", errors="ignore"
        )
        for n, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append(f"{rel}:{n}: {line.strip()}")
    return hits


# --------------------------------------------------------------
def read(path, root=None):
    """Read one wiki document by relative path."""
    base = get_root(root)
    doc = (base / path).resolve()
    if not doc.is_relative_to(base):
        raise ValueError(
            f"Path escapes wiki root: {path}"
        )
    return doc.read_text(encoding="utf-8")


# --------------------------------------------------------------
def main():
    """Tiny CLI: wiki_tools.py find|grep|read [arg]."""
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    cmd, rest = args[0], args[1:]
    if cmd == "find":
        print("\n".join(find(rest[0] if rest else "*")))
    elif cmd == "grep" and rest:
        print("\n".join(grep(rest[0])))
    elif cmd == "read" and rest:
        print(read(rest[0]))
    else:
        print(f"Usage: {sys.argv[0]} "
              "find|grep|read [arg]")


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
