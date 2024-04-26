#!/bin/bash
#Displays the body of a GET request
echo "$(curl -s "$1")"
