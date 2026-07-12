from __future__ import annotations

from app.core import market


def build_stream_groups(
    interval: str = "5m",
    batch_size: int = 150,
) -> list[str]:

    streams = [
        f"{coin.symbol.lower()}@kline_{interval}"
        #for coin in market
    ]

    groups = []

    for i in range(0, len(streams), batch_size):

        chunk = streams[i:i + batch_size]

        groups.append("/".join(chunk))

    return groups