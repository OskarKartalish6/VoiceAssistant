from tests.get_router import get_router


def test_create_note():
    router = get_router()

    response = router.route("создай заметку тест")

    assert response == "Заметка тест создана"

def test_delete_note():
    router = get_router()

    router.route("создай заметку тест")

    response = router.route("удали заметку тест")

    assert response == "Заметка тест удалена"


def test_show_notes():
    router = get_router()

    response = router.route("покажи заметки")

    assert response is not None
