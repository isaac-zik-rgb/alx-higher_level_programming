#!/bin/bash
# Send a request to a uri and display the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
