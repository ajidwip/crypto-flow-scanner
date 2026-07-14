from __future__ import annotations


class EntryEngine:

    def calculate(
        self,
        coin,
    ):

        candles = list(coin.candles)

        if len(candles) < 30:
            return

        current = candles[-1]

        lows = [

            c.low

            for c in candles[-10:]

        ]

        highs = [

            c.high

            for c in candles[-10:]

        ]

        support = min(lows)

        resistance = max(highs)

        entry = coin.entry

        entry.entry = current.close

        entry.stop = support

        risk = abs(
            entry.entry
            -
            entry.stop
        )

        if risk <= 0:
            return

        entry.rr = 2.0

        entry.take_profit = (
            entry.entry
            +
            risk * entry.rr
        )

        entry.updated = True


entry_engine = EntryEngine()