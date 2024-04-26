#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print("X-Request-Id not found in response headers.")
    except requests.RequestException as e:
        print("Error fetching URL:", e)
