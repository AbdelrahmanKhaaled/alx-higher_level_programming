#!/usr/bin/python3
"""Module for fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    try:
        url = "http://0.0.0.0:5000/search_user"
        payload = {'q': letter}
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Error:", response.text)
        json_data = response.json()
                                                                                        
        if isinstance(json_data, dict) and not json_data:
            print("No result")
        elif isinstance(json_data, list) and len(json_data) > 0:
            user = json_data[0]
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print("Error sending POST request:", e)
