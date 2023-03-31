#!/usr/bin/python3

"""Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)

    # Make API request to get user information
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=auth)

    # Check if response was successful
    if response.status_code != 200:
        print('None')
        sys.exit()

    # Extract and print user ID from response
    user_info = response.json()
    print(user_info['id'])
