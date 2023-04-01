#!/bin/bash

# Find the process that is listening on port 8080
PORT=8080
PID=$(sudo lsof -t -i:${PORT})

# Terminate the process using the PID
echo "Terminating process ${PID}..."
sudo kill ${PID}
