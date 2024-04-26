#!/bin/bash
#Write a Bash script that sends a DELETE request
echo "$(curl -s -X DELETE "$1")"
