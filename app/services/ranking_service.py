from __future__ import annotations

from app.core.market import market

from app.core.priority_market import priority_market


class RankingService:

    def update(self):

        coins = market.all()

        coins.sort(

            key=lambda c: c.score.total,

            reverse=True,

        )

        priority_market.update(
            coins,
            limit=30,
        )

        for rank, coin in enumerate(coins, start=1):

            last = coin.score.rank

            coin.score.last_rank = last

            coin.score.rank = rank

            if last == 0:

                coin.score.rank_change = 0

            else:

                coin.score.rank_change = last - rank

        return coins

    def top(
        self,
        limit: int = 30,
    ):

        coins = self.update()

        return coins[:limit]


ranking_service = RankingService()