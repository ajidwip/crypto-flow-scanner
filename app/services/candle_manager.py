from __future__ import annotations

import logging
from datetime import datetime

from app.core.market import market
from app.models.candle import Candle

logger = logging.getLogger("FLOW")


class CandleManager:

    async def on_message(self, payload: dict):

        if "data" not in payload:
            return

        data = payload["data"]

        if data.get("e") != "kline":
            return

        k = data["k"]

        symbol = data["s"]

        coin = market.get(symbol)

        if coin is None:
            return

        candle = self._build_candle(symbol, k)

        self._update_coin(coin, candle)

    def _build_candle(
        self,
        symbol: str,
        k: dict,
    ) -> Candle:

        return Candle(

            symbol=symbol,

            interval=k["i"],

            open_time=datetime.fromtimestamp(
                k["t"] / 1000
            ),

            close_time=datetime.fromtimestamp(
                k["T"] / 1000
            ),

            open=float(k["o"]),

            high=float(k["h"]),

            low=float(k["l"]),

            close=float(k["c"]),

            volume=float(k["v"]),

            quote_volume=float(k["q"]),

            trades=int(k["n"]),

            taker_buy_base_volume=float(k["V"]),

            taker_buy_quote_volume=float(k["Q"]),

            is_closed=k["x"],
        )

    def _update_coin(
        self,
        coin,
        candle: Candle,
    ):

        if coin.last_candle:

            if (
                coin.last_candle.close_time
                ==
                candle.close_time
            ):

                coin.candles[-1] = candle

            else:

                coin.add_candle(candle)

        else:

            coin.add_candle(candle)

        if candle.is_closed:

            logger.info(

                "%-12s  %10.4f   Vol:%12.2f",

                coin.symbol,

                candle.close,

                candle.volume,

            )


candle_manager = CandleManager()