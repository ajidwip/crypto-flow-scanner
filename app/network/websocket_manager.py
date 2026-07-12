from __future__ import annotations

import asyncio
import logging

from app.network.websocket_client import WebSocketClient

logger = logging.getLogger("FLOW")


class WebSocketManager:

    def __init__(
        self,
        streams: list[str],
        callback,
        batch_size: int = 175,
    ):

        self.streams = streams

        self.callback = callback

        self.batch_size = batch_size

        self.clients: list[WebSocketClient] = []

    def build_groups(self) -> list[list[str]]:

        groups = []

        for i in range(0, len(self.streams), self.batch_size):

            groups.append(
                self.streams[i:i + self.batch_size]
            )

        return groups

    def build_clients(self):

        self.clients.clear()

        groups = self.build_groups()

        logger.info(
            "Total Streams : %s",
            len(self.streams),
        )

        logger.info(
            "Total Groups : %s",
            len(groups),
        )

        for index, group in enumerate(groups, start=1):

            client = WebSocketClient(

                name=f"WS-{index}",

                streams=group,

                callback=self.callback,

            )

            self.clients.append(client)

            logger.info(

                "%s -> %s streams",

                client.name,

                len(group),

            )

    async def start(self):

        self.build_clients()

        tasks = []

        for client in self.clients:

            tasks.append(

                asyncio.create_task(

                    client.start()

                )

            )

        await asyncio.gather(*tasks)

    async def stop(self):

        tasks = []

        for client in self.clients:

            tasks.append(

                asyncio.create_task(

                    client.stop()

                )

            )

        if tasks:

            await asyncio.gather(*tasks)