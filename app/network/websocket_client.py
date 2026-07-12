from __future__ import annotations

import asyncio
import json
import logging
from typing import Awaitable
from typing import Callable

import aiohttp

logger = logging.getLogger("FLOW")


MessageCallback = Callable[[dict], Awaitable[None]]


class WebSocketClient:

    def __init__(
        self,
        name: str,
        streams: list[str],
        callback: MessageCallback,
    ):

        self.name = name

        self.streams = streams

        self.callback = callback

        self.session: aiohttp.ClientSession | None = None

        self.ws = None

        self.running = False

    @property
    def url(self) -> str:

        return (
            "wss://fstream.binance.com/stream?streams="
            + "/".join(self.streams)
        )

    async def start(self):

        self.running = True

        timeout = aiohttp.ClientTimeout(total=None)

        self.session = aiohttp.ClientSession(
            timeout=timeout
        )

        while self.running:

            try:

                await self._connect()

            except asyncio.CancelledError:

                raise

            except Exception as ex:

                logger.exception(
                    "[%s] %s",
                    self.name,
                    ex,
                )

                await self.reconnect()

    async def stop(self):

        self.running = False

        try:

            if self.ws:

                await self.ws.close()

        except:
            pass

        try:

            if self.session:

                await self.session.close()

        except:
            pass

    async def _connect(self):

        logger.info(
            "[%s] Connecting...",
            self.name
        )

        async with self.session.ws_connect(

            self.url,

            heartbeat=20,

            autoping=True,

            compress=15,

        ) as ws:

            self.ws = ws

            logger.info(

                "[%s] Connected (%s streams)",

                self.name,

                len(self.streams),

            )

            logger.info(
                "[%s] %s",
                self.name,
                self.url[:120] + "...",
            )

            await self._listen()

    async def _listen(self):

        async for msg in self.ws:

            try:

                await self._handle_message(msg)

            except Exception:

                logger.exception(
                    "[%s] Callback Error",
                    self.name,
                )

        logger.warning(
            "[%s] WebSocket loop ended",
            self.name,
        )

        raise RuntimeError("Connection Lost")

    async def _handle_message(self, msg: aiohttp.WSMessage):

        if msg.type == aiohttp.WSMsgType.TEXT:

            try:

                payload = json.loads(msg.data)

                await self.callback(payload)

            except Exception:

                logger.exception(
                    "[%s] Invalid Payload",
                    self.name,
                )

            return

        if msg.type == aiohttp.WSMsgType.ERROR:

            raise RuntimeError(
                self.ws.exception()
            )

        if msg.type in (
            aiohttp.WSMsgType.CLOSE,
            aiohttp.WSMsgType.CLOSED,
            aiohttp.WSMsgType.CLOSING,
        ):

            raise RuntimeError(
                "WebSocket Closed"
            )

    async def reconnect(self):

        logger.warning(
            "[%s] Reconnecting in 5 seconds...",
            self.name,
        )

        await asyncio.sleep(5)
