#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
