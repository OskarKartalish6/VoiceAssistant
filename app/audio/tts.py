#Text-to-Speech
import pyttsx3

class TextToSpeech:
    def __init__(self,
                 rate: int = 125,
                 volume: float = 1.0,
                 voice_language: str = "ru",
                 )->None:
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)
        self._select_voice(voice_language)

    def _select_voice(self, voice_language: str)->None:
        voices = self.engine.getProperty("voices")
        language = voice_language.lower()

        for voice in voices:
            voice_data = " ".join(
                str(value).lower()
                for value in (voice.id, voice.name, voice.languages)
            )

            if language in voice_data or "russian" in voice_data:
                self.engine.setProperty("voice", voice.id)
                return

    def say(self, text: str) -> None:
        print("TTS input:", repr(text))
        text = text.strip()

        if not text:
            return

        self.engine.say(text)
        self.engine.runAndWait()
        print("TTS done")

