#!/usr/bin/python3

"""Python script that takes 2 arguments in
   order to solve this challenge
"""

import requests
import sys

if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Build the API endpoint URL
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        sys.exit(1)

    # Retrieve the list of commits from the API response
    commits = response.json()

    # Print the 10 most recent commits (from the most recent to oldest)
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')
