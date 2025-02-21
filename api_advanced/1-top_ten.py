#!/usr/bin/python3
""" This will query the API for reddit """
import requests


def top_ten(subreddit):
    """getting number of subscriber if subreddit is valid
    if not get 0"""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if posts:
            for i in range(min(10, len(posts))):
                print(posts[i].get('data', {}).get('title'))
        else:
            print("OK")
    else:
        print("OK")
