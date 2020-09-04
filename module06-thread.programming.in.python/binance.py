import time

import requests
import grequests


def get_ticker(symbol):
    return requests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}").content

def async_get_tickers():
    return (grequests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}") for symbol in symbols)


symbols = ["LTCBTC", "BNBBTC", "NEOBTC", "QTUMETH", "EOSETH", "SNTETH", "BNTETH", "BCCBTC", "GASBTC", "BNBETH",
           "BTCUSDT", "ETHUSDT", "HSRBTC", "OAXETH", "DNTETH", "MCOETH", "ICNETH", "MCOBTC", "WTCBTC", "WTCETH",
           "LRCBTC", "LRCETH", "QTUMBTC", "YOYOBTC", "OMGBTC", "OMGETH", "ZRXBTC", "ZRXETH", "STRATBTC", "STRATETH",
           "SNGLSBTC", "SNGLSETH", "BQXBTC", "BQXETH", "KNCBTC", "KNCETH", "FUNBTC", "FUNETH", "SNMBTC", "SNMETH",
           "NEOETH", "IOTABTC", "IOTAETH", "LINKBTC", "LINKETH", "XVGBTC", "XVGETH", "SALTBTC", "SALTETH", "MDABTC"]


def sync_call():
    for symbol in symbols:
        ticker = get_ticker(symbol)
        print(ticker)



start = time.perf_counter()
for ticker in grequests.map(async_get_tickers()):
    print(ticker)
elapsed_time = time.perf_counter() - start
print(f"{__file__} executed in {elapsed_time:3.2f} seconds")
