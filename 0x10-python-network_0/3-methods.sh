#!/bin/bash
#Lists the HTTP methods a server accepts
curl -s -X OPTIONS -i "$1" | awk '/Allow:/ {print substr($0, index($0, ":") + 2)}'
