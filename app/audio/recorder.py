#Microphone recording
import queue
from collections.abc import Generator

import sounddevice as sd


class Recorder:
    def __init__(
        self,
        samplerate: int = 16_000,
        channels: int = 1,
        dtype: str = "int16",
        blocksize: int = 16_000,
    ) -> None:
        self.samplerate = samplerate
        self.channels = channels
        self.dtype = dtype
        self.blocksize = blocksize
        self._audio_queue: queue.Queue[bytes] = queue.Queue()

    def _callback(self, indata, frames, time, status) -> None:
        if status:
            print(f"Recorder status: {status}")

        self._audio_queue.put(bytes(indata))

    def listen(self) -> Generator[bytes, None, None]:
        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            dtype=self.dtype,
            channels=self.channels,
            callback=self._callback,
        ):
            while True:
                yield self._audio_queue.get()
