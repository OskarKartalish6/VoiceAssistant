from app.skills.note_skill import NoteSkill
from app.skills.browser_skill import BrowserSkill
from app.skills.timer_skill import TimerSkill
from app.skills.system_skill import SystemSkill
from app.skills.calculator_skill import CalculatorSkill
from app.skills.time_skill import TimeSkill
from app.skills.weather_skil import WeatherSkill

from app.core.intent_recognizer import IntentRecognizer


class Router:

    def __init__(self, tts):

        self.recognizer = IntentRecognizer()

        skills = [
            NoteSkill(),
            BrowserSkill(),
            TimerSkill(),
            SystemSkill(tts),
            CalculatorSkill(),
            TimeSkill(),
            WeatherSkill()
        ]

        self.skills = {}

        for skill in skills:

            for intent in skill.INTENTS:

                self.skills[intent] = skill

    def route(self, text: str):

        intent, command = (
            self.recognizer.recognize(text)
        )

        if not intent:

            return "Команда не распознана"

        skill = self.skills.get(intent)

        if not skill:

            return "Skill не найден"

        return skill.handle(
            text,
            intent,
            command
        )