import time

import requests
import schedule

"""
resp = requests.get("https://api.binance.com/api/v3/ticker/price")
for ticker in resp.json():
    print("%12s %-8.3f" % (ticker['symbol'],float(ticker['price'])))
"""
def call_binance():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    print(resp.json())

schedule.every(1).seconds.do(call_binance)

while 1:
    schedule.run_pending()
    time.sleep(1)