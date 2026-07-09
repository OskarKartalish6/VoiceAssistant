import threading
import tkinter as tk

from app.audio.recorder import Recorder
from app.audio.stt import SpeechToText
from app.audio.tts import TextToSpeech

from app.core.assistant import Assistant
from app.core.router import Router

from app.database.db_manager import DatabaseManager
from app.auth.auth_manager import AuthManager

from app.ui.ui_manager import UIManager

from app.logs.logger import Logger

def main():

    root = tk.Tk()
    root.withdraw()

    recorder = Recorder()
    stt = SpeechToText()
    tts = TextToSpeech()

    db = DatabaseManager()
    auth = AuthManager(db)

    ui = UIManager(root, auth, db)

    logger = Logger(db)

    router = Router(
        tts=tts,
        auth=auth,
        ui=ui
    )

    assistant = Assistant(
        recorder,
        stt,
        tts,
        router,
        logger
    )

    threading.Thread(
        target=assistant.run,
        daemon=True
    ).start()

    root.mainloop()


if __name__ == "__main__":
    main()