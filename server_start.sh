#!/bin/bash
# Start the wiki server (port 8020) in the background.
# If the port is already in use, stop that server first
# and start a fresh one - i.e. start doubles as restart.
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
    echo "Port $PORT already in use - restarting"
    ./server_stop.sh
    sleep 1
fi

# Whatever holds the port was not ours to kill, or did
# not die: better to say so than to start a server that
# cannot bind.
if lsof -ti :$PORT > /dev/null 2>&1; then
    echo "Port $PORT is still in use - not starting"
    echo "Check with: lsof -i :$PORT"
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
