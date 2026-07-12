from __future__ import annotations

import logging

from app.models.coin import Coin


logger = logging.getLogger("FLOW")


class FlowEngine:


    def calculate(
        self,
        coin: Coin
    ):

        if len(coin.candles) < 50:
            return


        volume = self.volume_score(
            coin
        )

        momentum = self.momentum_score(
            coin
        )

        candle = self.candle_score(
            coin
        )

        money_flow = self.buy_pressure_score(
            coin
        )

        trend = self.trend_score(
            coin
        )

        delta = self.delta_score(coin)

        coin.score.whale = self.whale_score(coin)

        coin.score.volume = volume

        coin.score.momentum = momentum

        coin.score.money_flow = money_flow

        coin.score.trend = trend

        coin.score.delta = delta

        whale = coin.score.whale

        total = (

            volume * 0.20 +

            momentum * 0.20 +

            candle * 0.15 +

            money_flow * 0.15 +

            trend * 0.10 +

            whale * 0.10 +

            delta * 0.10

        )


        coin.score.total = round(
            total,
            2
        )


        coin.score.updated = True



    def volume_score(
        self,
        coin
    ):

        volumes = coin.volumes


        current = volumes[-1]


        avg = (
            sum(
                volumes[-20:]
            )
            /
            20
        )


        if avg == 0:

            return 0


        ratio = current / avg


        if ratio >= 3:

            return 100


        if ratio >= 2:

            return 80


        if ratio >= 1.5:

            return 60


        if ratio >= 1:

            return 40


        return 20



    def momentum_score(
        self,
        coin
    ):

        candles = coin.candles


        now = candles[-1].close

        old = candles[-10].close


        change = (

            (now - old)

            /

            old

        ) * 100



        if change >= 5:

            return 100


        if change >= 3:

            return 80


        if change >= 1:

            return 60


        if change >= 0:

            return 40


        return 20



    def candle_score(
        self,
        coin
    ):

        candle = coin.last_candle


        if candle is None:

            return 0



        if candle.candle_range == 0:

            return 0



        strength = (

            candle.body_size

            /

            candle.candle_range

        )


        return min(
            strength * 100,
            100
        )



    def buy_pressure_score(
        self,
        coin
    ):

        candle = coin.last_candle


        if candle.volume == 0:

            return 0



        ratio = (

            candle.taker_buy_base_volume

            /

            candle.volume

        )


        return min(
            ratio * 100,
            100
        )



    def trend_score(
        self,
        coin
    ):

        indicator = coin.indicator


        if (

            indicator.ema20

            >

            indicator.ema50

        ):

            return 100



        if (

            indicator.ema20

            >

            indicator.ema200

        ):

            return 70



        return 30


    def whale_score(self, coin):

        pressure = coin.whale_cache.pressure

        return pressure * 100

    def delta_score(self, coin):

        return coin.delta_volume.pressure * 100



flow_engine = FlowEngine()