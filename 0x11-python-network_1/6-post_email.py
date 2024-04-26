#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print("Response Body:")
        print(response.text)
    except requests.RequestException as e:
        print("Error sending POST request:", e)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
