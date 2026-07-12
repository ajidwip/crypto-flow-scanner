from __future__ import annotations

from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass(slots=True)
class Trade(BaseModel):

    symbol: str = ""

    price: float = 0.0

    quantity: float = 0.0

    value: float = 0.0

    buyer_maker: bool = False

    trade_time: int = 0