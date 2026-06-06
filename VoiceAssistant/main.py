from app.audio.recorder import Recorder
from app.audio.stt import SpeechToText
from app.audio.tts import TextToSpeech
from app.core.assistant import Assistant
from app.core.router import CommandRouter
from app.skills.browser_skill import Browserskill
from app.skills.time_skill import TimeSkill


def main():
    recorder = Recorder()
    stt = SpeechToText()
    tts = TextToSpeech()

    router = CommandRouter(
        skills=[
            TimeSkill(),
            Browserskill()
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