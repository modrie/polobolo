## used for testing the trading engine with historical candle data


import os
import time
import json
import gc

data_dir = 'currencies'

# load the filenames
flist = os.listdir(data_dir)

# load the files (this may take some time)
t1 = time.time()
master = {}
for f in flist:
    print("loading %s" % f)
    with open('%s/%s' % (data_dir, f),'r') as fn:
        master[os.path.splitext("%s" % f)[0]] = json.loads(fn.read())
    gc.collect()

print("load completed in", time.time()-t1, "seconds")

# load the current times for the currencies
current_times = {}
for f in flist:
    fn = os.path.splitext(f)[0]
    current_times[fn] = master[fn][0]['date']

# print current_times
# value_history =

# loop through all times
time = current_times['BTC_XMR']
print(master['BTC_XMR'][0])

#for i in range(300):
