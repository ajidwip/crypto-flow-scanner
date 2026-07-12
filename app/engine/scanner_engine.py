from __future__ import annotations

import asyncio
import logging

from app.core.market import market
from app.engine.flow_engine import flow_engine
from app.engine.indicator_engine import indicator_engine
from app.services.ranking_service import ranking_service
from app.core.market_events import market_events


logger = logging.getLogger("FLOW")


class ScannerEngine:

    def __init__(self):

        self.running = False

    async def start(self):

        self.running = True

        logger.info("Scanner Engine Started")

        while self.running:

            self.scan()

            await asyncio.sleep(1)

    def stop(self):

        self.running = False

    def scan(self):

        while True:

            symbol = market_events.pop()

            if symbol is None:

                break

            coin = market.get(symbol)

            if coin is None:

                continue

            if coin.live_candle is None:

                continue

            if coin.candle_count < 200:

                continue

            indicator_engine.calculate(coin)

            statistics.indicator += 1

            flow_engine.calculate(coin)

            statistics.score += 1

            coin.score.updated = True


scanner_engine = ScannerEngine()