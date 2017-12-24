import requests
import json


# get the usdt btc currencies
r = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1497559748&end=9999999999&period=300')
with open('currencies/USDT_BTC.json', 'w') as f:
    f.write(r.content)
