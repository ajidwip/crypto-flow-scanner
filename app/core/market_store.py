from __future__ import annotations

from threading import RLock
from typing import Dict
from typing import Iterator

from app.models.coin import Coin


class MarketStore:
    """
    Runtime market storage.
    """

    def __init__(self) -> None:

        self._coins: Dict[str, Coin] = {}

        self._lock = RLock()

    def add(self, coin: Coin) -> None:

        with self._lock:

            self._coins[coin.symbol] = coin

    def remove(self, symbol: str) -> None:

        with self._lock:

            self._coins.pop(symbol, None)

    def exists(self, symbol: str) -> bool:

        return symbol in self._coins

    def get(self, symbol: str) -> Coin | None:

        return self._coins.get(symbol)

    def clear(self) -> None:

        with self._lock:

            self._coins.clear()

    def values(self):

        return self._coins.values()

    def keys(self):

        return self._coins.keys()

    def items(self):

        return self._coins.items()

    def all(self) -> list[Coin]:

        return list(self._coins.values())

    def total(self) -> int:

        return len(self._coins)

    def top_score(
        self,
        limit: int = 20
    ) -> list[Coin]:

        return sorted(

            self._coins.values(),

            key=lambda x: x.score.total,

            reverse=True

        )[:limit]

    def top_velocity(

        self,

        limit: int = 20

    ) -> list[Coin]:

        return sorted(

            self._coins.values(),

            key=lambda x: x.score.velocity,

            reverse=True

        )[:limit]

    def top_rotation(

        self,

        limit: int = 20

    ) -> list[Coin]:

        return sorted(

            self._coins.values(),

            key=lambda x: x.score.rotation,

            reverse=True

        )[:limit]

    def __len__(self):

        return len(self._coins)

    def __iter__(self) -> Iterator[Coin]:

        return iter(self._coins.values())