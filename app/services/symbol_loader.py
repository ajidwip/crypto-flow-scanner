from __future__ import annotations

import logging

from app.models.coin import Coin
from app.network.rest_client import rest
from app.core.market import market


logger = logging.getLogger("FLOW")


class SymbolLoader:


    async def load(self):

        logger.info(
            "Loading Binance Futures Symbols..."
        )


        data = await rest.exchange_info()


        symbols = data.get(
            "symbols",
            []
        )


        total = 0


        for item in symbols:


            if item.get("contractType") != "PERPETUAL":
                continue


            if item.get("quoteAsset") != "USDT":
                continue


            if item.get("status") != "TRADING":
                continue



            symbol = item["symbol"]


            if not symbol.isascii():
                logger.warning(
                    "Skip invalid symbol: %s",
                    symbol,
                )
                continue

            price_precision = item.get(
                "pricePrecision",
                0
            )


            quantity_precision = item.get(
                "quantityPrecision",
                0
            )


            tick_size = 0.0

            step_size = 0.0



            for f in item.get("filters", []):

                if f["filterType"] == "PRICE_FILTER":

                    tick_size = float(
                        f["tickSize"]
                    )


                elif f["filterType"] == "LOT_SIZE":

                    step_size = float(
                        f["stepSize"]
                    )



            coin = Coin(

                symbol=symbol,

                base_asset=item.get(
                    "baseAsset",
                    ""
                ),

                quote_asset=item.get(
                    "quoteAsset",
                    ""
                ),

                status=item.get(
                    "status",
                    ""
                ),

                price_precision=price_precision,

                quantity_precision=quantity_precision,

                tick_size=tick_size,

                step_size=step_size,

            )


            market.add(
                coin
            )


            total += 1



        logger.info(
            "Loaded %s symbols",
            total
        )


        market.summary()



        return market.all()

    def symbols(self):

        return list(market.symbols())


symbol_loader = SymbolLoader()