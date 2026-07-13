from dataclasses import dataclass


@dataclass(slots=True)
class FundingRate:

    rate: float = 0.0

    score: float = 50.0

    updated: bool = False