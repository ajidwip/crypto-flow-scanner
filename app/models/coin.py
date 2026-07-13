from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from dataclasses import field

from app.models.base import BaseModel
from app.models.candle import Candle
from app.models.history import History
from app.models.indicator import Indicator
from app.models.score import Score
from app.models.state import State
from app.realtime.trade_cache import TradeCache
from app.realtime.whale_cache import WhaleCache
from app.realtime.delta_volume import DeltaVolume
from app.realtime.cvd import CVD
from app.models.order_book import OrderBook
from app.models.volume_profile import VolumeProfile
from app.models.volume_spike import VolumeSpike
from app.models.rvol import RVOL
from app.models.open_interest import OpenInterest
from app.models.signal import Signal
from app.models.timeframe_trend import TimeframeTrend
from app.models.order_book import OrderBook
from app.models.orderbook_score import OrderBookScore

@dataclass(slots=True)
class Coin(BaseModel):
    """
    Runtime object for one trading symbol.
    """

    symbol: str = ""

    base_asset: str = ""

    quote_asset: str = ""

    status: str = "TRADING"

    price_precision: int = 0

    quantity_precision: int = 0

    tick_size: float = 0.0

    step_size: float = 0.0

    max_history: int = 500

    candles: deque[Candle] = field(
        default_factory=lambda: deque(maxlen=500)
    )

    indicator: Indicator = field(default_factory=Indicator)

    score: Score = field(default_factory=Score)

    history: History = field(default_factory=History)

    trade_cache: TradeCache = field(
        default_factory=TradeCache
    )

    whale_cache: WhaleCache = field(
        default_factory=WhaleCache
    )

    delta_volume: DeltaVolume = field(
        default_factory=DeltaVolume
    )

    cvd: CVD = field(
        default_factory=CVD
    )

    order_book: OrderBook = field(
        default_factory=OrderBook
    )

    volume_profile: VolumeProfile = field(
        default_factory=VolumeProfile
    )

    volume_spike: VolumeSpike = field(
        default_factory=VolumeSpike
    )

    rvol: RVOL = field(
        default_factory=RVOL
    )

    open_interest: OpenInterest = field(
        default_factory=OpenInterest
    )

    signal: Signal = field(
        default_factory=Signal
    )

    timeframe: TimeframeTrend = field(
        default_factory=TimeframeTrend
    )

    order_book: OrderBook = field(
        default_factory=OrderBook
    )

    order_book_score: OrderBookScore = field(
        default_factory=OrderBookScore
    )

    live_candle: Candle | None = None

    state: State = field(default_factory=State)
    
    def add_candle(self, candle: Candle) -> None:
        """
        Add new candle into memory.
        """
        self.candles.append(candle)

        self.state.last_price = candle.close
        self.state.last_volume = candle.volume
        self.state.last_close_time = candle.close_time
        self.state.candle_count += 1
        self.state.last_update_time = candle.created_at

    @property
    def last_candle(self) -> Candle | None:
        if not self.candles:
            return None

        return self.candles[-1]

    @property
    def first_candle(self) -> Candle | None:
        if not self.candles:
            return None

        return self.candles[0]

    @property
    def close_prices(self) -> list[float]:
        return [c.close for c in self.candles]

    @property
    def high_prices(self) -> list[float]:
        return [c.high for c in self.candles]

    @property
    def low_prices(self) -> list[float]:
        return [c.low for c in self.candles]

    @property
    def volumes(self) -> list[float]:
        return [c.volume for c in self.candles]

    @property
    def working_candles(self) -> list[Candle]:

        candles = list(self.candles)

        if self.live_candle:

            candles.append(self.live_candle)

        return candles

    @property
    def working_close_prices(self):

        return [

            c.close

            for c in self.working_candles

        ]
    
    @property
    def working_high_prices(self):

        return [

            c.high

            for c in self.working_candles

        ]

    @property
    def working_low_prices(self):

        return [

            c.low

            for c in self.working_candles

        ]

    @property
    def working_volumes(self):

        return [

            c.volume

            for c in self.working_candles

        ]

    def clear(self) -> None:
        """
        Reset runtime data.
        """

        self.candles.clear()

        self.history.clear()

        self.score.reset()

        self.state.candle_count = 0

        self.state.last_price = 0.0

        self.state.last_volume = 0.0

    @property
    def candle_count(self) -> int:
        return len(self.candles)

    @property
    def ready(self) -> bool:
        """
        Scanner ready after enough candle history.
        """
        return self.candle_count >= 200

    @property
    def latest_price(self) -> float:
        if not self.candles:
            return 0.0

        return self.candles[-1].close

    def __str__(self) -> str:
        return (
            f"{self.symbol} | "
            f"Price={self.latest_price:.4f} | "
            f"Score={self.score.total:.2f}"
        )