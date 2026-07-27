#!/bin/bash
# Stop the wiki server (port 8020).
# Usage: ./server_stop.sh

cd "$(dirname "$0")"

PORT=8020
PIDFILE=.wiki_server.pid

STOPPED=0

# 1) try the recorded pid
if [ -f "$PIDFILE" ]; then
    PID=$(cat "$PIDFILE")
    if kill "$PID" 2>/dev/null; then
        echo "Stopped wiki server (pid $PID)"
        STOPPED=1
    fi
    rm -f "$PIDFILE"
fi

# 2) fallback: whatever is listening on the port
PIDS=$(lsof -ti :$PORT 2>/dev/null)
if [ -n "$PIDS" ]; then
    echo "$PIDS" | xargs kill 2>/dev/null
    echo "Stopped process(es) on port $PORT: $PIDS"
    STOPPED=1
fi

if [ "$STOPPED" -eq 0 ]; then
    echo "No wiki server running on port $PORT"
fi
