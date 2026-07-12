from __future__ import annotations

import asyncio
import inspect
import logging
from collections import defaultdict
from typing import Any
from typing import Awaitable
from typing import Callable


logger = logging.getLogger("FLOW")


class EventBus:
    """
    Async Event Bus
    """

    def __init__(self) -> None:

        self._subscribers: dict[
            str,
            list[Callable[..., Any]]
        ] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        callback: Callable[..., Any]
    ) -> None:

        if callback not in self._subscribers[event_name]:

            self._subscribers[event_name].append(callback)

            logger.info(
                "Subscribe %s -> %s",
                event_name,
                callback.__name__
            )

    def unsubscribe(
        self,
        event_name: str,
        callback: Callable[..., Any]
    ) -> None:

        if callback in self._subscribers[event_name]:

            self._subscribers[event_name].remove(callback)

    async def publish(
        self,
        event_name: str,
        data: Any = None
    ) -> None:

        callbacks = self._subscribers.get(event_name, [])

        if not callbacks:

            return

        for callback in callbacks:

            try:

                result = callback(data)

                if inspect.isawaitable(result):

                    await result

            except Exception:

                logger.exception(
                    "Event Error : %s",
                    event_name
                )

    def clear(self) -> None:

        self._subscribers.clear()

    def count(self) -> int:

        return sum(

            len(v)

            for v in self._subscribers.values()

        )

    def events(self) -> list[str]:

        return list(self._subscribers.keys())