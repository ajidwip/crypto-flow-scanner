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

        breakout = self.breakout_score(
            coin
        )

        delta = self.delta_score(coin)

        cvd = self.cvd_score(coin)

        coin.score.cvd = cvd

        coin.score.whale = self.whale_score(coin)

        coin.score.volume = volume

        coin.score.momentum = momentum

        coin.score.money_flow = money_flow

        coin.score.trend = trend

        coin.score.breakout = breakout

        coin.score.delta = delta

        whale = coin.score.whale

        total = (

            volume * 0.18 +

            momentum * 0.18 +

            candle * 0.12 +

            money_flow * 0.12 +

            trend * 0.10 +

            whale * 0.10 +

            delta * 0.10 +

            cvd * 0.10

        )


        coin.score.total = round(
            total,
            2
        )

        self.update_signal(
            coin
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

    def breakout_score(
        self,
        coin,
    ):

        candles = list(coin.candles)

        if len(candles) < 30:

            return 0

        current = candles[-1]

        highs = [

            c.high

            for c in candles[-21:-1]

        ]

        lows = [

            c.low

            for c in candles[-21:-1]

        ]

        resistance = max(highs)

        support = min(lows)

        if resistance == support:
            return 50

        if current.close > resistance:

            return 100

        if current.close < support:

            return 0

        distance = (

            (current.close - support)

            /

            (resistance - support)

        )

        return max(
            0,
            min(
                distance * 100,
                100,
            ),
        )


    def whale_score(self, coin):

        pressure = coin.whale_cache.pressure

        return pressure * 100

    def delta_score(self, coin):

        return coin.delta_volume.pressure * 100

    def cvd_score(
        self,
        coin,
    ):

        value = coin.cvd.value

        if value >= 500:

            return 100

        if value >= 250:

            return 80

        if value >= 100:

            return 60

        if value >= 0:

            return 40

        return 20

    def update_signal(
        self,
        coin,
    ):

        score = coin.score.total

        if score >= 85:

            coin.score.signal = "STRONG BUY"

        elif score >= 70:

            coin.score.signal = "BUY"

        elif score >= 55:

            coin.score.signal = "WATCH"

        elif score >= 40:

            coin.score.signal = "NEUTRAL"

        elif score >= 25:

            coin.score.signal = "WEAK"

        else:

            coin.score.signal = "SELL"

flow_engine = FlowEngine()