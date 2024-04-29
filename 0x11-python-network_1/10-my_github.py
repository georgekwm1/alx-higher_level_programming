#!/usr/bin/python3
"""
A Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display the user's ID.
"""

import requests
import sys


def get_github_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        user_id = data.get('id')
        if user_id:
            print(user_id)
        else:
            print("Failed to retrieve user ID from GitHub API response.")
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    get_github_id(username, password)
