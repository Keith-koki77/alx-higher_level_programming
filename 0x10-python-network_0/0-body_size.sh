#!/bin/bash
url=$1 #Gets the URL from the cmd line argument
curl -s -I "$url" | wc -c
