import urllib
import hmac
import hashlib
import json
import time
import requests

class polowrapper(object):
    def __init__(self, key, secret):
        self.key=key
        self.secret=secret

    def getSign(self, req):
        post_data = urllib.urlencode(req)
        return hmac.new(self.secret, post_data, hashlib.sha512).hexdigest()

    def returnBalances(self):
        req = {}
        req['nonce'] = int(time.time()*1000)
        req['command'] = "returnBalances"
        headers = {'Key':self.key, 'Sign':self.getSign(req)}
        r = requests.post("https://poloniex.com/tradingApi",headers=headers, data=req)
        return json.loads(r.text)

    def returnHolds(self):
        ndict = {}
        for key, value in self.returnBalances().iteritems():
            if value != '0.00000000':
                ndict[key] = value
        return ndict

    @staticmethod
    def getCurrPairs():
        currs = []
        r = requests.get('https://poloniex.com/public?command=return24hVolume')

        currencies = json.loads(r.content)
        count = 0
        # download history for BTC currencies
        for key,currency in currencies.iteritems():
            if key[0:3] == 'BTC':
                currs.append(key)
        return currs

    @staticmethod
    def getCurrIndices():
        ind = {}
        r = requests.get('https://poloniex.com/public?command=return24hVolume')
        s = requests.get('https://poloniex.com/public?command=returnCurrencies')
        currencies = json.loads(r.content)
        db = json.loads(s.content)
        count = 0
        # download history for BTC currencies
        for key,currency in currencies.iteritems():
            if key[0:4] == 'BTC_':
                ind[db[key[4:]]['id']]=key
        return ind

    @staticmethod
    def getCurrHistory(dur):
        #duration in minutes
        outs = {}
        for curr in ['BTC_XMR', "BTC_ETH"]: #polowrapper.getCurrPairs():
            ts = int(time.time())
            req = {}
            req['command'] = "returnChartData"
            req['currencyPair'] = curr
            req['start'] = ts-(dur*60)
            req['end'] = ts
            req['period'] = 300
            r = requests.get("https://poloniex.com/public",params=req)
            print r
            d = json.loads(r.text)
            outs[curr] = d
        return outs


if __name__ == "__main__":
    for dct in polowrapper.getCurrHistory(120)["BTC_ETH"]:
        print dct
