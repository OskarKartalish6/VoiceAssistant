from app.skills.base import Skill
from app.auth.current_user import CurrentUser


class LogsSkill(Skill):

    INTENTS = [
        "LOGS"
    ]
    def __init__(self, ui):
        self.ui = ui

    def handle(self, text: str, intent: str, command: str) -> str:
        if not CurrentUser.is_logged():
            return "Войдите в акаунт"

        if intent == "LOGS":
            self.ui.open_logs()
            return "Открываю логи"