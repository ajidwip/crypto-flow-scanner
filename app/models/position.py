from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Position:

    capital: float = 1000.0

    risk_percent: float = 1.0

    leverage: int = 5

    risk_amount: float = 0.0

    position_size: float = 0.0

    margin: float = 0.0

    loss_if_sl: float = 0.0

    profit_tp: float = 0.0

    updated: bool = False