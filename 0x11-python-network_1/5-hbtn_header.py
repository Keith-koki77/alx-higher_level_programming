#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(f'X-Request-Id: {x_request_id}')
        else:
            print('X-Request-Id header not found in the response.')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
