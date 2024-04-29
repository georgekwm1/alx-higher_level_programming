#!/usr/bin/python3
"""
A Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No result")
        sys.exit(1)

    letter = sys.argv[1]

    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': letter})
        if response.status_code == 200:
            data = response.json()
            if data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
