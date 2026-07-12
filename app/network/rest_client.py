from __future__ import annotations

import asyncio
import logging
from typing import Any

import aiohttp

from app.config.settings import settings

logger = logging.getLogger("FLOW")


class RestClient:

    def __init__(self):

        self._session: aiohttp.ClientSession | None = None

    async def start(self):

        if self._session is None:

            timeout = aiohttp.ClientTimeout(
                total=30,
                connect=10,
                sock_connect=10,
                sock_read=30,
            )

            connector = aiohttp.TCPConnector(
                limit=100,
                limit_per_host=100,
                ttl_dns_cache=300,
                ssl=True,
            )

            self._session = aiohttp.ClientSession(
                timeout=timeout,
                connector=connector,
                headers={
                    "User-Agent": "CryptoFlowScanner/1.0"
                }
            )

    async def close(self):

        if self._session:

            await self._session.close()

            self._session = None

    async def get(
        self,
        endpoint: str,
        params: dict | None = None,
        retry: int = 3,
    ) -> Any:

        await self.start()

        url = settings.BINANCE_REST.rstrip("/") + endpoint

        last_error = None

        for attempt in range(retry):

            try:

                async with self._session.get(
                    url,
                    params=params
                ) as response:

                    if response.status != 200:

                        text = await response.text()

                        raise Exception(
                            f"HTTP {response.status} : {text}"
                        )

                    return await response.json()

            except Exception as ex:

                last_error = ex

                logger.warning(
                    "GET Retry %s/%s %s",
                    attempt + 1,
                    retry,
                    endpoint,
                )

                await asyncio.sleep(2)

        raise last_error

class BinanceRest:

    def __init__(self):

        self.client = RestClient()

    async def exchange_info(self):

        return await self.client.get(
            "/fapi/v1/exchangeInfo"
        )

    async def ticker_24h(self):

        return await self.client.get(
            "/fapi/v1/ticker/24hr"
        )

    async def klines(
        self,
        symbol: str,
        interval: str,
        limit: int = 500,
    ):

        return await self.client.get(
            "/fapi/v1/klines",
            params={
                "symbol": symbol,
                "interval": interval,
                "limit": limit,
            },
        )

    async def server_time(self):

        return await self.client.get(
            "/fapi/v1/time"
        )

    async def close(self):

        await self.client.close()


rest = BinanceRest()