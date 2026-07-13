from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Signal:

    direction: str = "NEUTRAL"

    confidence: float = 0.0

    reason: list[str] = field(default_factory=list)

    updated: bool = False