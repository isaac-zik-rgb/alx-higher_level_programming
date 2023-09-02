#!/usr/bin/python3
"""A script that prints 10 commit from the most recent to the oldest"""
import sys
import requests
if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get("https://api.github.com/repos/{}/{}/commits?per_page=1"
                       .format(repo, owner))
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                                  commits[i].get("commit").
                                  get("author").get("name")))
    except IndexError:
        pass
