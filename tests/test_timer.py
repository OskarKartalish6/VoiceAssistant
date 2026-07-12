from tests.get_router import get_router


def test_setTimer():
    router = get_router()

    response = router.route("поставь таймер на 5 минут")

    assert "Таймер поставлен на" in response

def test_deleteTimer():
    router = get_router()

    router.route("поставь таймер на 5 минут")
    response = router.route("останови таймер")

    assert "Таймер остановлен" in response
