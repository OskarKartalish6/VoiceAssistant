from app.audio.recorder import Recorder
from app.audio.stt import SpeechToText
from app.audio.tts import TextToSpeech
from app.core.assistant import Assistant
from app.core.router import CommandRouter
from app.skills.browser_skill import BrowserSkill
from app.skills.time_skill import TimeSkill
from app.skills.weather_skil import WeatherSkill
from app.skills.system_skill import SystemSkill
from app.skills.timer_skill import TimerSkill
from app.skills.calculator_skill import CalculatorSkill


def main():
    recorder = Recorder()
    stt = SpeechToText()
    tts = TextToSpeech()

    router = CommandRouter(
        skills=[
            TimeSkill(),
            BrowserSkill(),
            WeatherSkill(),
            SystemSkill(tts),
            TimerSkill(),
            CalculatorSkill()
        ]
    )

    assistant = Assistant(
        recorder=recorder,
        stt=stt,
        tts=tts,
        router=router,
    )

    assistant.run()


if __name__ == "__main__":
    main()