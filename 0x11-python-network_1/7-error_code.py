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
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print("Response Body:")
            print(response.text)
    except requests.RequestException as e:
        print("Error fetching URL:", e)
