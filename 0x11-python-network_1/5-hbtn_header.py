#!/usr/bin/python3
"""
a Python script that takes in a URL,\
sends a request to the URL and displays the value of the\
variable X-Request-Id in the response header
"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        body = response.read()
        x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
