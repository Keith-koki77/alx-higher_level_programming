#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")

    except urllib.error.URLError as e:
        print(f"Failed to retrieve data from {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
