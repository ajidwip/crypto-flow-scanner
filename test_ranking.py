from app.services.ranking_service import ranking_service

for coin in ranking_service.top(20):

    print(

        coin.symbol,

        round(coin.score.total, 2),

        coin.score.signal

    )