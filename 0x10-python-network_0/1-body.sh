#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
url=$1
response=$(curl -s -w "%{http_code}" "$url")
[ "${response: -3}" -eq 200 ] && curl -s "$url"
