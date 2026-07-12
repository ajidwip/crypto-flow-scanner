from __future__ import annotations

from app.core.market import market


class RankingService:

    def top(self, limit=30):

        coins = list(market.all())

        coins.sort(

            key=lambda x: x.score.total,

            reverse=True,

        )

        return coins[:limit]


ranking_service = RankingService()