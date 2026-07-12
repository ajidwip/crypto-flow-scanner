from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Statistics:

    trades: int = 0

    candles: int = 0

    indicator: int = 0

    score: int = 0


statistics = Statistics()