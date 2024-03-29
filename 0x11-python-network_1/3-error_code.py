#!/usr/bin/python3

"""
    Python script that takes in a URL, sends a request to the URL
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            li = str(response.read().decode('utf-8'))
            print(li)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
