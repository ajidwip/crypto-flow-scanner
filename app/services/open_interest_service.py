from __future__ import annotations

import asyncio

from app.core.market import market
from app.network.rest_client import rest
from app.core.priority_market import priority_market


class OpenInterestService:

    async def start(self):

        while True:

            for symbol in priority_market.all():

                coin = market.get(symbol)

                if coin is None:
                    continue

                try:

                    data = await rest.open_interest(
                        coin.symbol
                    )

                    value = float(
                        data["openInterest"]
                    )

                    oi = coin.open_interest

                    oi.previous = oi.value

                    oi.value = value

                    if oi.previous:

                        oi.delta = (

                            oi.value

                            -

                            oi.previous

                        )

                        oi.percent = (

                            oi.delta

                            /

                            oi.previous

                        ) * 100

                    oi.updated = True

                except:

                    pass

            await asyncio.sleep(10)


open_interest_service = OpenInterestService()