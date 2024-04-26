#!/bin/bash

if [ $# -ne 1 ]; then
	  echo "Usage: $0 <URL>"
	    exit 1
fi

url=$1

response=$(mktemp)
curl -s -o "$response" "$url"

size=$(wc -c < "$response")

echo "Size of the response body: $size bytes"

rm "$response"
