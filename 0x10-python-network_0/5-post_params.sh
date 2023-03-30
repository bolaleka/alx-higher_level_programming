#!/bin/bash
# Send POST request with email and subject variables
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
