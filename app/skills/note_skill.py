from app.skills.base import Skill
from app.database.db_manager import DatabaseManager


class NoteSkill(Skill):

    INTENTS = [
        "CREATE_NOTE",
        "READ_NOTE",
        "DELETE_NOTE",
        "LIST_NOTES"
    ]
    def __init__(self):

        self.db = DatabaseManager()

    def handle(self, text: str, intent: str, command: str) -> str:

        if intent == "CREATE_NOTE":

            name = text.replace(
                command,
                ""
            ).strip()

            self.db.create_note(name)

            return f"Заметка {name} создана"

        if intent == "READ_NOTE":

            name = text.replace(
                command,
                ""
            ).strip()

            content = self.db.get_note(name)

            return content or "Заметка не найдена"

        if intent == "DELETE_NOTE":

            name = text.replace(
                command,
                ""
            ).strip()

            self.db.delete_note(name)

            return f"Заметка {name} удалена"

        if intent == "LIST_NOTES":

            notes = self.db.get_notes()

            if not notes:
                return "Заметок нет"

            return ", ".join(notes)