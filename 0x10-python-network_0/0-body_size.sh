#!/bin/bash
# This script takes a URL, sends a request, and displays the response body size in bytes
curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r'
