#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    url = f'https://api.github.com/users/{username}'
    header = {'Authorization': f'Bearer {tocken}'}
    response = urllib.request.Request(url, headers=header)
    with urllib.request.urlopen(response) as req:
        r = req.read()
        head = req.headers
    print(r)
