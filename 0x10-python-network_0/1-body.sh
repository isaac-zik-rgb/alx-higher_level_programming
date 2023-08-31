#!/bin/bash
# A script that uses `curl` command to send a GET request and display a 200 respond message
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -s "$1"
