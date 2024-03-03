#!/bin/bash

# Function to scale the app service to a specified number of replicas
scale_app() {
    local replicas="$1"
    docker-compose up --build -d --scale app1="$replicas"
}

# Main script
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <replicas>"
    exit 1
fi

replicas="$1"

if ! [[ "$replicas" =~ ^[0-9]+$ ]]; then
    echo "Replicas must be a valid positive integer."
    exit 1
fi

if [ "$replicas" -lt 1 ] || [ "$replicas" -gt 5 ]; then
    echo "Replicas must be between 1 and 5."
    exit 1
fi

scale_app "$replicas"
echo "Scaled app1 to $replicas replicas."
