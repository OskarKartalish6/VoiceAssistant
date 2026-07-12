from tests.get_router import get_router

def test_google():
    router = get_router()

    response = router.route("найди в интернете python")

    assert "Ищу" in response


def test_youtube():
    router = get_router()

    response = router.route("найди в ютубе котики")

    assert "Ищу" in response

def test_wikipedia():
    router = get_router()

    response = router.route("найди в википедии питон")

    assert "Ищу" in response