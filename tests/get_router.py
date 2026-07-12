from app.auth.current_user import CurrentUser
from tests.test_factory import create_router


def get_router():
    CurrentUser.login(1, "dante")
    return create_router()