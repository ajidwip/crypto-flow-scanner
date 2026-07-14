from __future__ import annotations

import asyncio

from app.core.statistics import statistics

from app.core.market import market

from app.services.ranking_service import ranking_service

from app.core.priority_market import priority_market

from app.core.paper_portfolio import portfolio


class SystemMonitor:

    async def start(self):

        while True:

            # print()

            # print("=" * 80)

            # print("Trades    :", statistics.trades)

            # print("Indicator :", statistics.indicator)

            # print("Score     :", statistics.score)

            # print("=" * 80)

            top = ranking_service.top(20)

            # print()

            # print("=" * 80)
            # print("TOP 20 FLOW")
            # print("=" * 80)

            for coin in top:

                signal = coin.score.signal

                # print(

                #     f"{coin.score.rank:>2}",

                #     f"{coin.symbol:<15}",

                #     f"{coin.score.total:>7.2f}",

                #     f"{signal:<8}",

                #     f"{coin.score.rank_change:+4}",

                # )

            coin = market.get_selected()

            if coin:

                # print()

                # print("SELECTED")

                # print(coin.symbol)

                # print("Trades :", coin.trade_cache.count)

                # print("Buy :", round(coin.trade_cache.buy_volume, 2))

                # print("Sell :", round(coin.trade_cache.sell_volume, 2))

                # print("Delta :", round(coin.trade_cache.delta, 2))

                # print("Notional :", round(coin.trade_cache.notional, 2))

                # print(
                #     "BUY Whale Count :",
                #     coin.whale_cache.buy_count,
                # )

                # print(
                #     "SELL Whale Count :",
                #     coin.whale_cache.sell_count,
                # )

                # print(
                #     "BUY Whale Value :",
                #     round(coin.whale_cache.buy_value, 2),
                # )

                # print(
                #     "SELL Whale Value :",
                #     round(coin.whale_cache.sell_value, 2),
                # )

                # print(
                #     "Largest Whale :",
                #     round(coin.whale_cache.largest, 2),
                # )

                # print(
                #     "Whale Pressure :",
                #     round(coin.whale_cache.pressure, 3),
                # )

                # print()

                # print("CVD :", round(coin.cvd.value, 2))

                # print("Delta :", round(coin.delta_volume.delta, 2))

                # print("Pressure :", round(coin.delta_volume.pressure, 3))

                # print()

                # print("Score :", coin.score.total)

                # print("Volume :", coin.score.volume)

                # print("Momentum :", coin.score.momentum)

                # print("Money Flow :", coin.score.money_flow)

                # print("Trend :", coin.score.trend)

                # print("Whale :", coin.score.whale)

                # print("Delta :", coin.score.delta)

                # print("CVD :", coin.score.cvd)

                # print()

                # print("ORDER BOOK")

                # print(
                #     "Bid Volume :",
                #     round(coin.order_book.bid_volume,2)
                # )

                # print(
                #     "Ask Volume :",
                #     round(coin.order_book.ask_volume,2)
                # )

                # print(
                #     "Bid Notional :",
                #     round(coin.order_book.bid_notional,2)
                # )

                # print(
                #     "Ask Notional :",
                #     round(coin.order_book.ask_notional,2)
                # )

                # print(
                #     "Spread :",
                #     coin.order_book.spread
                # )

                # print(
                #     "Imbalance :",
                #     round(
                #         coin.order_book.imbalance,
                #         3
                #     )
                # )

                # print()

                # print("ORDERBOOK SCORE")

                # print("Imbalance :", round(coin.order_book.score.imbalance, 2))

                # print("Wall :", round(coin.order_book.score.wall, 2))

                # print("Spread :", round(coin.order_book.score.spread, 2))

                # print("Liquidity :", round(coin.order_book.score.liquidity, 2))

                # print("Pressure :", round(coin.order_book.score.pressure, 2))

                # print("Total :", round(coin.order_book.score.total, 2))

                # print()

                # print("VOLUME PROFILE")

                # print("POC :", coin.volume_profile.poc)

                # print()

                # print("VOLUME PROFILE")

                # print("VAL :", coin.volume_profile.val)

                # print("POC :", coin.volume_profile.poc)

                # print("VAH :", coin.volume_profile.vah)

                # print(
                #     "Total Volume :",
                #     round(coin.volume_profile.total_volume, 2),
                # )

                # print()

                # print("VOLUME SPIKE")

                # print(
                #     "Average :",
                #     round(
                #         coin.volume_spike.average_volume,
                #         2,
                #     ),
                # )

                # print(
                #     "Current :",
                #     round(
                #         coin.volume_spike.current_volume,
                #         2,
                #     ),
                # )

                # print(
                #     "Ratio :",
                #     round(
                #         coin.volume_spike.ratio,
                #         2,
                #     ),
                # )

                # print(
                #     "Score :",
                #     round(
                #         coin.volume_spike.score,
                #         2,
                #     ),
                # )

                # print()

                # print("RVOL")

                # print("Average :", round(coin.rvol.average,2))

                # print("Current :", round(coin.rvol.current,2))

                # print("Ratio :", round(coin.rvol.ratio,2))

                # print("Score :", round(coin.rvol.score,2))

                # print()

                # if coin.open_interest.updated:

                #     print()

                #     print("OPEN INTEREST")

                #     print(
                #         "Value :",
                #         coin.open_interest.value
                #     )

                #     print(
                #         "Delta :",
                #         coin.open_interest.delta
                #     )

                #     print(
                #         "% :",
                #         coin.open_interest.percentage
                #     )

                #     print(
                #         "Score :",
                #         coin.open_interest.score
                #     )

                # print()

                # print("TOP PRIORITY")

                # for symbol in priority_market.all()[:10]:

                #     print(symbol)

                # print()

                # print("SIGNAL")

                # print(coin.symbol)

                # print("Direction :", coin.signal.direction)

                # print("Confidence :", round(

                #     coin.signal.confidence,

                #     2,

                # ))

                # print()

                # print("REASONS")

                # if coin.signal.reason:

                #     for reason in coin.signal.reason:

                #         print("✓", reason)

                # else:

                #     print("-")

                # print()

                # print("FUNDING")

                # print("Rate :", round(coin.funding_rate.rate, 4))

                # print("Score :", round(coin.funding_rate.score, 2))

                # print()

                # print("ENTRY")

                # print("Entry :", round(coin.entry.entry, 4))

                # print("Stop  :", round(coin.entry.stop, 4))

                # print("TP1   :", round(coin.entry.tp1, 4))

                # print("TP2   :", round(coin.entry.tp2, 4))

                # print("RR    :", round(coin.entry.rr, 2))

                # print()

                # print("REGIME")

                # print("Regime :", coin.market_regime.regime)

                # print("Score  :", round(coin.market_regime.score, 2))

                # print()
                                
                # print("POSITION")

                # print("Capital :", coin.position.capital)

                # print("Risk %  :", coin.position.risk_percent)

                # print("Leverage:", coin.position.leverage)

                # print("Risk $  :", round(coin.position.risk_amount, 2))

                # print("Size    :", round(coin.position.position_size, 4))

                # print("Margin  :", round(coin.position.margin, 2))

                # print("SL Loss :", round(coin.position.loss_if_sl, 2))

                # print("TP1     :", round(coin.position.profit_tp1, 2))

                # print("TP2     :", round(coin.position.profit_tp2, 2))

                print()
                print("=" * 80)
                print("OPEN POSITIONS")
                print("=" * 80)

                if not portfolio.positions:

                    print("No Open Position")

                else:

                    for p in portfolio.positions:

                        if p.status != "OPEN":
                            continue

                        print()

                        print(p.symbol)

                        print("Side   :", p.side)

                        print("Entry  :", round(p.entry, 8))

                        print("Stop   :", round(p.stop, 8))

                        print("TP     :", round(p.take_profit, 8))

                        print("Qty    :", round(p.quantity, 2))

                print()
                print("=" * 80)
                print("TRADE HISTORY")
                print("=" * 80)

                if not portfolio.history:

                    print("No Trade")

                else:

                    for trade in portfolio.history[-10:]:

                        print()

                        print(trade.symbol)

                        print("Result :", trade.status)

                        print("Entry :", trade.entry)

                        print("Stop :", trade.stop)

                        print("PnL    :", round(trade.pnl, 2))

                total = portfolio.win + portfolio.loss

                if total:

                    winrate = portfolio.win / total * 100

                else:

                    winrate = 0

                print()
                print("=" * 80)
                print("PORTFOLIO")
                print("=" * 80)

                print("Balance :", round(portfolio.balance, 2))
                print("Win     :", portfolio.win)
                print("Loss    :", portfolio.loss)
                print("Trades  :", total)
                print("WinRate :", round(winrate, 2), "%")

            await asyncio.sleep(5)


system_monitor = SystemMonitor()