from __future__ import annotations

import logging

from app.core.market import market
from app.engine.flow_engine import flow_engine
from app.engine.indicator_engine import indicator_engine
from app.realtime.trade_manager import trade_manager
from app.core.market_events import market_events
from app.core.statistics import statistics
from app.models.trade import Trade
from app.services.whale_detector import whale_detector
from app.realtime.delta_volume import DeltaVolume


logger = logging.getLogger("FLOW")


class TradeStreamService:


    async def handle(
        self,
        payload: dict,
    ):

        data = payload.get("data")

        if not data:
            return


        if data.get("e") != "trade":
            return


        symbol = data["s"]

        coin = market.get(symbol)

        if coin is None:
            return


        price = float(data["p"])

        quantity = float(data["q"])

        trade_time = int(data["T"])

        statistics.trades += 1

        trade = Trade(

            symbol=symbol,

            price=price,

            quantity=quantity,

            value=price * quantity,

            buyer_maker=data["m"],

            trade_time=trade_time,

        )

        coin.trade_cache.add(trade)

        coin.delta_volume.add(

            quantity,

            data["m"],

        )

        coin.cvd.add(

            quantity,

            data["m"],

        )

        whale = whale_detector.detect(trade)

        if whale:

            coin.whale_cache.add(whale)

        builder = trade_manager.builder(symbol)

        candle = builder.update(

            price,

            quantity,

            trade_time,

        )

        coin.live_candle = builder.current

        market_events.push(symbol)

        if candle:

            self.on_candle_closed(

                coin,

                candle,

            )

    def on_candle_closed(

        self,

        coin,

        candle,

    ):

        coin.add_candle(candle)

        coin.live_candle = None

        # logger.info(

        #     "%s Candle Closed %.2f",

        #     coin.symbol,

        #     candle.close,

        # )

trade_stream_service = TradeStreamService()