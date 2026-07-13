from __future__ import annotations

from app.core.market import market


class OrderBookStreamService:

    async def handle(
        self,
        payload: dict,
    ):

        data = payload.get("data")

        if not data:
            return

        symbol = data["s"]

        coin = market.get(symbol)

        if coin is None:
            return

        bids = data["b"]

        asks = data["a"]

        book = coin.order_book

        book.bids.clear()
        book.asks.clear()

        bid_volume = 0.0
        ask_volume = 0.0

        bid_notional = 0.0
        ask_notional = 0.0

        for price, qty in bids:

            p = float(price)
            q = float(qty)

            book.bids.append((p, q))

            bid_volume += q
            bid_notional += p * q

        for price, qty in asks:

            p = float(price)
            q = float(qty)

            book.asks.append((p, q))

            ask_volume += q
            ask_notional += p * q

        book.bid_volume = bid_volume
        book.ask_volume = ask_volume

        book.bid_notional = bid_notional
        book.ask_notional = ask_notional

        if bids and asks:

            bid = float(bids[0][0])
            ask = float(asks[0][0])

            book.spread = ask - bid

        total = bid_volume + ask_volume

        if total:

            book.imbalance = (
                (bid_volume - ask_volume)
                /
                total
            )

        else:

            book.imbalance = 0

        book.updated = True


orderbook_stream_service = OrderBookStreamService()