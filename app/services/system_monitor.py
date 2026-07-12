from __future__ import annotations

import asyncio

from app.core.statistics import statistics

from app.core.market import market


class SystemMonitor:

    async def start(self):

        while True:

            print()

            print("=" * 80)

            print("Trades    :", statistics.trades)

            print("Indicator :", statistics.indicator)

            print("Score     :", statistics.score)

            print("=" * 80)

            coin = market.get("BTCUSDT")

            if coin:

                print()

                print("BTC Trade Cache")

                print("Trades :", coin.trade_cache.count)

                print("Buy :", round(coin.trade_cache.buy_volume, 2))

                print("Sell :", round(coin.trade_cache.sell_volume, 2))

                print("Delta :", round(coin.trade_cache.delta, 2))

                print("Notional :", round(coin.trade_cache.notional, 2))

                print(
                    "Whale :",
                    coin.whale_cache.count,
                )

                print(
                    "BUY Whale :",
                    coin.whale_cache.buy,
                )

                print(
                    "SELL Whale :",
                    coin.whale_cache.sell,
                )

            await asyncio.sleep(5)


system_monitor = SystemMonitor()