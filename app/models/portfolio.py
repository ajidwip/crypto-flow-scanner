from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from app.models.paper_position import PaperPosition


@dataclass(slots=True)
class Portfolio:

    balance: float = 1000

    equity: float = 1000

    positions: list[PaperPosition] = field(default_factory=list)

    history: list[PaperPosition] = field(default_factory=list)

    trades: int = 0

    win: int = 0

    loss: int = 0

    profit: float = 0.0

    loss_amount: float = 0.0

    positions: list[PaperPosition] = field(
        default_factory=list
    )