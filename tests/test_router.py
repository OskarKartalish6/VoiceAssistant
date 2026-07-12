from tests.get_router import get_router


def test_router():
    router = get_router()

    list_command = ["погода гамбург", "сколько будет 2+2",
                    "тише звук","покажи заметки",
                    "найди в интернете", "проверка связи",
                    "говори быстрее", "время"]
    for command in list_command:
        response = router.route(command)
        assert response is not None

