#!/usr/bin/python3
""" Search API """

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""

    try:
        r = requests.get(url)
        js = r.json()
        print("Good")
        print(js)
    except ValueError:
        print("Error")
