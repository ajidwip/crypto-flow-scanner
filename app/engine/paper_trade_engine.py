from __future__ import annotations

from app.core.paper_portfolio import portfolio
from app.models.paper_position import PaperPosition

MAX_OPEN_POSITION = 3

class PaperTradeEngine:

    def calculate(
        self,
        coin,
    ):

        signal = coin.signal

        if signal.direction not in (
            "WATCH BUY",
            "BUY",
            "STRONG BUY",
        ):
            return

        open_positions = sum(
            1
            for p in portfolio.positions
            if p.status == "OPEN"
        )

        if open_positions >= MAX_OPEN_POSITION:
            return

        for p in portfolio.positions:

            if (
                p.symbol == coin.symbol
                and
                p.status == "OPEN"
            ):
                return

        position = PaperPosition()

        position.symbol = coin.symbol

        position.side = "LONG"

        position.entry = coin.entry.entry

        position.stop = coin.entry.stop

        position.tp1 = coin.entry.tp1

        position.tp2 = coin.entry.tp2

        position.quantity = coin.position.position_size

        position.remaining_qty = position.quantity

        position.open()

        portfolio.positions.append(position)

        portfolio.trades += 1


paper_trade_engine = PaperTradeEngine()