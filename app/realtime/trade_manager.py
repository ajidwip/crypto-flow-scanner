from __future__ import annotations

from app.realtime.trade_builder import TradeBuilder


class TradeManager:

    def __init__(self):

        self.builders = {}

    def builder(
        self,
        symbol: str,
    ) -> TradeBuilder:

        if symbol not in self.builders:

            self.builders[symbol] = TradeBuilder()

        return self.builders[symbol]


trade_manager = TradeManager()