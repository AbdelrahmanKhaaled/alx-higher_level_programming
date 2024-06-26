#!/bin/bash
#sends a request to a URL passed as an argument, and displays only the status code of the response.
if [ $# -ne 1 ]; then
	  echo "Usage: $0 <URL>"
	    exit 1
fi
url=$1
curl -s -o /dev/null -w "%{http_code}" "$url"
