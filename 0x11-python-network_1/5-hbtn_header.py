#!/usr/bin/python3
"""
a Python script that takes in a URL,\
sends a request to the URL and displays the value of the\
variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    x_request_id = response.headers['X-Request-Id']
    print(x_request_id)
    print(response.headers)
