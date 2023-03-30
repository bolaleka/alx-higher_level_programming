#!/bin/bash
# Send a GET request to the URL and display the response body
curl -s -o /dev/null -w "%{http_code}" "$1"
