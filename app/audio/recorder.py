import queue
from collections.abc import Generator

import pyaudio

class Recorder:

    def __init__(
        self,
        samplerate: int = 16000,
        channels: int = 1,
        blocksize: int = 4000,
        enabled: bool = True
    ) -> None:

        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize

        self._audio_queue: queue.Queue[bytes] = queue.Queue()

        self.audio = pyaudio.PyAudio()

        self.enabled = enabled

    def _callback(
            self,
            in_data,
            frame_count,
            time_info,
            status
    ):
        if not self.enabled:
            return (None, pyaudio.paContinue)

        self._audio_queue.put(in_data)

        return (None, pyaudio.paContinue)

    def clear(self):
        while not self._audio_queue.empty():
            self._audio_queue.get_nowait()

    def listen(self) -> Generator[bytes, None, None]:

        stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.samplerate,
            input=True,
            frames_per_buffer=self.blocksize,
            stream_callback=self._callback
        )

        stream.start_stream()

        try:
            while True:
                yield self._audio_queue.get()

        finally:
            stream.stop_stream()
            stream.close()