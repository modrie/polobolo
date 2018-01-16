import websocket
import thread
import time
import json
import requests
from polowrapper import polowrapper
from orderbook import orderbook

class coinStream(object):
    def __init__(self, orderbook, currlist):
        print "hi"
        websocket.enableTrace(True)
        self.currlist = currlist
        self.orderbook = orderbook
        self.ws = websocket.WebSocketApp("wss://api2.poloniex.com/",
                                  on_message = self.on_message,
                                  on_error = self.on_error,
                                  on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, ws, message):
        mess = json.loads(message)
        self.orderbook.parse(mess)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        print("ONOPEN")

        def run(*args):
            #ws.send(json.dumps({'command':'subscribe','channel':1001}))
            #ws.send(json.dumps({'command':'subscribe','channel':1002}))
            #ws.send(json.dumps({'command':'subscribe','channel':1003}))
            for curr in self.currlist:
                print curr
                ws.send(json.dumps({'command':'subscribe','channel':'%s' % curr}))
            # ws.send(json.dumps({'command':'subscribe','channel':'BTC_XMR'}))
            while True:
                time.sleep(1)
            ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ob = orderbook()
    coins = coinStream(ob,polowrapper.getCurrPairs())
