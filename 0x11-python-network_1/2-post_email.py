#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))
