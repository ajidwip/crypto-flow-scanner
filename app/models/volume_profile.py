from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class VolumeProfile:

    poc: float = 0.0

    vah: float = 0.0

    val: float = 0.0

    hvn: list[float] = field(default_factory=list)

    lvn: list[float] = field(default_factory=list)

    total_volume: float = 0.0

    updated: bool = False