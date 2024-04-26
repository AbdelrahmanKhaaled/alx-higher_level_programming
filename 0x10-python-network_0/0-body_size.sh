#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

headers=$(curl -sI "$url")

content_length=$(echo "$headers" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

echo "Size of the response body: $content_length bytes"
