#Time, Date
from datetime import datetime

from app.skills.base import Skill

class TimeSkill(Skill):
    def can_handle(self, text: str) -> bool:
        phrases = ("время", "день недели",
                   "какое сегодня число",
                   "какая сегодня дата"
        )

        return any(phrase in text for phrase in phrases)

    def handle(self, text: str) -> str:
        if "время" in text:
            now = datetime.now()
            return f"Сейчас {now.hour}:{now.minute:02d}"
        if "день недели" in text:
            day = datetime.today().weekday()
            for i in range(0, 7):
                if day == i:  weekday = "Понедельник"
                if day == i:  weekday = "Вторник"
                if day == i:  weekday = "Среда"
                if day == i:  weekday = "Четверг"
                if day == i:  weekday = "Пятница"
                if day == i:  weekday = "Субота"
                if day == i:  weekday = "Воскресенье"
            return f"Сегодня {weekday}"
        if "какое сегодня число" in text:
            day = datetime.today()
            return f"Сегодня {day.today().day}"
        if "какая сегодня дата" in text:        # не работает
            day = datetime.today()
            return f"Сегодня {day.today().date()}"