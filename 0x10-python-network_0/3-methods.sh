#!/bin/bash
# A script that takes in a uri and displat the available options in http reques
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
