from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RVOL:

    current: float = 0

    average: float = 0

    ratio: float = 0

    score: float = 0

    updated: bool = False