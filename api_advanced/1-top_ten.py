#!/usr/bin/python3
""" this will query the API for reddit """
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:top_ten_script:v1.0 (by /u/Separate-Lion-614)'
    }
    params = {'limit': 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data']['title'])
