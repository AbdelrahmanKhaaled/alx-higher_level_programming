#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.parse
import sys


if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode()
req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    body_response = response.read().decode('utf-8')
    print("Your email is:", email)
    print(body_response)

