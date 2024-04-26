#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body_response = response.read().decode('utf-8')
        print(body_response)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
