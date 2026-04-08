import requests, json, os
from datetime import datetime
url='https://api.alternative.me/fng/'
params={'limit':365,'format':'json'}
data=requests.get(url,params=params).json()
ts=datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
os.makedirs('data/bronze/fear_greed',exist_ok=True)
json.dump(data,open(f'data/bronze/fear_greed/fear_greed_{ts}.json','w'),indent=2)