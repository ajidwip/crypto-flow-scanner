from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class VolumeSpike:

    average_volume: float = 0.0

    current_volume: float = 0.0

    ratio: float = 0.0

    score: float = 0.0

    updated: bool = False