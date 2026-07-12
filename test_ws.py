import asyncio

from app.network.websocket_client import WebSocketClient
from app.network.rest_client import rest
from app.services.historical_loader import historical_loader
from app.services.symbol_loader import symbol_loader
from app.services.trade_stream_service import trade_stream_service


async def callback(payload):

    print("PAYLOAD RECEIVED")

    await trade_stream_service.handle(payload)


async def main():

    await symbol_loader.load()

    await historical_loader.load()


    client = WebSocketClient(

        name="BTC",

        streams=[

            "btcusdt@trade"

        ],

        callback=callback,

    )


    try:

        await client.start()

    finally:

        await client.stop()

        await rest.close()


asyncio.run(main())