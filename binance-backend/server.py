import asyncio
import json
import threading

import flask
import websockets
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS, cross_origin

host = "127.0.0.1"
port = 4040

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print(f'received message: {message}')


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        mappedTrade = {"symbol": trade['s'], "price": float(trade['p']), "quantity": float(trade['q'])}
        socketio.emit("trade", mappedTrade)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


def runSocketio():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(connect())
    loop.run_forever()
    print("deneme")

socketio.run(app, port=port)


if __name__ == "__main__":
    print("App is starting...")
    t = threading.Thread(target=runSocketio)
    t.start()
