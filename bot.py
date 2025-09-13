import os
import requests
from requests_oauthlib import OAuth1
from datetime import datetime
from zoneinfo import ZoneInfo

w = ["月", "火", "水", "木", "金", "土", "日"]
japan_tz = ZoneInfo("Asia/Tokyo")
today = datetime.now(japan_tz)
message = "本日は" + today.strftime("%Y/%m/%d") + "(" + w[today.weekday()] + ")です。\n"
url = "https://star.static.jp/data/calendar.csv"
rows = requests.get(url).content.decode("utf-8").splitlines()
for row in rows:
    v = row.split(",")
    y = int(v[0])
    m = int(v[1])
    d = int(v[2])
    dt = datetime(y, m, d, tzinfo=japan_tz)
    name = v[3] + "の" + dt.strftime("%Y/%m/%d") + "(" + w[dt.weekday()] + ")"
    dd = (dt - today).days
    if dd > 0:
        message += name + "まで残り" + str(dd + 1) + "日です。\n"
    if dd > 29:
        break
api_key = os.getenv("X_API_KEY")
api_secret = os.getenv("X_API_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
url = "https://api.x.com/2/tweets"
payload = {"text": message}
auth = OAuth1(api_key, api_secret, access_token, access_token_secret)
res = requests.post(url, json=payload, auth=auth)
print(res.status_code, res.text)
