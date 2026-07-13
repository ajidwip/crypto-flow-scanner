from __future__ import annotations

from dataclasses import dataclass, field

from app.models.orderbook_score import OrderBookScore


@dataclass(slots=True)
class OrderBook:

    bids: list[tuple[float, float]] = field(default_factory=list)

    asks: list[tuple[float, float]] = field(default_factory=list)

    bid_volume: float = 0.0

    ask_volume: float = 0.0

    bid_notional: float = 0.0

    ask_notional: float = 0.0

    spread: float = 0.0

    imbalance: float = 0.0

    updated: bool = False

    score: OrderBookScore = field(
        default_factory=OrderBookScore
    )