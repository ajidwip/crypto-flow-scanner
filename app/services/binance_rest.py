from __future__ import annotations

import aiohttp

from app.config.settings import settings


class BinanceRestClient:

    def __init__(self) -> None:

        self.base_url = settings.BINANCE_REST.rstrip("/")

        self.timeout = aiohttp.ClientTimeout(total=30)

        self.session: aiohttp.ClientSession | None = None

    async def connect(self) -> None:

        if self.session is None:

            self.session = aiohttp.ClientSession(
                timeout=self.timeout
            )

    async def close(self) -> None:

        if self.session:

            await self.session.close()

            self.session = None

    async def get(
        self,
        endpoint: str,
        params: dict | None = None
    ) -> dict:

        if self.session is None:

            await self.connect()

        async with self.session.get(

            f"{self.base_url}{endpoint}",

            params=params

        ) as response:

            response.raise_for_status()

            return await response.json()

    async def exchange_info(self) -> dict:

        return await self.get(

            "/fapi/v1/exchangeInfo"

        )

    async def ticker_24hr(self) -> list:

        return await self.get(

            "/fapi/v1/ticker/24hr"

        )

    async def open_interest(

        self,

        symbol: str

    ) -> dict:

        return await self.get(

            "/fapi/v1/openInterest",

            {

                "symbol": symbol

            }

        )

    async def funding_rate(

        self,

        symbol: str,

        limit: int = 1

    ) -> list:

        return await self.get(

            "/fapi/v1/fundingRate",

            {

                "symbol": symbol,

                "limit": limit

            }

        )

    async def klines(

        self,

        symbol: str,

        interval: str = "5m",

        limit: int = 500

    ) -> list:

        return await self.get(

            "/fapi/v1/klines",

            {

                "symbol": symbol,

                "interval": interval,

                "limit": limit

            }

        )


binance = BinanceRestClient()