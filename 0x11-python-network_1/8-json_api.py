#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    params = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', params=params)

    json_response = response.json()

    if response.status_code == 200 and json_response:
        if isinstance(json_response, list):
            for user in json_response:
                print(f"[{user.get('id')}] {user.get('name')}")
        else:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
    elif not json_response:
        print("No result")
    else:
        print("No a valid JSON")
