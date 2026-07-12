from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.models.base import BaseModel


@dataclass(slots=True)
class State(BaseModel):
    """
    Runtime state for one symbol.
    """

    initialized: bool = False

    websocket_connected: bool = False

    collecting: bool = False

    analyzing: bool = False

    scoring: bool = False

    ranking: bool = False

    trading: bool = False

    last_price: float = 0.0

    last_volume: float = 0.0

    last_close_time: Optional[datetime] = None

    last_score_time: Optional[datetime] = None

    last_update_time: Optional[datetime] = None

    last_open_interest_time: Optional[datetime] = None

    last_funding_time: Optional[datetime] = None

    candle_count: int = 0

    reconnect_count: int = 0

    error_count: int = 0

    warning_count: int = 0

    is_hot: bool = False

    is_breakout: bool = False

    is_new_listing: bool = False

    is_active: bool = True