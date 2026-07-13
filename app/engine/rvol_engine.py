from __future__ import annotations


class RVOL_Engine:

    def calculate(
        self,
        coin,
    ):

        candles = list(coin.candles)

        if len(candles) < 30:
            return

        current = candles[-1].volume

        average = sum(

            c.volume

            for c in candles[-21:-1]

        ) / 20

        if average == 0:
            return

        ratio = current / average

        if ratio >= 5:
            score = 100

        elif ratio >= 4:
            score = 90

        elif ratio >= 3:
            score = 80

        elif ratio >= 2:
            score = 60

        elif ratio >= 1.5:
            score = 40

        elif ratio >= 1:
            score = 20

        else:

            score = ratio * 20

        rvol = coin.rvol

        rvol.current = current

        rvol.average = average

        rvol.ratio = ratio

        rvol.score = score

        rvol.updated = True


rvol_engine = RVOL_Engine()