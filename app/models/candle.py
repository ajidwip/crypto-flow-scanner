from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Optional

from app.models.base import BaseModel


@dataclass(slots=True)
class Candle(BaseModel):
    """
    Binance Kline Candle
    """

    symbol: str = ""

    interval: str = "5m"

    open_time: Optional[datetime] = None

    close_time: Optional[datetime] = None

    open: float = 0.0

    high: float = 0.0

    low: float = 0.0

    close: float = 0.0

    volume: float = 0.0

    quote_volume: float = 0.0

    trades: int = 0

    taker_buy_base_volume: float = 0.0

    taker_buy_quote_volume: float = 0.0

    is_closed: bool = False

    ignore: float = 0.0
    
    @property
    def body_size(self) -> float:
        return abs(self.close - self.open)

    @property
    def candle_range(self) -> float:
        return self.high - self.low

    @property
    def upper_wick(self) -> float:
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self) -> float:
        return min(self.open, self.close) - self.low

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    @property
    def hl2(self) -> float:
        return (self.high + self.low) / 2

    @property
    def hlc3(self) -> float:
        return (self.high + self.low + self.close) / 3

    @property
    def ohlc4(self) -> float:
        return (
            self.open +
            self.high +
            self.low +
            self.close
        ) / 4

    def copy(self) -> "Candle":
        return Candle(**self.to_dict())