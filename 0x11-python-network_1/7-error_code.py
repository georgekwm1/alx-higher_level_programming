#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL\
      and displays the body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
