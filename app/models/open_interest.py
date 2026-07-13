from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OpenInterest:

    value: float = 0.0

    previous: float = 0.0

    delta: float = 0.0

    percentage: float = 0.0

    score: float = 10.0

    updated: bool = False