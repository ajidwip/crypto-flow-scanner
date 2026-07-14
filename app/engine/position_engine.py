from __future__ import annotations


class PositionEngine:

    def calculate(
        self,
        coin,
    ):

        entry = coin.entry
        position = coin.position

        if entry.entry <= 0:
            return

        capital = position.capital
        risk_percent = position.risk_percent

        risk_amount = capital * risk_percent / 100

        stop_distance = abs(
            entry.entry - entry.stop
        )

        if stop_distance <= 0:
            return

        qty = risk_amount / stop_distance

        margin = (
            qty * entry.entry
        ) / position.leverage

        position.risk_amount = risk_amount

        position.position_size = qty

        position.margin = margin

        position.loss_if_sl = risk_amount

        position.profit_tp = (
            abs(entry.take_profit - entry.entry)
            * qty
        )

        position.updated = True


position_engine = PositionEngine()