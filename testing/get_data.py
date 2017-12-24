import requests
import json


# get the currencies
r = requests.get('https://poloniex.com/public?command=returnCurrencies')
with open('currencies.json', 'w') as f:
    f.write(r.content)

currencies = json.loads(r.content)
curname = currencies.keys()

# download history for BTC currencies
for currency in curname:
    r = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=BTC_%s&start=1497559748&end=9999999999&period=300' % currency)
    if len(r.content)==34:
        continue
    with open('currencies/BTC_%s.json' % currency, 'w') as f:
        f.write(r.content)
