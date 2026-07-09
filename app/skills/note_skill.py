from app.skills.base import Skill
from app.database.db_manager import DatabaseManager
from app.auth.current_user import CurrentUser


class NoteSkill(Skill):

    INTENTS = [
        "CREATE_NOTE",
        "READ_NOTE",
        "DELETE_NOTE",
        "ADD_CONTENT_NOTE",
        "LIST_NOTES"
    ]
    def __init__(self):

        self.db = DatabaseManager()

    def handle(self, text: str, intent: str, command: str) -> str:
        if not CurrentUser.is_logged():
            return "Войдите в акаунт"

        if intent == "CREATE_NOTE":

            name = text.replace(
                command,
                ""
            ).strip()

            self.db.create_note(name)

            return f"Заметка {name} создана"
        if intent == "ADD_CONTENT_NOTE":
            data = text.replace(command, "").strip().split(" ", 1)

            if len(data) < 2:
                return "Недостаточно данных"
            note_name, content = data
            self.db.add_content(note_name, content)
            return f"{content} добавлен в {note_name}"
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