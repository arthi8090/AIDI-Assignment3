import requests, json, os
from datetime import datetime
url='https://api.binance.com/api/v3/klines'
params={'symbol':'BTCUSDT','interval':'1d','limit':365}
data=requests.get(url,params=params).json()
ts=datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
os.makedirs('data/bronze/binance',exist_ok=True)
json.dump(data,open(f'data/bronze/binance/btc_klines_{ts}.json','w'),indent=2)