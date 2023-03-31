#!/usr/bin/python3

"""Write a Python script that takes in a letter and sends a POST
   request to http://5ca90df4cc6d.136d45d2.alx-cod.online:5000/search_user
   with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://5ca90df4cc6d.136d45d2.alx-cod.online:5000'
    if q.isalpha():
        data = {'q': q}
    else:
        print("No result")
        sys.exit(1)

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
