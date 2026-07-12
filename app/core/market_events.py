from __future__ import annotations

from collections import deque


class MarketEvents:

    def __init__(self):

        self.updated = deque()

        self.pending = set()

    def push(self, symbol: str):

        if symbol in self.pending:
            return

        self.pending.add(symbol)

        self.updated.append(symbol)

    def pop(self):

        if not self.updated:
            return None

        symbol = self.updated.popleft()

        self.pending.remove(symbol)

        return symbol


market_events = MarketEvents()