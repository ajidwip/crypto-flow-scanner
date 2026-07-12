from __future__ import annotations

from collections import deque

from app.models.whale_trade import WhaleTrade


class WhaleCache:

    def __init__(self):

        self.trades = deque(maxlen=200)

        self.buy_count = 0

        self.sell_count = 0

        self.buy_value = 0.0

        self.sell_value = 0.0

        self.largest = 0.0

    def add(
        self,
        trade: WhaleTrade,
    ):

        if len(self.trades) == self.trades.maxlen:

            old = self.trades[0]

            if old.side == "BUY":

                self.buy_count -= 1
                self.buy_value -= old.value

            else:

                self.sell_count -= 1
                self.sell_value -= old.value

        self.trades.append(trade)

        if trade.side == "BUY":

            self.buy_count += 1
            self.buy_value += trade.value

        else:

            self.sell_count += 1
            self.sell_value += trade.value

        if trade.value > self.largest:

            self.largest = trade.value

    @property
    def count(self):

        return len(self.trades)

    @property
    def delta(self):

        return self.buy_value - self.sell_value

    @property
    def total(self):

        return self.buy_value + self.sell_value

    @property
    def pressure(self):

        if self.total == 0:

            return 0.0

        return self.delta / self.total