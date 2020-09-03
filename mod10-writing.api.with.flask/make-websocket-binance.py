import asyncio
import json

import websockets

trades = []

async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        trades.append({"symbol": trade['s'], "price": float(trade['p']), "quantity": float(trade['q'])})
        print(trades)

async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()