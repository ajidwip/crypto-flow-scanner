from __future__ import annotations

from app.core.paper_portfolio import portfolio


class PaperPositionMonitor:

    def update(self, coin):

        current = coin.last_candle

        if current is None:
            return

        high = current.high
        low = current.low
        close = current.close

        for position in portfolio.positions:

            if position.status != "OPEN":
                continue

            if position.symbol != coin.symbol:
                continue

            #
            # STOP LOSS
            #
            if low <= position.stop:

                position.status = "STOP"

                position.close_price = low

                position.close_time = current.close_time

                loss = (
                    low
                    -
                    position.entry
                ) * position.quantity

                position.realized_pnl += loss

                position.pnl = position.realized_pnl

                portfolio.balance += loss

                portfolio.loss += 1

                portfolio.history.append(position)

                portfolio.loss_amount += abs(position.pnl)

                print()

                print("[STOP LOSS]", position.symbol)

                print("PnL :", round(position.pnl, 2))

                continue

            #
            # TP
            #
            if high >= position.take_profit:

                position.status = "TP"

                position.close_price = high

                position.close_time = current.close_time

                profit = (
                    position.take_profit
                    -
                    position.entry
                ) * position.quantity

                portfolio.balance += profit

                position.realized_pnl += profit

                position.pnl = position.realized_pnl

                portfolio.win += 1

                portfolio.history.append(position)

                portfolio.profit += position.pnl

                print()

                print("[TAKE PROFIT]", position.symbol)

                print("PnL :", round(position.pnl, 2))


paper_position_monitor = PaperPositionMonitor()