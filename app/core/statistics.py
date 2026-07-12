from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Statistics:

    trades = 0

    candles = 0

    indicator = 0

    score = 0


statistics = Statistics()