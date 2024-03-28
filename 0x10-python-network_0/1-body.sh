#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
if ! curl -sLI "$1" | grep "200" | wc -l; then
	curl -sL "$1"
fi
