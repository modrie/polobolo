import os
import time
import json
import gc
import engine

data = None
data_dir = 'testing/currencies/'
# flist = os.listdir(data_dir)
flist = ['BTC_BCH.json']

for f in flist:
    with open('%s/%s' % (data_dir, f),'r') as fn:
        data = json.loads(fn.read())

    eng = engine.currency_pair(f, [], 0.03)

    balance_btc=1.0
    balance_alt=0

    money_in = False

    for i in data:
        #print i
        eng.add_timepoint(i)
        #print eng.get_current_price()
        if eng.risk == 1 and not money_in:
            balance_alt = balance_btc/eng.get_current_price()
            balance_btc = 0
            money_in = True
        elif eng.risk == -1 and money_in:
            balance_btc = balance_alt*eng.get_current_price()
            balance_alt = 0
            money_in = False
        else:
            continue

    if balance_btc == 0:
        print(f, balance_alt*eng.get_current_price(), balance_alt*eng.get_current_price()>1)
    else:
        print(f, balance_btc, balance_btc>1)
