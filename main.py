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


logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

)


async def callback(payload):

    await trade_stream_service.handle(payload)


async def create_clients():

    clients = []

    symbols = symbol_loader.symbols()

    streams = [

        f"{symbol.lower()}@trade"

        for symbol in symbols

    ]

    group_size = 150

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

    try:

        await asyncio.gather(*tasks)

    finally:

        scanner_engine.stop()

        for client in clients:

            await client.stop()

        await rest.close()


if __name__ == "__main__":

    asyncio.run(main())