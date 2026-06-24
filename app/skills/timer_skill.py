from app.skills.base import Skill

from words2numsrus import NumberExtractor

from threading import Timer

import subprocess
import re


class TimerSkill(Skill):

    INTENTS = [
        "CREATE_TIMER",
        "STOP_TIMER"
    ]

    extractor = NumberExtractor()

    def __init__(self):
        self.timer = None

    def handle(self, text: str, intent: str, command: str):

        if intent == "CREATE_TIMER":

            normalized_text = (self.extractor.replace_groups(text))

            match = re.search(r"\d+", normalized_text)

            if not match:
                return "Не удалось определить время"

            number = int(match.group())

            seconds = self.parse_duration(text, number)

            if seconds is None:
                return ("Укажи секунды, минуты или часы")

            self.start_timer(seconds)

            return (f"Таймер поставлен на {number}")

        if intent == "STOP_TIMER":

            if self.timer is None:
                return ("Нет активного таймера")

            self.timer.cancel()

            self.timer = None

            return "Таймер остановлен"

    def parse_duration(self, text: str, number: int):

        text = text.lower()

        if "секунд" in text:
            return number

        if "минут" in text:
            return number * 60

        if "час" in text:
            return number * 3600

        return None

    def start_timer(self, seconds: int):

        if self.timer:
            self.timer.cancel()

        self.timer = Timer(seconds, self.timer_finished)

        self.timer.start()

    def timer_finished(self):

        self.timer = None

        subprocess.run(
            [
                "afplay",
                "/Users/kartalishoskar/PycharmProjects/VoiceAssistant/additionalFiles/htc_basic.mp3"
            ]
        )

        print("Таймер закончился")