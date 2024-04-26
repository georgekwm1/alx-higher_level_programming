#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request and store the response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the response status code is 200
if [ "$response" -eq 200 ]; then
    # If status code is 200, display the body of the response
    curl -s "$1"

elif [ "$response" -eq 302 ]; then
    echo "Route 2"

else
    # If status code is not 200, display an error message
    echo "Error: HTTP status code $response"
fi

