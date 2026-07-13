from __future__ import annotations


class PriorityMarket:

    def __init__(self):

        self.symbols = []

    def update(
        self,
        coins,
        limit=30,
    ):

        self.symbols = [

            coin.symbol

            for coin in coins[:limit]

        ]

    def all(self):

        return self.symbols


priority_market = PriorityMarket()