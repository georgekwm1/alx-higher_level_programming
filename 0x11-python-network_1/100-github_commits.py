#!/usr/bin/python3
"""
A Python script that lists the 10 most recent commits of a given user
in a GitHub repository.
"""

import requests
import sys


def list_commits(username, repository):
    url = f"https://api.github.com/repos/{username}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for i, commit in enumerate(commits[:10], 1):
            commit_message = commit['commit']['message']
            commit_author = commit['commit']['author']['name']
            commit_sha = commit['sha']
            print(f"{commit_sha}: {commit_author}")
    else:
        print("Failed to retrieve commits. Status code:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <username> <repository>")
        sys.exit(1)

    username = sys.argv[1]
    repository = sys.argv[2]

    list_commits(username, repository)
