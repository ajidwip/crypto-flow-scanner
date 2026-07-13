from __future__ import annotations


class RegimeEngine:

    def calculate(
        self,
        coin,
    ):

        mtf = coin.timeframe_trend

        score = mtf.score

        if score >= 75:
            regime = "TRENDING"

        elif score >= 50:
            regime = "RANGING"

        elif score >= 30:
            regime = "VOLATILE"

        else:
            regime = "CHOPPY"

        coin.market_regime.regime = regime
        coin.market_regime.score = score
        coin.market_regime.updated = True


regime_engine = RegimeEngine()