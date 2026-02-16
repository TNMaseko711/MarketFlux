"""Reusable technical indicator calculations for stream jobs."""


def sma(values: list[float], window: int) -> float | None:
    if len(values) < window:
        return None
    return sum(values[-window:]) / window


def ema(values: list[float], window: int) -> float | None:
    if not values:
        return None
    multiplier = 2 / (window + 1)
    ema_value = values[0]
    for value in values[1:]:
        ema_value = (value - ema_value) * multiplier + ema_value
    return ema_value
