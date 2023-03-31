#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    content = response.json()
    print("Body response:")
    print("\t- type: {}".format(content["name"]))
    print("\t- content: {}".format(content["status"]))
