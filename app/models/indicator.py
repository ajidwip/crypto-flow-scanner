from __future__ import annotations

from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass(slots=True)
class Indicator(BaseModel):
    """
    Indicator values for one symbol.
    """

    ema9: float = 0.0
    ema20: float = 0.0
    ema50: float = 0.0
    ema100: float = 0.0
    ema200: float = 0.0

    sma20: float = 0.0
    sma50: float = 0.0
    sma100: float = 0.0
    sma200: float = 0.0

    rsi14: float = 0.0

    atr14: float = 0.0

    macd: float = 0.0
    macd_signal: float = 0.0
    macd_histogram: float = 0.0

    volume_ma20: float = 0.0

    obv: float = 0.0

    vwap: float = 0.0

    mfi14: float = 0.0

    cmf20: float = 0.0

    adx14: float = 0.0

    plus_di14: float = 0.0
    minus_di14: float = 0.0

    bollinger_upper: float = 0.0
    bollinger_middle: float = 0.0
    bollinger_lower: float = 0.0

    stochastic_k: float = 0.0
    stochastic_d: float = 0.0

    roc12: float = 0.0

    cci20: float = 0.0

    williams_r14: float = 0.0

    momentum10: float = 0.0

    volatility: float = 0.0

    trend_strength: float = 0.0