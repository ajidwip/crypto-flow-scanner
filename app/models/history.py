from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from dataclasses import field

from app.models.base import BaseModel


@dataclass(slots=True)
class History(BaseModel):
    """
    Rolling history buffer.
    """

    max_size: int = 500

    score: deque = field(default_factory=lambda: deque(maxlen=500))

    money_flow: deque = field(default_factory=lambda: deque(maxlen=500))

    momentum: deque = field(default_factory=lambda: deque(maxlen=500))

    trend: deque = field(default_factory=lambda: deque(maxlen=500))

    volume: deque = field(default_factory=lambda: deque(maxlen=500))

    velocity: deque = field(default_factory=lambda: deque(maxlen=500))

    acceleration: deque = field(default_factory=lambda: deque(maxlen=500))

    health: deque = field(default_factory=lambda: deque(maxlen=500))

    rotation: deque = field(default_factory=lambda: deque(maxlen=500))

    close_price: deque = field(default_factory=lambda: deque(maxlen=500))

    close_volume: deque = field(default_factory=lambda: deque(maxlen=500))

    open_interest: deque = field(default_factory=lambda: deque(maxlen=500))

    funding_rate: deque = field(default_factory=lambda: deque(maxlen=500))

    def add_score(self, value: float) -> None:
        self.score.append(value)

    def add_money_flow(self, value: float) -> None:
        self.money_flow.append(value)

    def add_momentum(self, value: float) -> None:
        self.momentum.append(value)

    def add_trend(self, value: float) -> None:
        self.trend.append(value)

    def add_volume(self, value: float) -> None:
        self.volume.append(value)

    def add_velocity(self, value: float) -> None:
        self.velocity.append(value)

    def add_acceleration(self, value: float) -> None:
        self.acceleration.append(value)

    def add_health(self, value: float) -> None:
        self.health.append(value)

    def add_rotation(self, value: float) -> None:
        self.rotation.append(value)

    def add_price(self, value: float) -> None:
        self.close_price.append(value)

    def add_volume_data(self, value: float) -> None:
        self.close_volume.append(value)

    def add_open_interest(self, value: float) -> None:
        self.open_interest.append(value)

    def add_funding_rate(self, value: float) -> None:
        self.funding_rate.append(value)

    def clear(self) -> None:
        self.score.clear()
        self.money_flow.clear()
        self.momentum.clear()
        self.trend.clear()
        self.volume.clear()
        self.velocity.clear()
        self.acceleration.clear()
        self.health.clear()
        self.rotation.clear()
        self.close_price.clear()
        self.close_volume.clear()
        self.open_interest.clear()
        self.funding_rate.clear()