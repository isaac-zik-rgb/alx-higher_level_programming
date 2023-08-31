#!/bin/bash
# This script takes a URL, sends a request, and displays the response body size in bytes
curl -sI "$1" | wc -c
