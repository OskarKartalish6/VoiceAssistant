from tests.get_router import get_router


def test_weather():

    router = get_router()

    response = router.route("погода гамбург")

    assert response is not None