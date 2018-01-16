import requests
import json


# get the currencies
currs = []
r = requests.get('https://poloniex.com/public?command=return24hVolume')

currencies = json.loads(r.content)
count = 0
# download history for BTC currencies
for key,currency in currencies.iteritems():
    if key[0:3] == 'BTC':
        currs.append(key)
