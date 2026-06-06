#Time, Date
from datetime import datetime

from app.skills.base import Skill

class TimeSkill(Skill):
    def can_handle(self, text: str) -> bool:
        phrases = (
            "сколько времени",
            "который час",
            "скажи время",
            "время",
        )

        return any(phrase in text for phrase in phrases)

    def handle(self, text: str) -> str:
        now = datetime.now()
        return f"Сейчас {now.hour}:{now.minute:02d}"
