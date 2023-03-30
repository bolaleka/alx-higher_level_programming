#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -I -X OPTIONS "$1" | grep 'Allow:' | tr -d '\r' | cut -d ' ' -f 2-
