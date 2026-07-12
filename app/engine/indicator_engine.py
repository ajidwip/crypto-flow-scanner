from __future__ import annotations

import logging

from app.models.coin import Coin


logger = logging.getLogger("FLOW")


class IndicatorEngine:


    def calculate(
        self,
        coin: Coin
    ):

        if len(coin.candles) < 200:
            return


        closes = coin.working_close_prices

        highs = coin.working_high_prices

        lows = coin.working_low_prices

        volumes = coin.working_volumes


        indicator = coin.indicator


        indicator.ema9 = self.ema(
            closes,
            9
        )


        indicator.ema20 = self.ema(
            closes,
            20
        )


        indicator.ema50 = self.ema(
            closes,
            50
        )


        indicator.ema100 = self.ema(
            closes,
            100
        )


        indicator.ema200 = self.ema(
            closes,
            200
        )


        indicator.sma20 = self.sma(
            closes,
            20
        )


        indicator.sma50 = self.sma(
            closes,
            50
        )


        indicator.sma100 = self.sma(
            closes,
            100
        )


        indicator.sma200 = self.sma(
            closes,
            200
        )


        indicator.rsi14 = self.rsi(
            closes,
            14
        )


        indicator.atr14 = self.atr(
            highs,
            lows,
            closes,
            14
        )


        indicator.volume_ma20 = self.sma(
            volumes,
            20
        )


        indicator.vwap = self.vwap(
            coin
        )


        indicator.momentum10 = (
            closes[-1] -
            closes[-10]
        )


        indicator.volatility = (
            indicator.atr14 /
            closes[-1]
            *
            100
        )

    def sma(
        self,
        data,
        period
    ):

        if len(data) < period:
            return 0.0

        return sum(
            data[-period:]
        ) / period



    def ema(
        self,
        data,
        period
    ):

        if len(data) < period:
            return 0.0


        multiplier = (
            2 /
            (period + 1)
        )


        ema = sum(
            data[:period]
        ) / period


        for price in data[period:]:

            ema = (
                price * multiplier
            ) + (
                ema *
                (1 - multiplier)
            )


        return ema

    def rsi(
        self,
        data,
        period
    ):

        if len(data) <= period:
            return 0.0


        gains = []

        losses = []


        for i in range(
            1,
            len(data)
        ):

            diff = (
                data[i]
                -
                data[i-1]
            )


            if diff >= 0:

                gains.append(
                    diff
                )

                losses.append(
                    0
                )

            else:

                gains.append(
                    0
                )

                losses.append(
                    abs(diff)
                )


        avg_gain = sum(
            gains[-period:]
        ) / period


        avg_loss = sum(
            losses[-period:]
        ) / period


        if avg_loss == 0:

            return 100.0


        rs = (
            avg_gain /
            avg_loss
        )


        return (
            100 -
            (
                100 /
                (1 + rs)
            )
        )



    def atr(
        self,
        highs,
        lows,
        closes,
        period
    ):

        trs = []


        for i in range(
            1,
            len(closes)
        ):

            tr = max(

                highs[i] - lows[i],

                abs(
                    highs[i]
                    -
                    closes[i-1]
                ),

                abs(
                    lows[i]
                    -
                    closes[i-1]
                )

            )

            trs.append(tr)



        if len(trs) < period:
            return 0.0


        return sum(
            trs[-period:]
        ) / period

    def vwap(
        self,
        coin
    ):

        total_volume = 0

        total_price_volume = 0


        for candle in coin.candles:

            price = candle.hlc3

            volume = candle.volume


            total_price_volume += (
                price *
                volume
            )


            total_volume += volume


        if total_volume == 0:

            return 0.0


        return (
            total_price_volume /
            total_volume
        )



indicator_engine = IndicatorEngine()