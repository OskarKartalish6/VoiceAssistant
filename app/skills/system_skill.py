import subprocess

from app.skills.base import Skill


class SystemSkill(Skill):

    INTENTS = [
        "SHOW_COMMANDS",
        "PING",
        "FASTER_SPEECH",
        "SLOWER_SPEECH",
        "LOUDER_TTS",
        "QUIETER_TTS",
        "SYSTEM_VOLUME_UP",
        "SYSTEM_VOLUME_DOWN",
        "OPEN_EXPLORER"
    ]
    
    def __init__(self, tts):
        self.tts = tts

    def handle(
            self,
            text: str,
            intent: str,
            command: str
    ):

        if intent == "SHOW_COMMANDS":

            return (
                "команды, проверка связи, работаешь, "
                "говори быстрее, говори медленнее, "
                "говори тише, говори громче, "
                "громче звук, тише звук, "
                "открой проводник"
            )

        if intent == "PING":

            if "работаешь" in text:
                return "Работаю"

            return "Я тут"

        if intent == "FASTER_SPEECH":

            self.tts.setHigherRate(
                self.tts.rate + 50
            )

            return "Буду говорить быстрее"

        if intent == "SLOWER_SPEECH":

            self.tts.setLowerRate(
                self.tts.rate - 50
            )

            return "Буду говорить медленнее"

        if intent == "LOUDER_TTS":

            self.tts.setHigherVolume(
                self.tts.volume + 0.2
            )

            return "Буду говорить громче"

        if intent == "QUIETER_TTS":

            self.tts.setLowerVolume(
                self.tts.volume - 0.2
            )

            return "Буду говорить тише"

        if intent == "SYSTEM_VOLUME_UP":

            volume = self.change_volume(10)

            return f"Системная громкость {volume}"

        if intent == "SYSTEM_VOLUME_DOWN":

            volume = self.change_volume(-10)

            return f"Системная громкость {volume}"

        if intent == "OPEN_EXPLORER":

            subprocess.run(["open", "/Users"])

            return "Проводник открыт"

        return "Команда не поддерживается"

    def change_volume(self, delta: int) -> int:
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
