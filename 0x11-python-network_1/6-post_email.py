#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address,\
      sends a POST request to the passed URL with the email\
          as a parameter, and finally displays the body of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    def post_email(url, email):
        data = 'email=' + email
        data = data.encode('utf-8')
        req = urllib.request.Request\
            (url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            body = response.read()
        print(body.decode('utf-8'))

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
