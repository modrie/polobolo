import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
from plot_engine import curr_plot

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

print df2['weightedAverage'].corr(df2['open'])

x=curr_plot(df)
x.pltprice1()
