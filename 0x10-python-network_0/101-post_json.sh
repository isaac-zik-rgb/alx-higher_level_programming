#!/bin/bash
# Sends a JSON POST request to a given URI with a given JSON file
curl -s -H "Content-Type:application/json" -d "$(cat "$2") "$1"
