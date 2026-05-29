#Speech-to-Text
import json
from pathlib import Path

from vosk import KaldiRecognizer, Model


class SpeechToText:
    def __init__(
        self,
        model_path: str | Path = "models/vosk-model-small-ru",
        samplerate: int = 16_000,
    ) -> None:
        self.model_path = Path(model_path)
        self.samplerate = samplerate

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Vosk model was not found: {self.model_path}."
            )

        self.model = Model(str(self.model_path))
        self.recognizer = KaldiRecognizer(self.model, self.samplerate)

    def recognize(self, audio_chunk: bytes) -> str | None:
        if self.recognizer.AcceptWaveform(audio_chunk):
            result = json.loads(self.recognizer.Result())
            text = result.get("text", "").strip()
            return text or None

        return None

    def get_partial_text(self) -> str | None:
        result = json.loads(self.recognizer.PartialResult())
        text = result.get("partial", "").strip()
        return text or None

    def get_final_text(self) -> str | None:
        result = json.loads(self.recognizer.FinalResult())
        text = result.get("text", "").strip()
        return text or None