from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TimeframeTrend:

    tf: str = ""

    trend: float = 0.0

    ema_fast: float = 0.0

    ema_slow: float = 0.0

    momentum: float = 0.0

    score: float = 0.0

    bullish: bool = False

    bearish: bool = False

    updated: bool = False



@dataclass(slots=True)
class MultiTimeframe:

    tf_5m: TimeframeTrend = field(
        default_factory=lambda: TimeframeTrend("5m")
    )

    tf_15m: TimeframeTrend = field(
        default_factory=lambda: TimeframeTrend("15m")
    )

    tf_1h: TimeframeTrend = field(
        default_factory=lambda: TimeframeTrend("1h")
    )

    tf_4h: TimeframeTrend = field(
        default_factory=lambda: TimeframeTrend("4h")
    )


    score: float = 0.0

    updated: bool = False