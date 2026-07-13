from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TimeframeTrend:

    m5: float = 50

    m15: float = 50

    h1: float = 50

    h4: float = 50

    total: float = 50

    updated: bool = False