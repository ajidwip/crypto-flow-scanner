from __future__ import annotations


class DeltaVolume:

    def __init__(self):

        self.buy = 0.0

        self.sell = 0.0

    def add(
        self,
        quantity: float,
        buyer_maker: bool,
    ):

        if buyer_maker:

            self.sell += quantity

        else:

            self.buy += quantity

    @property
    def delta(self):

        return self.buy - self.sell

    @property
    def total(self):

        return self.buy + self.sell

    @property
    def pressure(self):

        if self.total == 0:

            return 0

        return self.delta / self.total

    def reset(self):

        self.buy = 0.0

        self.sell = 0.0