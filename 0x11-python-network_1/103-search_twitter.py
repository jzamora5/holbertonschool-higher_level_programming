#!/usr/bin/python3
""" Twitter Oauth2 and Search API """

if __name__ == "__main__":
    import requests
    import sys
    import base64
    cons_key = sys.argv[1]
    cons_secret = sys.argv[2]
    st_search = sys.argv[3]
    url_oauth2 = "https://api.twitter.com/oauth2/token"
    url_search = "https://api.twitter.com/1.1/search/tweets.json"

    # Authentication to obtain bearer token

    br_token = "{:s}:{:s}".format(cons_key, cons_secret)
    br_token_64 = base64.b64encode(br_token.encode('utf-8'))
    headers = {
        "Authorization": "Basic " + br_token_64.decode('utf-8'),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    req_body = {'grant_type': 'client_credentials'}
    response = requests.post(url_oauth2, headers=headers, data=req_body)
    try:
        payload = response.json()
    except ValueError:
        sys.exit()
    acs_token = payload.get('access_token')

    # Search Tweets

    auth = {'Authorization': "Bearer " + acs_token}
    payload = {
        'q': st_search,
        'result_type': 'recent',
        'count': 5}

    search_res = requests.get(url_search, headers=auth, params=payload)
    try:
        json_search_res = search_res.json()
    except ValueError:
        sys.exit()
    for s in json_search_res.get("statuses"):
        st = "[{}] {} by {}".format(
            s.get('id'), s.get('text'), s.get('user').get('name'))
        print(st)
