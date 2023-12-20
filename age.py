import requests
import json

url = "https://www.binance.com/en/trade/BTC_USDT?type=spot"

data = requests.get(url)
print(data.status_code)

information = data.json()
print(data.json())
