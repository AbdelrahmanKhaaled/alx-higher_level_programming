#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
url=$1
size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')
echo "Size of the response body: $content_length bytes"
