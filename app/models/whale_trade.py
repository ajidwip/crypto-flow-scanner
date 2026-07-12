from __future__ import annotations

from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass(slots=True)
class WhaleTrade(BaseModel):

    symbol: str = ""

    side: str = ""

    value: float = 0.0

    price: float = 0.0

    quantity: float = 0.0

    trade_time: int = 0