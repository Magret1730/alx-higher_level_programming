#!/usr/bin/python3
"""
A script that prints 10 commits from github api
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    r = requests.get(url)
    data = r.json()
    for commit in data[:10]:
        sha = commit.get('sha', 'None')
        author_name = commit['commit']['author'].get('name', 'None')
        print(f"{sha}: {author_name}")
