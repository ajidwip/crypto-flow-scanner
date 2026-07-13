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

        risk = current.close - support

        if risk <= 0:
            return

        reward = risk * 2

        entry = coin.entry

        entry.entry = current.close

        entry.stop = support

        entry.tp1 = current.close + reward

        entry.tp2 = current.close + reward * 1.5

        entry.rr = reward / risk

        entry.updated = True


entry_engine = EntryEngine()