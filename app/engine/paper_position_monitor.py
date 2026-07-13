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

                position.remaining_qty = 0

                position.close_price = low

                position.close_time = current.close_time

                loss = (
                    low
                    -
                    position.entry
                ) * position.remaining_qty

                position.realized_pnl += loss

                position.pnl = position.realized_pnl

                portfolio.balance += loss

                position.remaining_qty = 0

                portfolio.loss += 1

                portfolio.history.append(position)

                portfolio.loss_amount += abs(position.pnl)

                print()

                print("[STOP LOSS]", position.symbol)

                print("PnL :", round(position.pnl, 2))

                continue

            #
            # TP1
            #

            if (
                not position.hit_tp1
                and
                high >= position.tp1
            ):

                position.hit_tp1 = True

                close_qty = position.remaining_qty * 0.50

                profit = (
                    position.tp1
                    -
                    position.entry
                ) * close_qty

                portfolio.balance += profit

                position.realized_pnl += profit

                position.remaining_qty -= close_qty

                #
                # Break Even
                #

                position.stop = position.entry

                position.moved_to_be = True

                print()

                print("[TP1]", position.symbol)

                print("Profit :", round(profit,2))

            #
            # TP2
            #
            if high >= position.tp2:

                position.status = "TP"

                position.remaining_qty = 0

                position.close_price = high

                position.close_time = current.close_time

                profit = (
                    position.tp2
                    -
                    position.entry
                ) * position.remaining_qty

                portfolio.balance += profit

                position.realized_pnl += profit

                position.pnl = position.realized_pnl

                position.remaining_qty = 0

                portfolio.win += 1

                portfolio.history.append(position)

                portfolio.profit += position.pnl

                print()

                print("[TAKE PROFIT]", position.symbol)

                print("PnL :", round(position.pnl, 2))


paper_position_monitor = PaperPositionMonitor()