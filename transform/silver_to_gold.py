import pandas as pd
b=pd.read_csv('data/silver/btc_daily_clean.csv')
f=pd.read_csv('data/silver/fear_greed_clean.csv')
b['date']=pd.to_datetime(b['date'])
f['date']=pd.to_datetime(f['date'])
df=pd.merge(b,f,on='date')
df['btc_daily_return']=df['btc_close'].pct_change()
df['positive_return']=(df['btc_daily_return']>0).astype(int)
df.dropna().to_csv('data/gold/crypto_sentiment_daily.csv',index=False)