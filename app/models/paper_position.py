from __future__ import annotations

from dataclasses import dataclass
from time import time


@dataclass(slots=True)
class PaperPosition:

    symbol: str = ""

    side: str = ""

    status: str = "OPEN"

    entry: float = 0.0

    stop: float = 0.0

    tp1: float = 0.0

    tp2: float = 0.0

    quantity: float = 0.0

    open_time: float = 0.0

    close_time: float = 0.0

    close_price: float = 0.0

    pnl: float = 0.0

    hit_tp1: bool = False

    hit_tp2: bool = False

    remaining_qty: float = 0.0

    realized_pnl: float = 0.0

    moved_to_be: bool = False

    def open(self):

        self.open_time = time()