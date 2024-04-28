#!/usr/bin/python3
"""
A Python script that takes in a URL and an email,\
sends a POST request to the passed URL with the email as a parameter,\
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = 'Your email is' + sys.argv[2]
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))

