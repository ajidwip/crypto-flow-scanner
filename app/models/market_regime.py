from dataclasses import dataclass


@dataclass(slots=True)
class MarketRegime:

    regime: str = "UNKNOWN"

    score: float = 0

    updated: bool = False