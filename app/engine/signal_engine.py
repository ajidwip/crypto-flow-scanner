from __future__ import annotations


class SignalEngine:

    def calculate(
        self,
        coin,
    ):

        score = coin.score.total

        signal = coin.signal

        signal.reason.clear()

        confidence = score

        trend = coin.score.trend
        whale = coin.score.whale
        delta = coin.score.delta
        cvd = coin.score.cvd
        momentum = coin.score.momentum
        orderbook = coin.order_book_score.total
        breakout = coin.score.breakout

        # ==========================
        # BUY CONFIRMATION
        # ==========================

        if trend >= 70:

            confidence += 3
            signal.reason.append("Up Trend")

        if momentum >= 60:

            confidence += 3
            signal.reason.append("Momentum")

        if whale >= 60:

            confidence += 4
            signal.reason.append("Whale Buy")

        if delta >= 60:

            confidence += 4
            signal.reason.append("Positive Delta")

        if cvd >= 60:

            confidence += 4
            signal.reason.append("Positive CVD")

        if orderbook >= 60:

            confidence += 4
            signal.reason.append("Bid Pressure")

        if breakout >= 70:

            confidence += 6
            signal.reason.append("Breakout")

        # ==========================
        # SELL CONFIRMATION
        # ==========================

        if trend <= 30:

            confidence -= 3
            signal.reason.append("Down Trend")

        if whale <= 40:

            confidence -= 4
            signal.reason.append("Whale Sell")

        if delta <= 40:

            confidence -= 4
            signal.reason.append("Negative Delta")

        if cvd <= 40:

            confidence -= 4
            signal.reason.append("Negative CVD")

        if orderbook <= 40:

            confidence -= 4
            signal.reason.append("Ask Pressure")

        if breakout <= 30:

            confidence -= 6
            signal.reason.append("Near Support")

        confidence = max(
            0,
            min(
                confidence,
                100,
            ),
        )

        signal.confidence = round(
            confidence,
            2,
        )

        # ==========================================
        # FINAL SIGNAL
        # ==========================================

        if confidence >= 90:

            signal.direction = "STRONG BUY"

        elif confidence >= 80:

            signal.direction = "BUY"

        elif confidence >= 65:

            signal.direction = "WATCH BUY"

        elif confidence >= 45:

            signal.direction = "NEUTRAL"

        elif confidence >= 30:

            signal.direction = "WATCH SELL"

        elif confidence >= 15:

            signal.direction = "SELL"

        else:

            signal.direction = "STRONG SELL"

        signal.updated = True


signal_engine = SignalEngine()