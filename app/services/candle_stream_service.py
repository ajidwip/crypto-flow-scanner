from __future__ import annotations

import logging
from datetime import datetime, timezone

from app.core.market import market
from app.models.candle import Candle
from app.engine.indicator_engine import indicator_engine
from app.engine.flow_engine import flow_engine


logger = logging.getLogger("FLOW")


class CandleStreamService:


    async def handle(
        self,
        payload: dict
    ):


        try:

            data = payload.get(
                "data"
            )


            if not data:

                return



            if data.get("e") != "kline":

                return



            kline = data.get(
                "k"
            )


            if not kline:

                return



            symbol = kline.get(
                "s"
            )


            coin = market.get(
                symbol
            )


            if coin is None:

                return



            candle = Candle(

                symbol=symbol,

                interval=kline.get(
                    "i",
                    "5m"
                ),

                open_time=datetime.fromtimestamp(

                    kline["t"] / 1000,

                    tz=timezone.utc

                ),

                close_time=datetime.fromtimestamp(

                    kline["T"] / 1000,

                    tz=timezone.utc

                ),

                open=float(
                    kline["o"]
                ),

                high=float(
                    kline["h"]
                ),

                low=float(
                    kline["l"]
                ),

                close=float(
                    kline["c"]
                ),

                volume=float(
                    kline["v"]
                ),

                quote_volume=float(
                    kline["q"]
                ),

                trades=int(
                    kline["n"]
                ),

                taker_buy_base_volume=float(
                    kline["V"]
                ),

                taker_buy_quote_volume=float(
                    kline["Q"]
                ),

                is_closed=kline["x"]

            )



            self.update_coin(
                coin,
                candle
            )



        except Exception as ex:

            logger.exception(
                "Candle Stream Error : %s",
                ex
            )



    def update_coin(
        self,
        coin,
        candle
    ):


        last = coin.last_candle



        # candle masih berjalan
        if last and last.open_time == candle.open_time:

            coin.candles[-1] = candle


        else:

            coin.add_candle(
                candle
            )



        if coin.ready:


            indicator_engine.calculate(
                coin
            )


            flow_engine.calculate(
                coin
            )



candle_stream_service = CandleStreamService()