#!/bin/bash
#takes in a URL, sends a request to that URL,and displays the size of the body of the response
echo "$(curl -sI "$1" | wc -c | grep -i Content-Length| awk '{print $2}')"
