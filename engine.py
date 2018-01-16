from coinStream import coinStream
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import time
import hmac,hashlib
import urllib
from polowrapper import polowrapper
#from plot_engine import curr_plot
apikey = "ZP7KW315-2H8LTMG0-SNP9T571-EE87BY20"
secret = "e5c6427f377734c6ae15e04f7d66f124342394fb2e17fdda1eaca5684660b30c36cc2fbef22d616dd459127f57ea3699ad68b049da1e623a8b055cf3458ff513"
x = polowrapper(apikey, secret)
print x.returnHolds()

#the engine manage all balances



# orderbook = {}
# print "we are here"
# c = coinStream(orderbook)
# print "we are now here"
# print orderbook
# print len(orderbook)
