from __future__ import annotations

import asyncio
import logging
from datetime import datetime

from app.core.market import market
from app.models.candle import Candle
from app.network.rest_client import rest


logger = logging.getLogger("FLOW")


class HistoricalLoader:


    def __init__(self):

        self.interval = "5m"

        self.limit = 500


    async def load(self):

        coins = market.all()


        logger.info(
            "Loading historical candles : %s coins",
            len(coins)
        )


        semaphore = asyncio.Semaphore(10)


        async def worker(coin):

            async with semaphore:

                await self.load_coin(
                    coin.symbol,
                    coin
                )


        tasks = [
            worker(coin)
            for coin in coins
        ]


        await asyncio.gather(
            *tasks
        )


        logger.info(
            "Historical loading finished"
        )

    async def load_coin(
        self,
        symbol: str,
        coin,
    ):

        try:

            data = await rest.klines(

                symbol,

                self.interval,

                self.limit,

            )


            for item in data:

                candle = self.parse_candle(
                    symbol,
                    item
                )


                coin.add_candle(
                    candle
                )


            logger.info(

                "%-12s %s candles",

                symbol,

                len(coin.candles)

            )


        except Exception as ex:


            logger.error(

                "%s historical error : %s",

                symbol,

                ex

            )

    def parse_candle(
        self,
        symbol: str,
        item: list,
    ) -> Candle:


        return Candle(

            symbol=symbol,

            interval=self.interval,


            open_time=datetime.fromtimestamp(
                item[0] / 1000
            ),


            close_time=datetime.fromtimestamp(
                item[6] / 1000
            ),


            open=float(item[1]),

            high=float(item[2]),

            low=float(item[3]),

            close=float(item[4]),

            volume=float(item[5]),

            quote_volume=float(item[7]),

            trades=int(item[8]),

            taker_buy_base_volume=float(
                item[9]
            ),

            taker_buy_quote_volume=float(
                item[10]
            ),

            is_closed=True,

        )



historical_loader = HistoricalLoader()