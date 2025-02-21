#!/usr/bin/python3
""" This will query the API for reddit """
import requests


def top_ten(subreddit):
    """getting top ten post titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"

    response = requests.get(
        subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        if 'data' in json_data and 'children' in json_data['data']:
            for i in range(10):
                print(json_data['data']['children'][i]['data']['title'])
        else:
            print(None)
    else:
        print(None)
