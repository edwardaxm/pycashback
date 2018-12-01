from app.cashback import cashback


def test_cashback_under_limit():
    result = cashback(1000)

    assert 50 == result


def test_cashback_upper_limit():
    result = cashback(100000)

    assert 3000 == result
