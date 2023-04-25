#!/bin/bash
echo "Starting the server..."
dir="$(dirname "$0")"               # get the directory name of the script
cd "$dir"                           # change the current working directory to the script directory

cleanup() {
    echo "Stopping the server..."
    pkill -TERM -P $$                 # Send SIGTERM signal to all child processes
}

trap cleanup SIGINT

python server_web.py               # construct the path to server_web.py and run it
