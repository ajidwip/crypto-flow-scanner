from __future__ import annotations


class CVD:

    def __init__(self):

        self.value = 0.0

    def add(
        self,
        quantity: float,
        buyer_maker: bool,
    ):

        if buyer_maker:

            self.value -= quantity

        else:

            self.value += quantity

    def reset(self):

        self.value = 0.0