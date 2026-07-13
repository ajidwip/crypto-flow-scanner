from __future__ import annotations

import asyncio
import aiohttp

from app.core.priority_market import priority_market


class FundingRateService:

    URL = (
        "https://fapi.binance.com"
        "/fapi/v1/premiumIndex"
    )


    async def start(self):

        while True:

            try:

                coins = priority_market.coins

                for coin in coins:

                    await self.update_coin(
                        coin
                    )

                    await asyncio.sleep(
                        0.1
                    )


            except Exception as e:

                print(
                    "FUNDING ERROR",
                    e
                )


            await asyncio.sleep(
                60
            )



    async def update_coin(
        self,
        coin
    ):

        params = {

            "symbol":
            coin.symbol

        }


        async with aiohttp.ClientSession() as session:

            async with session.get(
                self.URL,
                params=params
            ) as response:

                data = await response.json()


        rate = float(
            data.get(
                "lastFundingRate",
                0
            )
        )


        funding = coin.funding_rate


        funding.rate = rate


        funding.updated = True


        funding.score = (
            self.calculate_score(
                rate
            )
        )



    def calculate_score(
        self,
        rate
    ):

        # normal bullish

        if 0 < rate < 0.0005:

            return 80


        # netral

        if -0.0005 <= rate <= 0:

            return 60


        # terlalu banyak long

        if rate >= 0.001:

            return 20


        # terlalu bearish

        if rate <= -0.001:

            return 40


        return 50



funding_rate_service = FundingRateService()