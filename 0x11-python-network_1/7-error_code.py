#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL\
      and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code >= 400:
            print ("Error code: ", e.code)
        else:
            pass
