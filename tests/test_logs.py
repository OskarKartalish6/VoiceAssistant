from tests.get_router import get_router


def test_logs():
    router = get_router()

    response = router.route("покажи логи")

    assert response == "Открываю логи"
