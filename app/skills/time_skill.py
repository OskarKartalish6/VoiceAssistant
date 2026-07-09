from datetime import datetime

from app.skills.base import Skill
from app.auth.current_user import CurrentUser


class TimeSkill(Skill):

    INTENTS = [
        "GET_TIME",
        "GET_WEEKDAY",
        "GET_DAY",
        "GET_DATE"
    ]

    def handle(self, text: str, intent: str, command: str) -> str:
        if not CurrentUser.is_logged():
            return "Войдите в акаунт"

        if intent == "GET_TIME":
            now = datetime.now()
            return f"Сейчас {now.hour}:{now.minute:02d}"

        if intent == "GET_WEEKDAY":
            day = datetime.today().weekday()

            weekdays = (
                "Понедельник",
                "Вторник",
                "Среда",
                "Четверг",
                "Пятница",
                "Суббота",
                "Воскресенье"
            )
            return f"Сегодня {weekdays[day]}"

        if intent == "GET_DAY":
            day = datetime.today()
            return f"Сегодня {day.day}"

        if intent == "GET_DATE":
            day = datetime.today()
            return f"Сегодня {day.date()}"