from src.operators.technical_indicators import ema, sma


def test_sma():
    assert sma([1, 2, 3, 4], 2) == 3.5


def test_ema_returns_number():
    assert ema([1, 2, 3, 4], 3) is not None
