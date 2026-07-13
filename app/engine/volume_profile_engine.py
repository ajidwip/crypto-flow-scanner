from __future__ import annotations

from collections import defaultdict


class VolumeProfileEngine:

    def calculate(
        self,
        coin,
    ):

        candles = coin.candles

        if len(candles) < 200:
            return

        tick = coin.tick_size

        if tick <= 0:
            tick = 0.01

        buckets = defaultdict(float)

        for candle in list(candles)[-200:]:

            price = round(
                round(candle.close / tick) * tick,
                coin.price_precision,
            )

            buckets[price] += candle.volume

        if not buckets:
            return

        sorted_profile = sorted(
            buckets.items(),
            key=lambda x: x[0],
        )

        prices = [
            p
            for p, _ in sorted_profile
        ]

        volumes = [
            v
            for _, v in sorted_profile
        ]

        poc = max(
            buckets.items(),
            key=lambda x: x[1],
        )[0]

        total_volume = sum(volumes)

        target_volume = total_volume * 0.70

        poc_index = prices.index(poc)

        left = poc_index
        right = poc_index

        current_volume = volumes[poc_index]

        while current_volume < target_volume:

            left_volume = -1
            right_volume = -1

            if left > 0:

                left_volume = volumes[left - 1]

            if right < len(volumes) - 1:

                right_volume = volumes[right + 1]

            if left_volume >= right_volume:

                if left > 0:

                    left -= 1

                    current_volume += volumes[left]

                elif right < len(volumes) - 1:

                    right += 1

                    current_volume += volumes[right]

                else:

                    break

            else:

                if right < len(volumes) - 1:

                    right += 1

                    current_volume += volumes[right]

                elif left > 0:

                    left -= 1

                    current_volume += volumes[left]

                else:

                    break

        coin.volume_profile.poc = poc

        coin.volume_profile.val = prices[left]

        coin.volume_profile.vah = prices[right]

        coin.volume_profile.total_volume = total_volume

        coin.volume_profile.updated = True


volume_profile_engine = VolumeProfileEngine()