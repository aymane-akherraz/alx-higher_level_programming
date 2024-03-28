#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
file_content=$(cat "$2")
curl -s -H "Content-Type: application/json" -d "$file_content" "$1"
