#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
if curl -sLI "$1" | grep -q "200"; then curl -sL "$1"; fi
