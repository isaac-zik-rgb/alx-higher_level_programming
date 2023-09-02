#!/usr/bin/python3
"""A script that prints 10 commit from the most recent to the oldest"""
import sys
import requests
if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get("https://api.github.com/repos/{}/{}/commits?per_page=1"
                       .format(repo, owner))
    latest_commit_sha = res.json()[0]['sha']
    res = requests.
    get("https://api.github.com/repos/{}/{}/commits?per_page=10&sha={}"
        .format(owner, repo, latest_commit_sha))
    commits = res.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
