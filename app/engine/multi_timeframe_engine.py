from __future__ import annotations


class MultiTimeframeEngine:


    def calculate(
        self,
        coin
    ):

        candles = coin.candles


        if len(candles) < 200:
            return


        mtf = coin.timeframe_trend


        price = candles[-1].close


        ema20 = coin.indicator.ema20

        ema50 = coin.indicator.ema50


        def calculate_tf(tf):

            tf.ema_fast = ema20

            tf.ema_slow = ema50


            if ema20 > ema50:

                tf.trend = 100

                tf.bullish = True

                tf.bearish = False


            elif ema20 < ema50:

                tf.trend = 0

                tf.bullish = False

                tf.bearish = True


            else:

                tf.trend = 50


            tf.momentum = (
                (price - ema20)
                /
                ema20
                *
                100
            )


            tf.updated = True



        calculate_tf(
            mtf.tf_5m
        )

        calculate_tf(
            mtf.tf_15m
        )

        calculate_tf(
            mtf.tf_1h
        )

        calculate_tf(
            mtf.tf_4h
        )


        mtf.score = (

            mtf.tf_5m.trend * 0.20
            +
            mtf.tf_15m.trend * 0.30
            +
            mtf.tf_1h.trend * 0.30
            +
            mtf.tf_4h.trend * 0.20

        )


        mtf.updated = True



multi_timeframe_engine = MultiTimeframeEngine()