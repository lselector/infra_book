#!/bin/bash
# Start the wiki server (port 8020) in the background.
# Usage: ./server_start.sh

cd "$(dirname "$0")"

# python from the active environment; override with
# PYTHON=/path/to/python ./server_start.sh
PYTHON="${PYTHON:-$(command -v python \
    || command -v python3)}"
if [ -z "$PYTHON" ]; then
    echo "No python found in PATH"
    exit 1
fi
PORT=8020
PIDFILE=.wiki_server.pid
LOGFILE=wiki_server.log

if lsof -ti :$PORT > /dev/null 2>&1; then
    echo "Port $PORT already in use - server running?"
    echo "Use ./server_stop.sh or ./server_restart.sh"
    exit 1
fi

nohup "$PYTHON" wiki_server.py > "$LOGFILE" 2>&1 &
echo $! > "$PIDFILE"
sleep 1

if kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    echo "Wiki server started (pid $(cat "$PIDFILE"))"
    echo "Open: http://localhost:$PORT"
    echo "Log:  $LOGFILE"
else
    echo "Server failed to start - see $LOGFILE"
    rm -f "$PIDFILE"
    exit 1
fi
