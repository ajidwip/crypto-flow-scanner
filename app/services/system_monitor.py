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
                    "BUY Whale Count :",
                    coin.whale_cache.buy_count,
                )

                print(
                    "SELL Whale Count :",
                    coin.whale_cache.sell_count,
                )

                print(
                    "BUY Whale Value :",
                    round(coin.whale_cache.buy_value, 2),
                )

                print(
                    "SELL Whale Value :",
                    round(coin.whale_cache.sell_value, 2),
                )

                print(
                    "Largest Whale :",
                    round(coin.whale_cache.largest, 2),
                )

                print(
                    "Whale Pressure :",
                    round(coin.whale_cache.pressure, 3),
                )

                print()

                print("CVD :", round(coin.cvd.value, 2))

                print("Delta :", round(coin.delta_volume.delta, 2))

                print("Pressure :", round(coin.delta_volume.pressure, 3))

                print()

                print("Score :", coin.score.total)

                print("Volume :", coin.score.volume)

                print("Momentum :", coin.score.momentum)

                print("Money Flow :", coin.score.money_flow)

                print("Trend :", coin.score.trend)

                print("Whale :", coin.score.whale)

                print("Delta :", coin.score.delta)

                print("CVD :", coin.score.cvd)

            await asyncio.sleep(5)


system_monitor = SystemMonitor()