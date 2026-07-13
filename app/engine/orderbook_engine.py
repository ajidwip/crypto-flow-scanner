from __future__ import annotations


class OrderBookEngine:

    def calculate(self, coin):

        book = coin.order_book

        if not book.updated:
            return

        score = book.score

        score.imbalance = self.imbalance_score(book)

        score.wall = self.wall_score(book)

        score.spread = self.spread_score(book)

        score.liquidity = self.liquidity_score(book)

        score.pressure = self.pressure_score(book)

        score.total = (

            score.imbalance * 0.35 +

            score.wall * 0.20 +

            score.spread * 0.10 +

            score.liquidity * 0.15 +

            score.pressure * 0.20

        )

    def imbalance_score(self, book):

        return (

            (book.imbalance + 1)

            *

            50

        )

    def spread_score(self, book):

        if book.spread <= 0:

            return 100

        if book.spread < 0.05:

            return 100

        if book.spread < 0.10:

            return 80

        if book.spread < 0.20:

            return 60

        return 20

    def liquidity_score(self, book):

        total = (

            book.bid_notional

            +

            book.ask_notional

        )

        if total > 10_000_000:

            return 100

        if total > 5_000_000:

            return 80

        if total > 1_000_000:

            return 60

        if total > 500_000:

            return 40

        return 20

    def pressure_score(self, book):

        buy = book.bid_notional

        sell = book.ask_notional

        total = buy + sell

        if total == 0:

            return 50

        pressure = (

            buy

            -

            sell

        ) / total

        return (

            pressure + 1

        ) * 50

    def wall_score(self, book):

        bid_wall = max(

            (

                qty

                for _, qty in book.bids

            ),

            default=0

        )

        ask_wall = max(

            (

                qty

                for _, qty in book.asks

            ),

            default=0

        )

        if bid_wall + ask_wall == 0:

            return 50

        return (

            bid_wall

            /

            (bid_wall + ask_wall)

        ) * 100
        
orderbook_engine = OrderBookEngine()