#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('- Server is: {}'.format(response.getheader('Server')))
        print('- Date is: {}'.format(response.getheader('Date')))
        print('- Content-Type is: {}'.format(response.getheader('Content-Type')))
        print('- Content length is: {}'.format(len(html)))
        print('- Message: {}'.format(html.decode('utf-8')))
