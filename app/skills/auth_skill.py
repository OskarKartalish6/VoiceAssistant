from app.skills.base import Skill


class AuthSkill(Skill):

    INTENTS = [
        "REGISTER",
        "LOGIN",
        "LOGOUT"
    ]

    def __init__(self, auth, ui):
        self.auth = auth
        self.ui = ui

    def handle(self, text: str, intent: str, command: str):

        if intent == "REGISTER":
            self.ui.open_register()
            return "Открываю регистрацию."

        if intent == "LOGIN":
            self.ui.open_login()
            return "Открываю вход."

        if intent == "LOGOUT":
            return self.auth.logout()