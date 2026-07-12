from __future__ import annotations

from datetime import datetime
from datetime import timezone

from app.models.candle import Candle


class TradeBuilder:

    def __init__(self):

        self.current: Candle | None = None

        self.bucket: int | None = None

    def update(
        self,
        price: float,
        quantity: float,
        trade_time: int,
    ) -> Candle | None:

        # abaikan data tidak valid
        if price <= 0 or quantity <= 0:
            return None

        bucket = trade_time // 300000

        if self.current is None:

            self.bucket = bucket

            open_time = datetime.fromtimestamp(
                bucket * 300,
                tz=timezone.utc,
            )

            self.current = Candle(
                open_time=open_time,
                interval="5m",
                open=price,
                high=price,
                low=price,
                close=price,
                volume=quantity,
                is_closed=False,
            )

            return None

        # ==========================
        # Candle baru
        # ==========================

        if bucket != self.bucket:

            finished = self.current

            finished.is_closed = True

            self.bucket = bucket

            open_time = datetime.fromtimestamp(
                bucket * 300,
                tz=timezone.utc,
            )

            self.current = Candle(
                open_time=open_time,
                interval="5m",
                open=price,
                high=price,
                low=price,
                close=price,
                volume=quantity,
                is_closed=False,
            )

            return finished

        # ==========================
        # Update candle berjalan
        # ==========================

        self.current.high = max(
            self.current.high,
            price,
        )

        self.current.low = min(
            self.current.low,
            price,
        )

        self.current.close = price

        self.current.volume += quantity

        return None