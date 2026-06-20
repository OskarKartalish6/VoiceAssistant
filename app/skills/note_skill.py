from app.skills.base import Skill
from app.datebase.db_manager import DatebaseManager

class NoteSkill(Skill):
    def __init__(self):
        self.db = DatebaseManager()

    def can_handle(self, text: str) -> bool:
        phrases = ("создай заметку","добавь в заметку",
                   "прочитай заметку", "все заметки",
                   "удалить заметку")

        return any(phrase in text for phrase in phrases)
    def handle(self, text: str) -> str:
        if "создай заметку" in text:
            name = text.strip().split()
            if len(name) != 3:
                return "Некоректное имя заметки"
            self.db.create_note(name[-1])
            return f"Заметка {name[-1]} создана"

        if "добавь в заметку" in text:
            parts = text.replace("добавь в заметку", "").strip().split(" ", 1)

            name = parts[0]
            content = parts[1] if len(parts) > 1 else ""
            print(content)

            self.db.add_content(name, content)
            return f"Добавлено в {name}"

        if "прочитай заметку" in text:
            name = text.strip().split()
            if len(name) != 3:
                return "Заметка не найдена"
            content = self.db.get_note(name[-1])
            return content

        if "все заметки" in text:
            names = self.db.get_notes()
            if not names:
                return "Заметок нет"

            return ", ".join(names)
        if "удалить заметку" in text:
            name = text.split()[-1]
            self.db.delete_note(name)
            return f"Заметка {name} удалена"



