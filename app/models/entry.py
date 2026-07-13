from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Entry:

    entry: float = 0.0

    stop: float = 0.0

    tp1: float = 0.0

    tp2: float = 0.0

    rr: float = 0.0

    updated: bool = False