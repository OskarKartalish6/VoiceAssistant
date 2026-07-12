from app.auth.auth_manager import AuthManager
from app.database.db_manager import DatabaseManager


def test_register():

    db = DatabaseManager()

    auth = AuthManager(db)

    response = auth.register("test_user", "123456")

    assert response is not None

def test_login():
    db = DatabaseManager()

    auth = AuthManager(db)

    auth.register("login_test", "123456")

    response = auth.login("login_test", "123456")

    assert "Добро пожаловать" in response

def test_logout():
    db = DatabaseManager()

    auth = AuthManager(db)

    auth.register("logout_test", "123456")

    auth.login("logout_test", "123456")

    response = auth.logout()

    assert response == "Вы вышли из аккаунта"