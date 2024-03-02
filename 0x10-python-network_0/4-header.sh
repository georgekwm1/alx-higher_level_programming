#!/bin/bash
# Sends a GET request to a URL with a header variable and value
curl -s -H "X-School-User-Id: 98" "$1"
