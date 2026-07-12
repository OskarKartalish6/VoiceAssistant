from tests.get_router import get_router


def test_calculator():
    router = get_router()

    response = router.route("сколько будет 2+2")

    assert response == "Будет: 4"
