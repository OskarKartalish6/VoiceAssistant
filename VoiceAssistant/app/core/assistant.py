#Assistant's Main Loop


class Assistant:
    stop_words = ("пока",
            "заткнись",
            "иди нахуй",
            "стоп")
    def __init__(self, recorder, stt, tts, router):
        self.recorder = recorder
        self.stt = stt
        self.tts = tts
        self.router = router
        self.running = True

    def run(self) -> None:
        self.tts.say("Assistant started")

        for audio_chunk in self.recorder.listen():
            print("Assistant is listening. Say something...")
            text = self.stt.recognize(audio_chunk)

            if not text:
                continue

            print(f"You said: {text}")
            response = self.router.route(text)
            print(f"Assistant: {response}")
            self.tts.say(response)

            text = text.lower()
            if text in self.stop_words:
                print("Assistant stopped.")
                self.tts.say("Assistant stopped")
                break