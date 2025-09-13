import os
import requests
from requests_oauthlib import OAuth1
from datetime import datetime

today = datetime.today()
next_year = today.year + 1
new_years_day = datetime(next_year, 1, 1)
days_remaining = (new_years_day - today).days
message = "本日は" + today.strftime("%Y年%m月%d日") + "です。\n"
message += "来年まで残り" + days_remaining + "日です。"

api_key = os.getenv("X_API_KEY")
api_secret = os.getenv("X_API_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
url = "https://api.x.com/2/tweets"
payload = {"text": message}
auth = OAuth1(api_key, api_secret, access_token, access_token_secret)
res = requests.post(url, json=payload, auth=auth)
print(res.status_code, res.text)
