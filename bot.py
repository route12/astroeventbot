import os
import requests
from requests_oauthlib import OAuth1

api_key = os.getenv("X_API_KEY")
api_secret = os.getenv("X_API_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

url = "https://api.x.com/2/tweets"
payload = {"text": "GitHub Actionsから投稿テストです！"}

auth = OAuth1(api_key, api_secret, access_token, access_token_secret)

res = requests.post(url, json=payload, auth=auth)
print(res.status_code, res.text)
