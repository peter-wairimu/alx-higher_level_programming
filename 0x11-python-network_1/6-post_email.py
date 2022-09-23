#!/usr/bin/python3
"""
    Python script that takes in a URL
"""
if __name__ == "__main__":
    import requests
    import sys

    dic = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=dic)
    print(r.text)
