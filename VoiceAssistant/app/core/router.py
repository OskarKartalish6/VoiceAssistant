# Command selection
from app.skills.base import Skill

class CommandRouter:
    def __init__(self, skills: list[Skill]) -> None:
        self.skills = skills

    def route(self, text: str) -> str:
        normalized_text = self._normalize(text)

        for skill in self.skills:
            if skill.can_handle(normalized_text):
                return skill.handle(normalized_text)

        return "I do not understand this command yet."

    def _normalize(self, text: str) -> str:
        return text.strip().lower()