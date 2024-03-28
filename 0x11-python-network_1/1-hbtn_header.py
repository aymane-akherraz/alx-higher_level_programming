#!/usr/bin/python3
""" Sends a request to the URL and displays the value
    of the X-Request-Id variable
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        id = response.info().get("X-Request-Id")
    print(id)
