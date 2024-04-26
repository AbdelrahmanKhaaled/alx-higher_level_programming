#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "\n%{http_code}\n" "$1" | awk '/^$/ {body=1; next} body && !/^2/'
