#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_2
