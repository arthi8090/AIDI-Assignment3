import pandas as pd, json, glob
b=sorted(glob.glob('data/bronze/binance/*.json'))[-1]
df=pd.DataFrame(json.load(open(b)),columns=['open_time','open','high','low','close','volume','ct','q','t','tb','tq','i'])
df['date']=pd.to_datetime(df['open_time'],unit='ms').dt.date
df['btc_close']=df['close'].astype(float)
df['btc_volume']=df['volume'].astype(float)
df[['date','btc_close','btc_volume']].to_csv('data/silver/btc_daily_clean.csv',index=False)
f=sorted(glob.glob('data/bronze/fear_greed/*.json'))[-1]
df=pd.DataFrame(json.load(open(f))['data'])
df['date']=pd.to_datetime(df['timestamp'],unit='s').dt.date
df['fear_greed_value']=df['value'].astype(int)
df.rename(columns={'value_classification':'fear_greed_label'},inplace=True)
df[['date','fear_greed_value','fear_greed_label']].to_csv('data/silver/fear_greed_clean.csv',index=False)