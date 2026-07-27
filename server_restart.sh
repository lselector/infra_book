#!/bin/bash
# Restart the wiki server (port 8020).
# Usage: ./server_restart.sh

cd "$(dirname "$0")"

./server_stop.sh
sleep 1
./server_start.sh
