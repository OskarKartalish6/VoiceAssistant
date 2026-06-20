#Assistant's Main Loop
class Assistant:
    stop_words = ("пока",
            "заткнись",
            "иди нахуй",
            "стоп",
            "завали ебало")

    def __init__(self, recorder, stt, tts, router):
        self.recorder = recorder
        self.stt = stt
        self.tts = tts
        self.router = router
        self.running = True
        self.is_speaking = False

    def say(self, text: str) -> None:
        self.is_speaking = True

        self.tts.say(text)

        self.is_speaking = False
        self.recorder.clear()

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

            response = self.router.route(text)

            print(f"Assistant: {response}")
            self.say(response)