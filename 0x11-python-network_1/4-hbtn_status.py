#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print("- type:", type(response.content))
print("- content:", response.content.decode())
