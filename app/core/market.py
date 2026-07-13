from __future__ import annotations

import logging

from app.models.coin import Coin

logger = logging.getLogger("FLOW")


class Market:

    def __init__(self):

        self.coins: dict[str, Coin] = {}

        self.selected = "BTCUSDT"

    def get_selected(self):

        return self.get(self.selected)

    def add(
        self,
        coin: Coin
    ):

        symbol = coin.symbol.upper()

        self.coins[symbol] = coin


    def get(
        self,
        symbol: str
    ) -> Coin | None:

        return self.coins.get(
            symbol.upper()
        )


    def remove(
        self,
        symbol: str
    ):

        self.coins.pop(
            symbol.upper(),
            None
        )


    def exists(
        self,
        symbol: str
    ) -> bool:

        return (
            symbol.upper()
            in self.coins
        )


    def all(self) -> list[Coin]:

        return list(
            self.coins.values()
        )


    def symbols(self) -> list[str]:

        return list(
            self.coins.keys()
        )


    def count(self) -> int:

        return len(
            self.coins
        )


    def clear(self):

        self.coins.clear()


    def summary(self):

        logger.info(
            "Market Loaded : %s coins",
            len(self.coins)
        )


market = Market()