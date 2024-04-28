#!/usr/bin/python3
"""
 A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print("\t- type:", type(body.decode('utf-8')))
    print("\t- content:", body.decode('utf-8'))

