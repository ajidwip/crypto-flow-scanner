from __future__ import annotations


class TimeframeEngine:

    def calculate(
        self,
        coin,
    ):

        score = coin.score

        trend = score.trend

        tf = coin.timeframe

        tf.m5 = trend

        tf.m15 = trend

        tf.h1 = trend

        tf.h4 = trend

        tf.total = (

            tf.m5 * 0.25 +

            tf.m15 * 0.25 +

            tf.h1 * 0.25 +

            tf.h4 * 0.25

        )

        tf.updated = True


timeframe_engine = TimeframeEngine()