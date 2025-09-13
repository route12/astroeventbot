# bot.py
import requests
import os

# 環境変数からトークン取得
BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

url = "https://api.x.com/2/tweets"
payload = {"text": "こんにちは！GitHub Actionsからの定期投稿です。"}
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code, response.text)
