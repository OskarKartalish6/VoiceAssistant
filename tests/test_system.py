from tests.get_router import get_router


def test_ping():
    router = get_router()

    response = router.route("проверка связи")

    assert response == "Я тут"

def test_volume_down():
    router = get_router()

    response = router.route("говори тише")

    assert response == "Буду говорить тише"

def test_volume_up():
    router = get_router()

    response = router.route("говори громче")

    assert response == "Буду говорить громче"