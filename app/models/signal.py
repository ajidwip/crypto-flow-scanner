from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Signal:

    direction: str = "NONE"

    confidence: float = 0

    strength: float = 0

    reason: list[str] = None

    updated: bool = False

    def __post_init__(self):

        if self.reason is None:

            self.reason = []