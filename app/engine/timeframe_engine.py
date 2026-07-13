from __future__ import annotations


class TimeframeEngine:


    def calculate(
        self,
        coin
    ):


        trend = coin.timeframe_trend


        score = (

            trend.tf_5m.trend * 0.20

            +

            trend.tf_15m.trend * 0.30

            +

            trend.tf_1h.trend * 0.30

            +

            trend.tf_4h.trend * 0.20

        )


        trend.score = score

        trend.updated = True



timeframe_engine = TimeframeEngine()