from __future__ import annotations

from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass(slots=True)
class Score(BaseModel):
    """
    Scanner score model.
    """

    total: float = 0.0

    confidence: float = 0.0

    money_flow: float = 0.0

    delta: float = 0.0

    whale: float = 0.0

    momentum: float = 0.0

    trend: float = 0.0

    volume: float = 0.0

    volatility: float = 0.0

    breakout: float = 0.0

    open_interest: float = 0.0

    funding: float = 0.0

    liquidity: float = 0.0

    velocity: float = 0.0

    acceleration: float = 0.0

    stability: float = 0.0

    health: float = 0.0

    rotation: float = 0.0

    rank: int = 0

    last_rank: int = 0

    rank_change: int = 0

    signal: str = "NEUTRAL"

    reason: str = ""

    updated: bool = False

    def reset(self) -> None:
        self.total = 0.0
        self.confidence = 0.0
        self.money_flow = 0.0
        self.delta = 0.0
        self.whale = 0.0
        self.momentum = 0.0
        self.trend = 0.0
        self.volume = 0.0
        self.volatility = 0.0
        self.breakout = 0.0
        self.open_interest = 0.0
        self.funding = 0.0
        self.liquidity = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0
        self.stability = 0.0
        self.health = 0.0
        self.rotation = 0.0
        self.rank = 0
        self.last_rank = 0
        self.rank_change = 0
        self.signal = "NEUTRAL"
        self.reason = ""
        self.updated = False