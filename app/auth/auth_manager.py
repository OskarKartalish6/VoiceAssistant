from app.auth.current_user import CurrentUser
from app.auth.password import Password


class AuthManager:

    def __init__(self, db):
        self.db = db

    def register(self, username: str, password: str) -> str:

        username = username.strip().lower()

        if not username:
            return "Введите имя пользователя"

        if len(password) < 6:
            return "Пароль должен содержать минимум 6 символов"

        if self.db.user_exists(username):
            return "Пользователь уже существует"

        password_hash = Password.hash(password)

        self.db.create_user(username, password_hash)

        return "Регистрация успешно завершена"

    def login(self, username: str, password: str) -> str:

        username = username.strip().lower()

        user = self.db.get_user(username)

        if user is None:
            return "Пользователь не найден"

        user_id = user[0]
        user_name = user[1]
        password_hash = user[2]

        if not Password.verify(password, password_hash):
            return "Неверный пароль"

        CurrentUser.login(user_id, user_name)

        return f"Добро пожаловать, {user_name}"

    def logout(self) -> str:
        if not CurrentUser.is_logged():
            return "Вы не вошли в аккаунт"

        CurrentUser.logout()

        return "Вы вышли из аккаунта"

    def delete_user(self, password: str) -> str:

        if not CurrentUser.is_logged():
            return "Сначала войдите"

        user = self.db.get_user(CurrentUser.username)

        if user is None:
            return "Ошибка"

        password_hash = user[2]

        if not Password.verify(password, password_hash):
            return "Неверный пароль"

        self.db.delete_user(CurrentUser.id)

        CurrentUser.logout()

        return "Аккаунт удалён"

    def change_password(self, old_password: str, new_password: str) -> str:

        if not CurrentUser.is_logged():
            return "Сначала войдите"

        if len(new_password) < 6:
            return "Пароль слишком короткий"

        user = self.db.get_user(CurrentUser.username)

        if user is None:
            return "Ошибка"

        password_hash = user[2]

        if not Password.verify(old_password, password_hash):
            return "Неверный старый пароль"

        new_hash = Password.hash(new_password)

        self.db.update_password(CurrentUser.id, new_hash)

        return "Пароль успешно изменён"