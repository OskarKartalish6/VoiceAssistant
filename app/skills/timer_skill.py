from app.skills.base import Skill
from words2numsrus import NumberExtractor
import re
from threading import Timer
import subprocess

class TimerSkill(Skill):
    extractor = NumberExtractor()
    timer = None
    def can_handle(self, text: str) -> bool:
        phrases = (
            "поставь таймер на", "таймер на",
            "сбрось таймер", "останови таймер"
        )
        return any(phrase in text for phrase in phrases)

    def handle(self, text: str) -> str:
        if "поставь таймер на" in text or "таймер на" in text:
            normalized_text = self.extractor.replace_groups(text)

            match = re.search(r"\d+", normalized_text)

            if match:
                number = int(match.group())

                if "секунд" in text:
                    self.timer = Timer(number, self.timer_finished)
                    self.timer.start()
                    return f"Таймер поставлен на {number} секунд"
                if "минут" in text:
                    self.timer = Timer(number * 60, self.timer_finished)
                    self.timer.start()
                    return f"Таймер поставлен на {number} минут"
                if "час" in text:
                    self.timer = Timer(number * 3600, self.timer_finished)
                    self.timer.start()
                    return f"Таймер поставлен на {number} час"
        if "сбрось таймер" in text or "останови таймер" in text:
            if self.timer is not None:
                self.timer.cancel()
                self.timer = None
                return "Таймер остановлен"

    def timer_finished(self):
        subprocess.run(["afplay", "/Users/kartalishoskar/PycharmProjects/VoiceAssistant/additionalFiles/htc_basic.mp3"])
        print("Таймер закончился!!!!!!")
