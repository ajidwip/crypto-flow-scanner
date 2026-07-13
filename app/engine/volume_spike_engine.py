from __future__ import annotations


class VolumeSpikeEngine:

    def calculate(
        self,
        coin,
    ):

        candles = coin.candles

        if len(candles) < 30:
            return

        history = list(candles)[-21:-1]

        avg = sum(
            c.volume
            for c in history
        ) / len(history)

        current = candles[-1].volume

        if avg <= 0:

            ratio = 0

        else:

            ratio = current / avg

        if ratio >= 5:
            score = 100
        elif ratio >= 4:
            score = 90
        elif ratio >= 3:
            score = 80
        elif ratio >= 2:
            score = 60
        elif ratio >= 1.5:
            score = 40
        elif ratio >= 1:
            score = 20
        else:
            score = ratio * 20

        spike = coin.volume_spike

        spike.average_volume = avg

        spike.current_volume = current

        spike.ratio = ratio

        spike.score = score

        spike.updated = True


volume_spike_engine = VolumeSpikeEngine()