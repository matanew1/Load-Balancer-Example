#!/bin/bash

# Define the desired scale
desired_scale=5

# Get the current scale of the app service
current_scale=$(docker-compose ps -q nginx | wc -l)

# Check if the current scale is less than the desired scale
if [ $current_scale -lt $desired_scale ]; then
    echo "Scaling up to $desired_scale containers..."
    docker-compose up -d --scale nginx=$desired_scale
elif [ $current_scale -gt $desired_scale ]; then
    echo "Scaling down to $desired_scale containers..."
    docker-compose up -d --scale nginx=$desired_scale
else
    echo "App service is already scaled to $desired_scale containers."
fi
