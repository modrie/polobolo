import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import time
from polowrapper import polowrapper

class orderbook(object):
    def __init__(self):
        #this is the orderbook. define a local orderBook
        self.obook = {}
        self.inttostr = {}
        self.strtoint = {}

        self.lastorder = {}

        self.lastprice = {}
        self.messno = 0

    def parse(self,message):
        self.messno += 1
        print self.messno 
        if len(message) > 2:
            cid = message[0]
            index = message[1]
            if self.lastorder.get(cid, 0) == 0:
                self.lastorder[cid]=index
            else:
                if self.lastorder[cid] != index-1:
                    print "UH OHHHHH"
            self.lastorder[cid] = index

            for line in message[2]:
                if line[0] == 'i': # this is an orderbook
                    cpair = line[1]['currencyPair']
                    self.obook[cpair] = line[1]['orderBook']
                    self.inttostr[cid] = cpair
                if line[0] == 'o': # this is an order
                    #print self.lastorder[cid], " ", index
                    #print line
                    if line[3] == "0.00000000":
                        self.obook[self.inttostr[cid]][line[1]].pop(line[2])
                    else:
                        self.obook[self.inttostr[cid]][line[1]][line[2]] = line[3]
                    #print line
        else:
            return

    def icoin(self, coin, book):
        #initialize a coin with a book
        self.obook[coin]=book

    def ubook(self, coin, price, value):
        #update a coin value in the book
        self.obook[coin][price]=value

    def get_momentum(self):
        return
