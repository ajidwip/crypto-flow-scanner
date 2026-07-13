from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OrderBookScore:

    imbalance: float = 0.0

    wall: float = 0.0

    spread: float = 0.0

    liquidity: float = 0.0

    pressure: float = 0.0

    total: float = 0.0