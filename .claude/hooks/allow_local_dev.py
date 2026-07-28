#!/usr/bin/env python3
"""Claude Code PreToolUse auto-allow for local dev work.

Approves Bash commands that only read this repo, build the
wiki, or fetch a URL, so they never raise a permission
prompt. Stays silent for everything else, letting the
normal permission rules decide.

A command is approved when *every* segment of it (split on
|, ||, &&, ;) is one of:

  1. python / python3 running a script of this repo
     (wiki_build.py, wikipedia_links.py, raw_download.py,
     wiki_server.py).
  2. ./server_start.sh, ./server_stop.sh or
     ./server_restart.sh - the local wiki server on port
     8020, and nothing else.
  3. curl doing a plain GET - no -d/-F/-T, no -X other
     than GET, and -o only to /dev/null or -.
  4. A read-only text filter (head, tail, grep, ls, sed
     -n, wc, find without -delete/-exec, ...), or sleep.
  5. `cd` to a path inside the project directory.
  6. A shell control word of a one-line loop
     (`for x in ...`, `do`, `done`).

Anything with command substitution, or a redirect that
writes a real file, is left alone. Cases 4 and 5 are what
let a compound one-liner through: without them a
read-only `cd X && for f in *; do grep ...; done` prompts
even though every piece of it is harmless.

Reads the hook payload as JSON on stdin, writes a
PreToolUse decision as JSON on stdout.

Example:
    echo '{"tool_input":{"command":"python wiki_build.py \\
        index"}}' | python3 allow_local_dev.py

Created: 2026-07-28
Last updated: 2026-07-28
"""

import json
import os
import re
import sys

REPO_SCRIPT_RX = re.compile(
    r"^python3?\s+"
    r"(wiki_build|wikipedia_links|raw_download"
    r"|wiki_server)\.py\b")

READER_RX = re.compile(
    r"^(head|tail|cat|wc|sort|uniq|grep|rg|jq|awk"
    r"|cut|tr|column|nl|ls|printf|echo|basename|dirname"
    r"|file|stat|diff|date|sleep|find"
    r"|python3?\s+-m\s+json\.tool"
    r"|sed\s+-n)\b")

# The wiki server control scripts: they only start, stop
# or restart the local server on port 8020.
SERVER_SCRIPT_RX = re.compile(
    r"^(\./)?server_(start|stop|restart)\.sh\b")

# find can run or delete things; those forms are not reads.
FIND_WRITE_RX = re.compile(
    r"(^|\s)-(delete|exec|execdir|ok|okdir|fprint\w*|fls)\b")

CURL_RX = re.compile(r"^curl\b")

CURL_WRITE_RX = re.compile(
    r"(^|\s)(-d|--data|--data-\S+|-F|--form|-T"
    r"|--upload-file)\b")

CURL_METHOD_RX = re.compile(
    r"(^|\s)(-X|--request)\s+(?!GET\b)")

CURL_OUT_RX = re.compile(r"(^|\s)(?:-o|--output)\s+(\S+)")

CD_RX = re.compile(r"^cd\s+(\S+)$")

LOOP_HEAD_RX = re.compile(r"^(for|while)\s+\S")

CONTROL_RX = re.compile(r"^(do|done|then|fi|else|esac)\b")

SUBST_RX = re.compile(r"\$\(|`")

QUOTED_RX = re.compile(r"'[^']*'|\"[^\"]*\"")

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
    # Quoted text first: `printf "a -> b"` and
    # `grep "^> quoted"` carry a > that is not a redirect.
    rest = QUOTED_RX.sub("", segment)
    rest = SAFE_REDIR_RX.sub("", rest)
    return ">" in rest or "<" in rest


# --------------------------------------------------------------
def is_read_only_curl(segment):
    """True for a curl that only fetches (a plain GET)."""
    if not CURL_RX.match(segment):
        return False
    if CURL_WRITE_RX.search(segment):
        return False
    if CURL_METHOD_RX.search(segment):
        return False
    # -o is fine as long as the body is discarded.
    return all(
        target.strip("'\"") in ("/dev/null", "-")
        for _flag, target in CURL_OUT_RX.findall(segment)
    )


# --------------------------------------------------------------
def is_inside_project(target):
    """True when a cd target stays inside the repo."""
    target = target.strip("'\"")
    if target.startswith("~") or ".." in target.split("/"):
        return False
    if not target.startswith("/"):
        return True
    root = os.environ.get("CLAUDE_PROJECT_DIR", "").rstrip("/")
    return bool(root) and (target == root
                           or target.startswith(root + "/"))


# --------------------------------------------------------------
def is_reader(segment):
    """True for a read-only text filter or lister."""
    if not READER_RX.match(segment):
        return False
    if segment.startswith("find"):
        return not FIND_WRITE_RX.search(segment)
    return True


# --------------------------------------------------------------
def segment_ok(segment):
    """True when one pipeline segment is safe to allow."""
    segment = segment.strip()
    # `for f in *; do grep ...; done` splits into a loop
    # head, a `do`-prefixed body, and a bare `done`.
    segment = re.sub(r"^do\s+", "", segment).strip()
    if not segment or CONTROL_RX.match(segment):
        return True
    if writes_a_file(segment):
        return False
    cd_match = CD_RX.match(segment)
    if cd_match:
        return is_inside_project(cd_match.group(1))
    if LOOP_HEAD_RX.match(segment):
        return True
    return bool(
        REPO_SCRIPT_RX.match(segment)
        or SERVER_SCRIPT_RX.match(segment)
        or is_reader(segment)
        or is_read_only_curl(segment))


# --------------------------------------------------------------
def read_payload():
    """Parse the hook payload, tolerating bad input."""
    try:
        return json.loads(sys.stdin.read() or "{}")
    except (ValueError, OSError):
        return {}


# --------------------------------------------------------------
def main():
    """Auto-allow local wiki build and read-only commands."""
    data = read_payload()
    command = data.get("tool_input", {}).get("command", "")
    if not command or SUBST_RX.search(command):
        sys.exit(0)

    segments = SPLIT_RX.split(command)
    if all(segment_ok(s) for s in segments):
        decision("allow", "Read-only / local wiki build - "
                          "allowed by "
                          ".claude/hooks/allow_local_dev.py")
    sys.exit(0)


# --------------------------------------------------------------
if __name__ == "__main__":
    main()
