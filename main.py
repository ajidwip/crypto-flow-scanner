from __future__ import annotations

import asyncio
import logging

from app.engine.scanner_engine import scanner_engine
from app.network.rest_client import rest
from app.network.websocket_client import WebSocketClient
from app.services.historical_loader import historical_loader
from app.services.symbol_loader import symbol_loader
from app.services.trade_stream_service import trade_stream_service
from app.services.system_monitor import system_monitor
from app.services.orderbook_stream_service import orderbook_stream_service
from app.services.open_interest_service import open_interest_service
from app.core.market import market
from app.services.funding_rate_service import funding_rate_service


logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

)


async def callback(payload):

    data = payload.get("data")

    if not data:
        return

    event = data.get("e")

    if event == "trade":

        await trade_stream_service.handle(payload)

    elif event == "depthUpdate":

        await orderbook_stream_service.handle(payload)


async def create_clients():

    clients = []

    symbols = symbol_loader.symbols()

    streams = []

    for symbol in symbols:

        streams.append(
            f"{symbol.lower()}@trade"
        )

        streams.append(
            f"{symbol.lower()}@depth20@100ms"
        )

    group_size = 100

    for i in range(0, len(streams), group_size):

        group = streams[i:i + group_size]

        clients.append(

            WebSocketClient(

                name=f"WS-{len(clients)+1}",

                streams=group,

                callback=callback,

            )

        )

    return clients


async def open_interest_loop():

    while True:

        coins = market.all()

        for coin in coins[:50]:

            await open_interest_service.update_coin(
                coin
            )

            await asyncio.sleep(
                0.05
            )


        await asyncio.sleep(
            60
        )


async def main():

    logging.info("======================================")

    logging.info("Crypto Flow Scanner")

    logging.info("======================================")

    await symbol_loader.load()

    await historical_loader.load()

    clients = await create_clients()

    tasks = []

    for client in clients:

        tasks.append(

            asyncio.create_task(

                client.start()

            )

        )

    tasks.append(

        asyncio.create_task(

            scanner_engine.start()

        )

    )
        
    tasks.append(

        asyncio.create_task(

            system_monitor.start()

        )

    )

    tasks.append(

        asyncio.create_task(
            open_interest_loop()
        )

    )

    tasks.append(

        asyncio.create_task(

            open_interest_service.start()

        )

    )

    tasks.append(

        asyncio.create_task(

            funding_rate_service.start()

        )

    )

    try:

        await asyncio.gather(*tasks)

    finally:

        scanner_engine.stop()

        for client in clients:

            await client.stop()

        await rest.close()


if __name__ == "__main__":

    asyncio.run(main())