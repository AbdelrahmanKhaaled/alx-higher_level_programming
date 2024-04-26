#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body_response = response.read()
        print("Body response:")
        print("    - type:", type(body_response))
        print("    - content:", body_response.decode())
        print("    - utf8 content:", body_response.decode())
