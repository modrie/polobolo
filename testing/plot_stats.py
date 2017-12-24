import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

data_dir = 'currencies/'
# flist = os.listdir(data_dir)
testfile = 'BTC_LSK.json'
usdt = "USDT_BTC.json"

f1 = open('%s%s' % (data_dir, usdt),'r')
data = json.loads(f1.read())
f1.close
df = pd.DataFrame(data=data)

f2 = open('%s%s' % (data_dir, testfile),'r')
data2 = json.loads(f2.read())
f2.close
df2 = pd.DataFrame(data=data2)
print df2['high'].corr(df2['low'])
print df2['date'].iloc[-300:], df2['volume'].iloc[-300:]
plt.plot(df2['date'].iloc[-300:], df2['quoteVolume'].iloc[-300:])
plt.show()
