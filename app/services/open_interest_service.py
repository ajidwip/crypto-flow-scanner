from __future__ import annotations

import asyncio
import aiohttp

from app.core.market import market

from app.core.priority_market import priority_market


class OpenInterestService:

    URL = (
        "https://fapi.binance.com"
        "/fapi/v1/openInterest"
    )


    async def start(self):

        while True:

            try:

                coins = priority_market.symbols

                # sementara ambil top 50 saja
                # agar tidak kena rate limit Binance

                for coin in coins[:50]:

                    await self.update_coin(
                        coin
                    )

                    await asyncio.sleep(
                        0.1
                    )


            except Exception:

                pass


            await asyncio.sleep(
                60
            )


    async def update_coin(
        self,
        coin
    ):

        params = {

            "symbol": coin.symbol

        }


        async with aiohttp.ClientSession() as session:

            async with session.get(
                self.URL,
                params=params,
            ) as response:

                data = await response.json()


        value = float(
            data["openInterest"]
        )


        oi = coin.open_interest


        if oi.value > 0:

            oi.previous = oi.value


        oi.value = value


        if oi.previous > 0:

            oi.delta = (
                oi.value -
                oi.previous
            )


            oi.percentage = (
                oi.delta /
                oi.previous
            ) * 100


        oi.score = self.calculate_score(
            oi.percentage
        )


        oi.updated = True



    def calculate_score(
        self,
        percentage
    ):

        if percentage >= 5:

            return 100


        elif percentage >= 2:

            return 80


        elif percentage > 0:

            return 60


        elif percentage <= -5:

            return 20


        else:

            return 40



open_interest_service = OpenInterestService()