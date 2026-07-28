#!/usr/bin/env python3
"""Claude Code PreToolUse auto-allow for local dev work.

Approves Bash commands that only build this wiki or poke
the local wiki server, so they never raise a permission
prompt. Stays silent for everything else, letting the
normal permission rules decide.

Approved when every pipeline segment is one of:

  1. python / python3 running a script of this repo
     (wiki_build.py, wikipedia_links.py, raw_download.py,
     wiki_server.py).
  2. curl aimed only at localhost / 127.0.0.1.
  3. A read-only text filter (head, tail, grep, wc, ...).

Anything with command substitution, or a redirect that
writes a real file, is left alone.

Reads the hook payload as JSON on stdin, writes a
PreToolUse decision as JSON on stdout.

Example:
    echo '{"tool_input":{"command":"python wiki_build.py \\
        index"}}' | python3 allow_local_dev.py

Created: 2026-07-28
Last updated: 2026-07-28
"""

import json
import re
import sys

REPO_SCRIPT_RX = re.compile(
    r"^python3?\s+"
    r"(wiki_build|wikipedia_links|raw_download"
    r"|wiki_server)\.py\b")

READER_RX = re.compile(
    r"^(head|tail|cat|wc|sort|uniq|grep|rg|jq|awk"
    r"|cut|tr|column|nl|python3?\s+-m\s+json\.tool"
    r"|sed\s+-n)\b")

URL_RX = re.compile(r"https?://[^\s'\"]+")

LOCAL_URL_RX = re.compile(
    r"^https?://(localhost|127\.0\.0\.1)([:/]|$)")

LOCAL_HOST_RX = re.compile(
    r"(^|[\s'\"=])(https?://)?"
    r"(localhost|127\.0\.0\.1)(:\d+)?([/\s'\"]|$)")

SUBST_RX = re.compile(r"\$\(|`")

# Redirects that only move stream handles around.
SAFE_REDIR_RX = re.compile(
    r"2>&1|&>\s*/dev/null|2?>>?\s*/dev/null")

SPLIT_RX = re.compile(r"\|\||&&|[|;]")


# --------------------------------------------------------------
def decision(verdict, reason):
    """Emit a PreToolUse permission decision."""
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": verdict,
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


# --------------------------------------------------------------
def writes_a_file(segment):
    """True when a redirect would create or append a file."""
    rest = SAFE_REDIR_RX.sub("", segment)
    return ">" in rest or "<" in rest


# --------------------------------------------------------------
def is_local_curl(segment):
    """True for a curl that only targets the local host."""
    if not re.match(r"^curl\b", segment):
        return False
    for url in URL_RX.findall(segment):
        if not LOCAL_URL_RX.match(url):
            return False
    return bool(LOCAL_HOST_RX.search(segment))


# --------------------------------------------------------------
def segment_ok(segment):
    """True when one pipeline segment is safe to allow."""
    segment = segment.strip()
    if not segment or writes_a_file(segment):
        return False
    return bool(
        REPO_SCRIPT_RX.match(segment)
        or READER_RX.match(segment)
        or is_local_curl(segment))


# --------------------------------------------------------------
def read_payload():
    """Parse the hook payload, tolerating bad input."""
    try:
        return json.loads(sys.stdin.read() or "{}")
    except (ValueError, OSError):
        return {}


# --------------------------------------------------------------
def main():
    """Auto-allow local wiki build and probe commands."""
    data = read_payload()
    command = data.get("tool_input", {}).get("command", "")
    if not command or SUBST_RX.search(command):
        sys.exit(0)

    segments = SPLIT_RX.split(command)
    if all(segment_ok(s) for s in segments):
        decision("allow", "Local wiki build / localhost "
                          "probe - allowed by "
                          ".claude/hooks/allow_local_dev.py")
    sys.exit(0)


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
