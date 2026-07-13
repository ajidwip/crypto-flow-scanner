from __future__ import annotations


class OpenInterestEngine:

    def calculate(
        self,
        coin,
    ):

        oi = coin.open_interest

        change = oi.percent

        if change >= 5:

            score = 100

        elif change >= 3:

            score = 80

        elif change >= 2:

            score = 60

        elif change >= 1:

            score = 40

        elif change > 0:

            score = 20

        elif change <= -5:

            score = 0

        else:

            score = 10

        oi.score = score


open_interest_engine = OpenInterestEngine()