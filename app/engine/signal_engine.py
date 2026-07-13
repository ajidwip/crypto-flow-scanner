from __future__ import annotations


class SignalEngine:

    def calculate(
        self,
        coin,
    ):

        score = coin.score.total

        signal = coin.signal

        signal.reason.clear()

        #mtf = coin.multi_timeframe.total_score

        if coin.score.trend >= 70:
            signal.reason.append("Trend Bullish")

        if coin.score.momentum >= 70:
            signal.reason.append("Momentum Strong")

        if coin.score.money_flow >= 70:
            signal.reason.append("Money Flow In")

        if coin.score.delta >= 70:
            signal.reason.append("Aggressive Buyers")

        if coin.score.cvd >= 70:
            signal.reason.append("CVD Rising")

        if coin.score.whale >= 70:
            signal.reason.append("Whale Buying")

        if coin.order_book_score.total >= 70:
            signal.reason.append("Bid Wall Dominant")

        if coin.volume_spike.score >= 40:
            signal.reason.append("Volume Spike")

        if coin.funding_rate.score >= 70:

            signal.reason.append(
                "✓ Funding Healthy"
            )

        elif coin.funding_rate.score <= 30:

            signal.reason.append(
                "⚠ Funding Risk"
            )

        if score >= 85:
            signal.direction = "STRONG BUY"
        elif score >= 70:
            signal.direction = "BUY"
        elif score >= 60:
            signal.direction = "WATCH BUY"
        elif score >= 40:
            signal.direction = "NEUTRAL"
        elif score >= 30:
            signal.direction = "WATCH SELL"
        elif score >= 15:
            signal.direction = "SELL"
        else:
            signal.direction = "STRONG SELL"

        # if mtf >= 80:

        #     signal.reason.append(
        #         "✓ Multi TF Bullish"
        #     )


        # elif mtf <= 20:

        #     signal.reason.append(
        #         "✓ Multi TF Bearish"
        #     )

        signal.confidence = score
        signal.updated = True


signal_engine = SignalEngine()