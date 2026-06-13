#Open the program
import subprocess

from app.skills.base import Skill


class SystemSkill(Skill):
    commands = ("команды","проверка связи","работаешь",
                "говори быстрее","говори медленнее",
                "говори тише","говори громче",
                "увеличь громкость","уменьши громкость",
                "громче звук", "тише звук", "открой проводник")
    def __init__(self, tts):
        self.tts = tts

    def can_handle(self, text: str) -> bool:
        user_text = text.lower()
        return any(command in user_text for command in self.commands)

    def handle(self, text: str) -> str:
        user_text = text.lower()
        if "команды" in user_text:
            return ("команды" "проверка связи" "работаешь"
                "говори быстрее" "говори медленнее"
                "говори тише" "говори громче"
                "увеличь громкость" "уменьши громкость"
                "громче звук" "тише звук" "открой проводник")

        if "проверка связи" in user_text:
            return "Я тут"

        if "работаешь" in user_text:
            return "Работаю"

        if "говори быстрее" in user_text:
            self.tts.setHigherRate(self.tts.rate + 50)
            return "Буду говорить быстрее"

        if "говори медленнее" in user_text:
            self.tts.setLowerRate(self.tts.rate - 50)
            return "Буду говорить медленнее"

        if "говори тише" in user_text or "уменьши громкость" in user_text:
            self.tts.setLowerVolume(self.tts.volume - 0.5)
            return "Буду говорить тише"

        if "говори громче" in user_text or "увеличь громкость" in user_text:
            self.tts.setHigherVolume(self.tts.volume + 0.5)
            return "Буду говорить громче"

        if "громче звук" in user_text:
            new_volume = self.change_volume(10)
            return f"звук поставлен на {new_volume}"

        if "тише звук" in user_text:
            new_volume = self.change_volume(-10)
            return f"звук поставлен на {new_volume}"

        if "открой проводник" in user_text:
            subprocess.run(["open", "~"])
            return "проводник открыт"

        return "Нету такой команды"


    def change_volume(delta: int) -> int:
        result = subprocess.run(
            ["osascript", "-e", "output volume of (get volume settings)"],
            capture_output=True,
            text=True
        )

        volume = int(result.stdout.strip())

        new_volume = max(0, min(volume + delta, 100))

        subprocess.run([
            "osascript",
            "-e",
            f"set volume output volume {new_volume}"
        ])

        return new_volume
