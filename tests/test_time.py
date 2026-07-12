from tests.get_router import get_router


def test_time():
    router = get_router()

    response = router.route("время")

    assert "Сейчас" in response

def test_date():
    router = get_router()

    response = router.route("какая сегодня дата")

    assert "Сегодня" in response

def test_weekday():
    router = get_router()

    response = router.route("день недели")

    assert "Сегодня" in response