#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d ':' -f 2 | cut -b 2-
