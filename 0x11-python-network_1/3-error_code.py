#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).You have to manage
urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            decoded = html.decode('utf-8')
            print(decoded)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
