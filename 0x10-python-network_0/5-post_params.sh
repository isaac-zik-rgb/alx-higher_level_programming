#!/bin/bash
# A script that send a POST request to a uri with parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
