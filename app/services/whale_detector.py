from __future__ import annotations

from app.models.trade import Trade
from app.models.whale_trade import WhaleTrade


class WhaleDetector:

    def __init__(self):

        self.level1 = 50_000

        self.level2 = 100_000

        self.level3 = 250_000

        self.level4 = 500_000

        self.level5 = 1_000_000

    def detect(
        self,
        trade: Trade,
    ) -> WhaleTrade | None:

        if trade.value < self.level1:
            return None

        side = "SELL" if trade.buyer_maker else "BUY"

        return WhaleTrade(

            symbol=trade.symbol,

            side=side,

            value=trade.value,

            price=trade.price,

            quantity=trade.quantity,

            trade_time=trade.trade_time,

        )


whale_detector = WhaleDetector()