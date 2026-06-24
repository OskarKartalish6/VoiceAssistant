from app.audio.recorder import Recorder
from app.audio.stt import SpeechToText
from app.audio.tts import TextToSpeech
from app.core.assistant import Assistant
from app.core.router import Router


def main():
    recorder = Recorder()
    stt = SpeechToText()
    tts = TextToSpeech()

    router = Router(tts)

    assistant = Assistant(
        recorder=recorder,
        stt=stt,
        tts=tts,
        router=router,
    )

    assistant.run()


if __name__ == "__main__":
    main()