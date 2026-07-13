from app.services.ranking_service import ranking_service

coins = ranking_service.top(20)

print()

print("=" * 80)

print("TOP 20")

print("=" * 80)

for coin in coins:

    print(

        f"{coin.score.rank:>3}",

        f"{coin.symbol:<15}",

        f"{coin.score.total:>7.2f}",

        f"{coin.score.rank_change:+4}",

    )