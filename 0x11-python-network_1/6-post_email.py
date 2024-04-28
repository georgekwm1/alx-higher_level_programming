#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address,\
      sends a POST request to the passed URL with the email\
          as a parameter, and finally displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    def post_email(url, email):
        data = {'email': email}
        response = requests.post(url, data=data)
        print(response.text)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
