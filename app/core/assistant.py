#Assistant's Main Loop
import time

class Assistant:
    stop_words = ("пока",
            "заткнись",
            "иди нахуй",
            "стоп",
            "завали ебало")

    def __init__(self, recorder, stt, tts, router, logger):
        self.recorder = recorder
        self.stt = stt
        self.tts = tts
        self.router = router
        self.is_speaking = False
        self.logger = logger

    def say(self, text: str) -> None:
        self.is_speaking = True
        self.recorder.enabled = False
        self.recorder.clear()

        self.tts.say(text)

        time.sleep(2.0)
        self.recorder.clear()
        self.stt.reset()

        self.recorder.enabled = True
        self.is_speaking = False

    def run(self) -> None:
        self.say("Assistant started")

        for audio_chunk in self.recorder.listen():

            print("Assistant is listening. Say something...")
            if self.is_speaking:
                continue

            text = self.stt.recognize(audio_chunk)
            if not text:
                continue

            print(f"You said: {text}")
            text = text.lower()

            if text in self.stop_words:
                print("Assistant stopped.")
                self.say("Assistant stopped")
                break

            try:

                response = self.router.route(text)
                self.logger.user.log(text, response)
                print(f"Assistant: {response}")
                self.say(response)

            except Exception as e:

                self.logger.system.log(text, e)
                self.say("Произошла ошибка")
