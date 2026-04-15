from peg_tracker import get_coin_id, calculate_peg_deviation, classify_peg_status


def test_get_coin_id():
    assert get_coin_id("USDC") == "usd-coin"
    assert get_coin_id("USDT") == "tether"
    assert get_coin_id("DAI") == "dai"
    assert get_coin_id("BTC") is None


def test_calculate_peg_deviation():
    assert round(calculate_peg_deviation(1.00), 2) == 0.00
    assert round(calculate_peg_deviation(1.01), 2) == 1.00
    assert round(calculate_peg_deviation(0.99), 2) == -1.00


def test_classify_peg_status():
    assert classify_peg_status(1.0) == "Above peg"
    assert classify_peg_status(-1.0) == "Below peg"
    assert classify_peg_status(0.1) == "On peg"
