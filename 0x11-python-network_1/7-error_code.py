#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).You have to manage
urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code <= 400:
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
