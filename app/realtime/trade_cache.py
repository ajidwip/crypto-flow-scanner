from __future__ import annotations

from collections import deque

from app.models.trade import Trade


class TradeCache:

    def __init__(self):

        self.trades = deque(maxlen=500)

        self._buy_volume = 0.0

        self._sell_volume = 0.0

        self._notional = 0.0

    def add(
        self,
        trade: Trade,
    ):

        if len(self.trades) == self.trades.maxlen:

            old = self.trades[0]

            if old.buyer_maker:

                self._sell_volume -= old.quantity

            else:

                self._buy_volume -= old.quantity

            self._notional -= old.value

        self.trades.append(trade)

        if trade.buyer_maker:

            self._sell_volume += trade.quantity

        else:

            self._buy_volume += trade.quantity

        self._notional += trade.value

    @property
    def count(self):

        return len(self.trades)

    @property
    def buy_volume(self):

        return self._buy_volume

    @property
    def sell_volume(self):

        return self._sell_volume

    @property
    def delta(self):

        return self._buy_volume - self._sell_volume

    @property
    def notional(self):

        return self._notional

    def clear(self):

        self.trades.clear()

        self._buy_volume = 0.0

        self._sell_volume = 0.0

        self._notional = 0.0